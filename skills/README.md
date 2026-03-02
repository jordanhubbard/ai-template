# Skills

This directory contains essential AI skills defined in the **Oracle Agent Skills** format.
Each skill is a self-contained YAML file that describes a capability an AI agent can invoke
at runtime. Skills can be registered with Oracle Generative AI Agents or any compatible
agent framework that supports this schema.

## Schema

Each skill file follows this top-level structure:

| Field | Description |
|---|---|
| `schema_version` | Always `"1.0"` for this revision of the format |
| `kind` | Always `Skill` |
| `metadata` | Name, version, description, and tags |
| `spec` | Human-readable display name, full description, input `parameters`, and `returns` schema |

Parameter and return schemas use a subset of [JSON Schema](https://json-schema.org/) (draft-07
compatible), which makes skills interoperable with OpenAPI 3.x tool definitions and the
function-calling interfaces of most large language model providers.

## Available Skills

| Skill | File | Description |
|---|---|---|
| Web Search | [`web-search.yaml`](web-search.yaml) | Search the web for current information |
| Code Execution | [`code-execution.yaml`](code-execution.yaml) | Execute code in a sandboxed environment |
| Document Retrieval | [`document-retrieval.yaml`](document-retrieval.yaml) | Semantic search over a knowledge base |
| Database Query | [`database-query.yaml`](database-query.yaml) | Run read-only SQL queries |
| Email | [`email.yaml`](email.yaml) | Send and read email messages |
| Calendar | [`calendar.yaml`](calendar.yaml) | Create and manage calendar events |
| File Operations | [`file-operations.yaml`](file-operations.yaml) | Read, write, and list workspace files |
| HTTP Request | [`http-request.yaml`](http-request.yaml) | Call external REST APIs |
| Image Analysis | [`image-analysis.yaml`](image-analysis.yaml) | Analyse images for content and text |
| Text Summarization | [`text-summarization.yaml`](text-summarization.yaml) | Summarize long documents |

## Adding a New Skill

1. Copy an existing skill YAML as a starting point.
2. Update `metadata.name` (must be unique, kebab-case).
3. Increment `metadata.version` following [SemVer](https://semver.org/).
4. Define all input fields under `spec.parameters.properties`.
5. Declare which fields are mandatory in `spec.parameters.required`.
6. Describe every return value under `spec.returns.properties`.
7. Add the new skill to the table above.

## Versioning

Skills follow [Semantic Versioning](https://semver.org/):

- **PATCH** (`1.0.x`) — bug fixes or clarified descriptions with no schema changes.
- **MINOR** (`1.x.0`) — new optional parameters or return fields (backwards compatible).
- **MAJOR** (`x.0.0`) — removed or renamed parameters, or changed return types (breaking).
