# Optional assistant integrations

These examples are inert here. Choose an integration only if you want its
workflow, inspect it, and merge the relevant entry into your existing assistant
configuration. Preserve unrelated settings. Installing the narrative skill does
not require any MCP server.

The examples pin `@codemcp/workflows` to the bundled skill's version (5.3.0).
Verify package availability and your assistant's configuration format before
installing; upgrade the package and skill together deliberately.

- `.mcp.json`: Claude Code server example.
- `.vscode/mcp.json`: VS Code server example.
- `opencode.json`: OpenCode server example.
- `.claude/skills/`, `.github/skills/`, `.opencode/skills/`: optional workflow skill
  adapters for the corresponding assistants.

The workflow skills retain their upstream attribution and MIT metadata. They are
not active defaults for this collection or for narrative adoption.
