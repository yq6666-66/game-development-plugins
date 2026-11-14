# Build-delivery Skill validation · 2026-11-14

Base: `becd721c27c01ef571b3c6a9886019593291bea5`. Added a portable Chinese/English build-and-delivery workflow and evidence card, based on fixed GameCI and Godot GitHub revisions recorded inside the Skill. Original synthesis only; no source code or images copied.

Scope: build identity, cache boundaries, local artifact inspection, target launch and handoff. No gameplay implementation, automatic signing, uploading or deployment. New and existing projects both covered.

Executed from repository root: `python3 scripts/validate_package.py`; `python3 -m unittest discover -s tests -v`; `git diff --check`. Results recorded after execution below.

Document scenario review: a data-only pack cannot pass executable delivery; cache-save failure is distinct from build failure; a declared version ignored by the implementation must not be reported as effective; editor-only operation does not establish packaged startup. These are paper walkthroughs, not engine tests.

Host loading, upstream GameCI execution, Godot export, target-device launch and game behavior: NOT RUN. CI not established. No merge/release.

Executed results: package PASS; 9/9 unit tests PASS; diff check PASS. These check packaging/navigation, not the runtime effectiveness of the new Skill.
