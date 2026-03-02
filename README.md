# ai-template

A GitHub template repository containing essential AI skills in the
**Oracle Agent Skills** format, ready to be used as the foundation for any
AI-powered project.

## Overview

This repository provides a curated collection of reusable AI skills that can
be wired into an Oracle Generative AI Agent (or any compatible agent framework)
to give it real-world capabilities such as searching the web, running code,
querying databases, managing email and calendars, and more.

Use this template as the starting point for new AI projects to avoid
re-defining common skills from scratch.

## Repository Structure

```
ai-template/
├── skills/               # Oracle Agent Skills definitions (YAML)
│   ├── README.md         # Skills directory documentation
│   ├── web-search.yaml
│   ├── code-execution.yaml
│   ├── document-retrieval.yaml
│   ├── database-query.yaml
│   ├── email.yaml
│   ├── calendar.yaml
│   ├── file-operations.yaml
│   ├── http-request.yaml
│   ├── image-analysis.yaml
│   └── text-summarization.yaml
└── LICENSE
```

## Skills

| Skill | Description |
|---|---|
| [Web Search](skills/web-search.yaml) | Search the web for current information and return ranked results |
| [Code Execution](skills/code-execution.yaml) | Execute code snippets in a secure sandbox (Python, JS, Bash, …) |
| [Document Retrieval](skills/document-retrieval.yaml) | Semantic search over a knowledge base for RAG workflows |
| [Database Query](skills/database-query.yaml) | Run read-only SQL queries against a configured database |
| [Email](skills/email.yaml) | Send email messages and read inbox content |
| [Calendar](skills/calendar.yaml) | Create, list, update, and delete calendar events |
| [File Operations](skills/file-operations.yaml) | Read, write, append, list, and delete workspace files |
| [HTTP Request](skills/http-request.yaml) | Call external REST APIs over HTTPS |
| [Image Analysis](skills/image-analysis.yaml) | Describe images, detect objects, and extract text via OCR |
| [Text Summarization](skills/text-summarization.yaml) | Condense long documents into concise summaries |

See [`skills/README.md`](skills/README.md) for the full schema reference and
instructions on adding new skills.

## Using This Template

1. Click **"Use this template"** on GitHub to create a new repository from this one.
2. Add or remove skill YAML files in the `skills/` directory to match your project's needs.
3. Register the skills with your Oracle Generative AI Agent endpoint or compatible framework.
4. Extend each skill's YAML with environment-specific configuration (connection IDs, API keys
   stored as secrets, etc.) as required by your deployment.

## Oracle Agent Skills Format

Skills are defined using a YAML schema with the following top-level fields:

```yaml
schema_version: "1.0"
kind: Skill
metadata:
  name: skill-name          # unique kebab-case identifier
  version: "1.0.0"          # Semantic Versioning
  description: "…"
  tags: []
spec:
  display_name: "…"
  description: |
    Detailed description visible in agent UIs.
  parameters:               # JSON Schema for inputs
    type: object
    properties: {}
    required: []
  returns:                  # JSON Schema for outputs
    type: object
    properties: {}
```

The `parameters` and `returns` schemas are JSON Schema (draft-07) compatible,
making skills interoperable with OpenAPI 3.x tool definitions and the
function-calling interfaces of major LLM providers.

## License

This project is licensed under the [BSD 2-Clause License](LICENSE).
