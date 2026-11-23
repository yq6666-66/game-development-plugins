#!/usr/bin/env python3
"""Fail-closed release approval gate. Does not publish or modify refs."""
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess

REQUIRED = {"codex-install", "codex-invoke", "codex-update", "codex-uninstall",
            "claude-install", "claude-invoke", "claude-update", "claude-uninstall"}

def git(*args):
    return subprocess.check_output(["git", *args])

def validate(record, read, ancestor):
    version = record["version"]
    sha = record["source_sha"]
    if not re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", version):
        raise ValueError("formal version required")
    if version == "0.1.0":
        raise ValueError("historical one-time exception is not reusable")
    if not re.fullmatch(r"[0-9a-f]{40}", sha) or not ancestor(sha):
        raise ValueError("source must be an ancestor of reviewed main")
    if record.get("approved") is not True or record.get("scope") != "github-release":
        raise ValueError("explicit release approval required")
    if not record.get("reviewer") or not record.get("approved_at"):
        raise ValueError("review identity and date required")
    if not re.fullmatch(r"[0-9a-f]{64}", record.get("artifact_sha256", "")):
        raise ValueError("approved artifact digest required")
    evidence = record["evidence"]
    if set(evidence) != REQUIRED:
        raise ValueError("complete dual-host evidence required")
    for name, item in evidence.items():
        p = PurePosixPath(item["path"])
        if p.is_absolute() or ".." in p.parts or not str(p).startswith("docs/validation/"):
            raise ValueError("unsafe evidence path")
        if item.get("status") != "PASS" or not all(item.get(k) for k in ("host_version", "platform", "input", "observed", "date")):
            raise ValueError("runtime evidence, not waiver or structural check, required")
        if item.get("source_sha") != sha or item.get("version") != version:
            raise ValueError("evidence must bind this source and version")
        body = read(str(p))
        if hashlib.sha256(body).hexdigest() != item["sha256"]:
            raise ValueError("evidence digest mismatch")
        proof = json.loads(body)
        for key in ("source_sha", "version", "status", "host_version", "platform", "input", "observed", "date"):
            if proof.get(key) != item[key]:
                raise ValueError("evidence body/approval mismatch")
        if proof.get("operation") != name or proof.get("mode") != "actual-host-runtime" or proof.get("artifact_sha256") != record["artifact_sha256"]:
            raise ValueError("operation and actual runtime artifact evidence required")
        if name.endswith("-update") and proof.get("update_scope") != "remote-candidate-end-to-end":
            raise ValueError("synthetic/local update is not remote propagation evidence")
        log = proof["log"]
        lp = PurePosixPath(log["path"])
        if lp.is_absolute() or ".." in lp.parts or not str(lp).startswith("docs/validation/"):
            raise ValueError("unsafe runtime log path")
        if hashlib.sha256(read(str(lp))).hexdigest() != log["sha256"]:
            raise ValueError("runtime log digest mismatch")
    return version, sha

def main():
    if os.environ.get("GITHUB_REF") != "refs/heads/main" or os.environ.get("GITHUB_EVENT_NAME") != "push":
        raise ValueError("only main push allowed")
    event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    before, after = event["before"], event["after"]
    if after != git("rev-parse", "HEAD").decode().strip() or set(before) == {"0"}:
        raise ValueError("invalid event baseline")
    paths = git("diff", "--name-status", before, after, "--", "docs/releases/approvals").decode().splitlines()
    if len(paths) != 1 or not paths[0].startswith("A\t"):
        raise ValueError("exactly one new approval required; never edit/replay old approvals")
    path = paths[0].split("\t")[1]
    record = json.loads(Path(path).read_text(encoding="utf-8"))
    version, sha = validate(record, lambda p: git("show", f"{after}:{p}"),
                            lambda s: subprocess.run(["git", "merge-base", "--is-ancestor", s, after]).returncode == 0)
    if path != f"docs/releases/approvals/{version}.json":
        raise ValueError("approval filename/version mismatch")
    for p in ("plugin.json", ".claude-plugin/plugin.json"):
        if json.loads(git("show", f"{sha}:{p}"))["version"] != version:
            raise ValueError("source manifest version mismatch")
    if version not in git("show", f"{sha}:CHANGELOG.md").decode():
        raise ValueError("missing changelog")
    with open(os.environ["GITHUB_OUTPUT"], "a") as out:
        out.write(f"version={version}\nsource={sha}\ndigest={record['artifact_sha256']}\n")

if __name__ == "__main__":
    main()
