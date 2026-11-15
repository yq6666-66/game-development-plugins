# Cloud saves: persistence, synchronization and conflicts

[中文](cloud-save-evidence.md)

Use only where cloud saves are already in scope. This reference does not authorize a new service, accounts or uploading real player data. Local-only games skip it.

Read account/slot identities, save keys, triggers, revision tokens, the approved conflict policy and isolated test data. Trace local write → remote submission → acknowledgement → UI. Distinguish locally durable, pending, remotely acknowledged and conflicting states. A sent request is not acceptance; acceptance does not prove restored object relationships.

Suggested checks, not executed in this research:

- Save offline and restart: local recovery succeeds without a false cloud-success indicator. Check the remote state separately after reconnecting.
- Have A and B read one revision, commit from A, then submit B's stale revision. Observe the approved rejection/merge/explicit-overwrite policy and preserve recoverability of unresolved changes.
- After acknowledgement, reread or use another isolated client to verify the expected version and matching UI.
- Check account/slot isolation and disabled synchronization when supported. Pending changes must not cross identities.

Removing a write-lock token can bypass conflict protection; a successful overwrite is not a passed conflict-resolution test. Unity's new-item omission and existing-item bypass are different cases. Do not use bypass as routine retry logic.

Client timestamps alone do not prove causal ordering (engineering inference requiring project-specific verification). Item locks, file sync and snapshots have different consistency boundaries. Multi-key atomicity, deletion propagation and migrations need separate contracts. Do not mandate a vendor, retry count, UI wording or merge strategy.

## Sources and evidence

Official text/API read on 2026-11-15; no service, engine or game executed. Original paraphrase only.

- Unity [write locks](https://docs.unity.com/en-us/cloud-save/concepts/write-locks), full concept text; online version, publication date unconfirmed.
- Unity [SaveItem / WriteLock](https://docs.unity3d.com/Packages/com.unity.services.cloudsave@3.4/api/Unity.Services.CloudSave.Models.SaveItem.html), constructor/property; package 3.4.2, generated 2026-10-13, not a confirmed publication date.
- Valve [Steam Cloud](https://partner.steamgames.com/doc/features/cloud), overview, best practices, paths, cross-platform and API/Auto-Cloud sections. Session-bound synchronization and user opt-out do not guarantee immediate acknowledgement in any game; device-specific settings should not blindly roam. This mechanism is not Unity's item-level locking.

Reading documentation does not license its code/assets; this repository's MIT license covers this original reference only.
