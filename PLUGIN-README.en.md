# Game Development Plugins: installation and use

[中文](PLUGIN-README.md). Initial release 0.1.0 (limited validation) packages seven shared Skills for Codex and Claude Code. It is not a game engine extension. Host runtime compatibility is not established by static package tests.

## Before installation
Use a host version with plugin support. Accounts, policies and model fees belong to the host. No MCP, hooks, background processes, telemetry or secrets are included. Inventory existing manually installed skills before installing; do not overwrite or delete them. Test in an isolated project first.

Extract the candidate ZIP into its own directory, called `./game-development-plugins` below. Keep both manifests and the entire skills tree. Never copy just a manifest.

## Codex
Check `codex --version` and `codex plugin --help`, then run from the directory above the extracted package:

```sh
codex plugin marketplace add ./game-development-plugins
codex plugin add game-development-plugins@game-development-plugins
codex plugin list
```

The catalog is `.agents/plugins/marketplace.json`. Start a new session, ask for `game-prototype-planning`, and check that its actual SKILL.md is loaded. A successful install is not an authenticated model invocation.

## Claude Code
For development: `claude --plugin-dir ./game-development-plugins`. For catalog installation:

```sh
claude plugin validate ./game-development-plugins
claude plugin marketplace add ./game-development-plugins
claude plugin install game-development-plugins@game-development-plugins
claude plugin list
```

Start a session and invoke `/game-development-plugins:game-prototype-planning`. Verify all seven components without duplicates. The manifest intentionally does not redeclare the automatically discovered `skills/` directory.

## Choose a skill

| Task | Skill |
| --- | --- |
| New prototype | [game-prototype-planning](skills/game-prototype-planning/SKILL.md) |
| Architecture and engineering | [game-engineering](skills/game-engineering/SKILL.md) |
| Engines, tools and assets | [game-resource-selection](skills/game-resource-selection/SKILL.md) |
| Visual evidence and iteration | [game-visual-iteration](skills/game-visual-iteration/SKILL.md) |
| Input, saves and restart | [game-playloop-validation](skills/game-playloop-validation/SKILL.md) |
| UI information and interaction | [game-ui-design](skills/game-ui-design/SKILL.md) |
| Build and local delivery | [game-build-delivery](skills/game-build-delivery/SKILL.md) |

New-project example: “Plan only an authorized new prototype: inputs, end state, restart and evidence. Do not implement.”

Existing-project example: “Read only an isolated visual example; propose a baseline, reference-transfer table and same-view comparison. Do not edit.”

Debugging example: “Investigate duplicate events after restart and propose a scoped lifecycle fix.” These examples do not authorize tools, uploads or publication.

## Update, disable, uninstall and rollback
Preserve the previous archive, version and local changes/configuration. Extract an update into a new directory; repeat checks and isolated invocations. Refresh the catalog AND verify the installed plugin version with the host's current update workflow. Codex exposes `codex plugin marketplace upgrade`; inspect help to determine whether reinstallation is required. Claude exposes plugin and marketplace update workflows; inspect their current help. Restart the session and verify actual loading.

Uninstall only this plugin with `codex plugin remove game-development-plugins@game-development-plugins` or `claude plugin uninstall game-development-plugins@game-development-plugins`. Remove a catalog separately only when no longer needed. Never delete the host's entire cache/configuration or user projects. Roll back by installing the retained older package and revalidating.

For duplicate names, inspect manual installations; for missing references, check the full package; for unknown commands, check the host version. Respect organization restrictions. Structure, discovery and actual invocation are separate checks.

## License and release
Original work is [MIT](LICENSE); third-party rights remain separate. Daily research and weekly integration do not imply a release. Publish only after the agreed acceptance gates pass. Source branches, candidate ZIPs, self-hosted catalogs and official directory listings are different states; official listing may require review, account access and terms.

Claude Code auto-update is off by default for custom marketplaces. Publishing a new package does not automatically update users; verify host settings and the installed version.

## 0.1.0 release scope

The owner explicitly approved release with the current evidence and known skipped invocation tests. Linux installation, discovery, uninstall and synthetic local upgrades passed for both hosts; Windows evidence covers only isolated Codex installation/enabling. Real model tasks, remote update propagation, rollback and complete Windows acceptance remain unverified. A GitHub release is not an official store listing or a claim of comprehensive compatibility.
