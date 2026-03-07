# ai-template

A project template that enforces consistent conventions, structured development workflows, and a distinctive documentation persona across all AI-assisted repositories.

Repositories cloned from this template automatically inherit rules and skills that guide AI coding assistants — no manual setup or repeated prompting required.

## What It Does

**ai-template** solves the problem of repeating yourself to AI assistants. Instead of explaining your project conventions every session, this template encodes them once and applies them everywhere:

- **Project structure enforcement** — Required directories (`tests/`, `docs/`), Makefile targets (`make`, `make test`, `make start`, `make stop`, `make restart`, `make clean`), and minimum 70% test coverage.
- **Structured development workflows** — Integration with [responsible-vibe-mcp](https://github.com/mrsimpson/responsible-vibe-mcp) for phase-based development (planning, implementation, testing, review) instead of unstructured "vibe coding."
- **Documentation persona** — The PROVENANCE skill mandates a humorous, serialized origin story for every AI-assisted project, featuring the programmer and Sir Reginald von Fluffington III. This serves as both a creative flourish and a practical grep-able marker for AI-assisted work.
- **Security and quality guardrails** — OWASP top-10 awareness, no over-engineering, no scope creep beyond what was requested.

## What's Included

| File / Directory | Purpose |
|-----------------|---------|
| [`CLAUDE.md`](CLAUDE.md) | Project conventions automatically loaded by Claude Code — directory structure, Makefile targets, test coverage, README requirements, code quality rules |
| [`skills/`](skills/) | Reusable AI prompt templates (see [Skills Index](skills/README.md)) |
| [`skills/PROVENANCE.md`](skills/PROVENANCE.md) | The origin story skill — style guide, character notes, chronicle chain, and checklist for adding new chapters |
| `.claude/skills/responsible-vibe/` | Structured development workflow skill for Claude Code |
| `.github/skills/responsible-vibe/` | Structured development workflow skill for GitHub Copilot |
| `.opencode/skills/responsible-vibe/` | Structured development workflow skill for OpenCode |

## Responsible Vibe MCP

The template includes the [responsible-vibe-mcp](https://github.com/mrsimpson/responsible-vibe-mcp) skill across multiple AI assistant platforms. This skill enforces structured development workflows — plan before you code, test what you build, review before you ship — rather than letting the AI jump straight into writing code without a plan.

The skill is installed for:
- **Claude Code** (`.claude/skills/`)
- **GitHub Copilot** (`.github/skills/`)
- **OpenCode** (`.opencode/skills/`)

## Usage

1. Clone or use this repo as a GitHub template for a new project.
2. The `CLAUDE.md` will automatically guide AI assistants to follow project conventions.
3. Replace this `README.md` with a project-specific one — the conventions require it, and will remind the AI to do so.
4. Use the PROVENANCE skill to write your project's origin story chapter and chain it into the chronicle.

## The Documentation Persona

Every project born from this template carries a section called "The Totally True and Not At All Embellished History of [Project Name]." This is not optional decoration — it is a deliberate convention with practical purpose:

- **Provenance tracking** — If a project has this section, an AI was meaningfully involved in its development. If it doesn't, the author worked alone.
- **Serialized narrative** — Each project is a numbered chapter in a continuing chronicle, with navigation links chaining them together across repositories.
- **Consistent voice** — Third-person limited, dry-humorous, mock-historical. The programmer announces things to his cat. The cat does not care.

See [`skills/PROVENANCE.md`](skills/PROVENANCE.md) for the full style guide, character notes, and checklist.

## License

MIT
