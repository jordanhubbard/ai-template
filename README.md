# ai-template

Reusable AI skills for existing repositories, with a distinctive project-story
voice and optional examples for new projects and assistant integrations.

## Add a narrative to an existing repository

Ask your assistant:

```text
Use /path/to/ai-template/skills/narrative/SKILL.md to add a project origin story
only if this README does not already have one. Preserve existing documentation.
```

You can also install the `skills/narrative/` folder in your assistant's supported
skill location, or append a reference to your existing instructions. Adoption
does not require copying this repository's root files.

The narrative convention applies to original-work repositories; forks of other
projects are excluded. The skill preserves existing stories and functional README content. Standalone
stories are supported. Joining or repairing the shared chronicle is a separate,
explicitly requested task; see [the chronicle index](CHRONICLE.md).

## What's included

| Path | Purpose |
|------|---------|
| [skills/narrative/SKILL.md](skills/narrative/SKILL.md) | Narrative style and non-destructive adoption guidance |
| [skills/PROVENANCE.md](skills/PROVENANCE.md) | Compatibility with older skill references |
| [CHRONICLE.md](CHRONICLE.md) | Shared chapter index and ordering evidence |
| [scripts/check_chronicle.py](scripts/check_chronicle.py) | Read-only chain and README preservation checks |
| [examples/integrations/](examples/integrations/README.md) | Optional assistant and workflow configuration examples |
| [starters/](starters/README.md) | Optional conventions for new projects |

No mandatory layout, Makefile, coverage target, narrative, or workflow server is
imposed on projects adopting a skill. Keep the destination's license and tool
configuration. The root `CLAUDE.md` and GitHub contribution templates govern this
collection itself.

## The documentation persona

The programmer announces technically ambitious projects to Sir Reginald von
Fluffington III. The cat withholds endorsement. Stories use dry humor,
mock history, and concrete details from the actual project.

A story can mark meaningful AI assistance. Its absence says nothing about whether
AI was involved. The voice is reusable without joining the numbered chronicle.

## Migrating from the old template

- Existing `skills/PROVENANCE.md` references remain supported.
- `skills/config.yaml` retains legacy switch names, now all off. Missing
  configuration also enables no automatic behavior.
- Root assistant/MCP configuration and automatically discovered workflow skills
  have moved to `examples/integrations/`.
- Replace inherited mandatory conventions only where they came from this
  template and the repository owner wants them removed. Preserve local additions.
- Existing repositories are not silently migrated by updating this collection.
  Review each destination's diff; never overwrite its README, license, or config.

## License

This collection is licensed under [BSD 2-Clause](LICENSE); bundled workflow
skills retain their stated upstream license. Adopting a skill does not select or
replace the destination project's license.
