# Optional new-project conventions

For a new project, consider `docs/`, a test location appropriate to the language,
and a convenient entrypoint for build and test commands. A Makefile can provide
`all`, `test`, and `clean`; service projects may also benefit from `start`, `stop`,
and `restart`. Pick coverage expectations that fit the project.

These are suggestions to adopt intentionally, not inherited requirements. Choose
the project's license separately. For an existing repository, retain its own
conventions and add only the selected skill.
