# Skills

| Skill | Purpose |
|-------|---------|
| [narrative](narrative/SKILL.md) | Add a project origin story or repair chronicle links when requested, preserving existing documentation. |
| [PROVENANCE](PROVENANCE.md) | Compatibility entrypoint for older references. |

Reference the skill directly in a prompt, or install the `narrative/` folder in
your assistant's supported skill location. No root configuration files are needed.
For shared-chain work, use the current [chronicle index](../CHRONICLE.md) from this
collection. Standalone narratives do not need the index.

`config.yaml` retains old switch names for migration. All defaults are now off;
missing configuration does not impose conventions. Explicit requests determine
what a skill should do.
