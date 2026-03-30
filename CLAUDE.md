# CLAUDE.md — SDET Marketplace

This repository is a marketplace of Claude Code plugins — skills, agents, and MCP servers. The marketplace catalog lives at `.claude-plugin/marketplace.json`. Each plugin is self-contained under `plugins/<name>/` with its own `.claude-plugin/plugin.json`. For the full catalog, see README.md.

## Plugin Types

| Type | Directory | Entrypoint | Description |
|------|-----------|------------|-------------|
| **Skill** | `plugins/<name>/skills/<name>/` | `SKILL.md` | Prompt-based capability invoked via slash command. Stateless, single-turn. |
| **Agent** | `plugins/<name>/agents/<name>/` | `AGENT.md` | Autonomous multi-step workflow that orchestrates tools and sub-tasks. |
| **MCP** | `plugins/<name>/mcps/<name>/` | `MCP.md` | External tool server exposing callable functions over the Model Context Protocol. |

## Plugin Structure

Every plugin lives at `plugins/<name>/` and follows this layout:

```
plugins/<name>/
├── .claude-plugin/
│   └── plugin.json        # Plugin manifest (required)
├── skills/<name>/         # For skill plugins
│   ├── SKILL.md
│   ├── <support>.md       # Tier 3 support files
│   └── tests.md
├── agents/<name>/         # For agent plugins
│   ├── AGENT.md
│   └── tests.md
└── mcps/<name>/           # For MCP plugins
    ├── MCP.md
    └── tests.md
```

The marketplace catalog at `.claude-plugin/marketplace.json` lists all plugins with their `source` paths (relative to repo root).

## Plugin Loading Tiers

- **Tier 1** (always in context): the `description` field from each plugin's frontmatter (~20 tokens/plugin)
- **Tier 2** (loaded when relevant): the full entrypoint body, triggered by matching the description
- **Tier 3** (loaded on demand): support files inside the plugin folder, only when the entrypoint explicitly instructs Claude to load them. Can be used as **sub-skills** — a parent skill detects intent and loads the matching sub-skill file (e.g., `source-control` loads `commit.md`, `branch.md`, or `summarize-diff.md`).

Write descriptions precisely — they are the relevance signal that determines when a plugin fires.

## .claude-plugin/plugin.json Schema

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "One-line description used for Tier 1 matching.",
  "author": { "name": "author-name" },
  "license": "MIT",
  "repository": "https://github.com/alex-gagnon/sdet-marketplace",
  "tags": ["category-tags"]
}
```

## Naming Conventions

| Convention | Rule |
|---|---|
| Plugin folder name | lowercase, hyphens only (e.g., `review-pr`) |
| Slash command (skills) | matches folder name exactly |
| `name` in plugin.json and frontmatter | must match folder name exactly |
| Tags | use category tags: `git`, `review`, `quality`, `docs`, `special`, `design`, `testing` |

## Adding a New Plugin

1. **Check for overlap first** — read `.claude-plugin/marketplace.json` and scan existing plugin descriptions. If a plugin with similar purpose exists:
   - Extend the existing plugin if the new behavior is a variant of the same trigger
   - Merge into the existing plugin if both trigger on nearly identical user intent AND the combined entrypoint body stays under ~400 tokens
   - Only create a new plugin if the purpose, trigger, and output are clearly distinct
2. Create `plugins/<name>/`
3. Create `plugins/<name>/.claude-plugin/plugin.json` with all required fields
4. Create the entrypoint file using existing plugins as templates
5. Create `tests.md` with scenarios, a rubric, and a golden set
6. Add the plugin entry to `.claude-plugin/marketplace.json`
7. Update README.md with the new plugin
8. For skills: add promptfoo assertions to `promptfoo.yaml`
9. Commit: `add <plugin-name> <plugin-type>`

**Tip:** Use the **plugin-architect** agent to interactively design and scaffold new plugins.

## Key Conventions for AI Assistants

- Do not create new plugin files unless explicitly requested
- Before creating a plugin, always check `.claude-plugin/marketplace.json` for overlap
- Prefer editing existing plugins over creating new ones
- When two plugins have nearly identical triggers, merge them rather than maintaining duplicates
- Never rename a plugin folder without updating `.claude-plugin/marketplace.json`, README.md, and all cross-references
- Plugins with support files must explicitly instruct Claude to load them — Tier 3 is not automatic
- If a plugin's purpose is unclear, read its entrypoint before invoking or editing it

## Git Practices

- Branch format: `claude/<description>-<id>`
- Push: `git push -u origin <branch-name>`
- Never force-push, never skip hooks (`--no-verify`)
- Keep commits atomic: one logical change per commit
