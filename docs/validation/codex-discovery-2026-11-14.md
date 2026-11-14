# 隔离 Codex 宿主发现检查 / Isolated Codex discovery

日期：2026-11-14。包基线 `21c80e7d7ffde4e53084e1ed38c52630c3b226df`。实际已安装宿主 `codex-cli 0.167.0-alpha.4`，Linux。

## 结果 / Result

**PASS：该版本 app-server 实际发现单个项目级 `game-resource-selection`，读取名称、描述与 UI metadata。** `skills/list` 返回 `scope: repo`、`enabled: true`、预期入口路径与 `errors: []`。隔离副本与仓库 Skill 五个文件逐文件 SHA256 一致。

**BLOCKED / 未验证：认证模型回合中的 Skill 正文加载与执行。** 实际检查确认隔离测试环境未配置模型认证。未复制用户凭据，未登录、调用模型、安装软件或修改个人技能与设置。目录发现和 metadata 解析不能宣称 Agent 已使用完整正文完成任务。

This is real host discovery in the stated version, not merely package validation. Model-turn body injection and actual task execution remain unverified because the isolated home has no authenticated session. It does not certify other Codex versions, hosts, engines or devices.

## 隔离与操作 / Isolation and operations

使用已安装 CLI；子进程环境仅提供 `PATH`、临时 `HOME` 与临时 `CODEX_HOME`。只读仓库 Skill，写入临时目录。宿主在其临时 home 内初始化自带系统 Skills；没有运行这些 Skills 或第三方工具。

```sh
command -v codex
codex --version
codex app-server --help
codex app-server generate-json-schema --help
```

随后用隔离环境执行 schema 生成并读取 `InitializeParams`、`SkillsListParams` 和 `SkillsListResponse`。用标准输入输出启动 `codex app-server --stdio`，发送以下协议（`PROJECT` 替换为临时项目绝对路径）：

```json
{"id":1,"method":"initialize","params":{"clientInfo":{"name":"isolated-skill-check","version":"1.0"}}}
{"method":"initialized"}
{"id":2,"method":"skills/list","params":{"cwds":["PROJECT"],"forceReload":true}}
```

每个有 ID 的请求读取对应响应；检查后终止仅本次启动的子进程。没有启动模型回合。未创建、复制或删除任何凭据。

## 可复现步骤 / Reproduction

从仓库根目录，用标准库创建新的临时目录，设置隔离 home，不读取或复制已有登录配置。以下脚本结构复现本次操作；它需要系统已有 `codex`，不负责安装或登录。临时目录可保留以便查看证据。

```python
import json, os, pathlib, selectors, shutil, subprocess, tempfile, time
root = pathlib.Path(tempfile.mkdtemp(prefix="skill-discovery-"))
for name in ("home", "codex", "project/.agents/skills"):
    (root / name).mkdir(parents=True, exist_ok=True)
source = pathlib.Path("skills/game-resource-selection")
shutil.copytree(source, root / "project/.agents/skills/game-resource-selection")
exe = shutil.which("codex")
if exe is None:
    raise SystemExit("BLOCKED: existing Codex CLI unavailable")
env = {"PATH": os.defpath, "HOME": str(root / "home"),
       "CODEX_HOME": str(root / "codex")}
with (root / "stderr.log").open("w") as log:
    process = subprocess.Popen([exe, "app-server", "--stdio"],
        cwd=root / "project", env=env, stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=log, text=True, bufsize=1)
    selector = selectors.DefaultSelector()
    selector.register(process.stdout, selectors.EVENT_READ)
    def request(message):
        process.stdin.write(json.dumps(message) + "\n")
        process.stdin.flush()
        deadline = time.monotonic() + 20
        while time.monotonic() < deadline:
            if not selector.select(timeout=1):
                continue
            line = process.stdout.readline()
            if not line:
                raise RuntimeError("app-server closed")
            reply = json.loads(line)
            if reply.get("id") == message["id"]:
                return reply
        raise TimeoutError(message["method"])
    try:
        print(request({"id": 1, "method": "initialize", "params": {
            "clientInfo": {"name": "isolated-skill-check", "version": "1.0"}}}))
        process.stdin.write('{"method":"initialized"}\n')
        process.stdin.flush()
        reply = request({"id": 2, "method": "skills/list", "params": {
            "cwds": [str(root / "project")], "forceReload": True}})
        (root / "result.json").write_text(json.dumps(reply, ensure_ascii=False))
        print(reply)
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
print(root)
```

该脚本示例与实际临时探针使用相同协议；未把示例本身的第二次运行作为证据。本次实际探针成功响应与 metadata 的脱敏摘录在[同目录 JSON](codex-discovery-2026-11-14.json)中。真实探针使用固定临时目录和20秒请求超时，仅为检查器选择，不是 Skill 通用重试规则。

## 限制与警告 / Limits and warnings

CLI 打印临时 home 下不创建 PATH helper 的警告，但此次协议初始化和扫描成功。记录警告，不扩大为所有 CLI 功能通过。发现列表还包含宿主自带系统 Skills，本次只判断目标 Skill。安装说明继续要求核对使用者宿主版本；不把本次 `.agents/skills` 实验推广到所有环境。
