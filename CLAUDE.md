# CLAUDE.md — Skills Repository

This repository stores Claude Code skills — reusable prompt-based capabilities invoked via slash commands (e.g., `/commit`, `/grill`). Skills live in `skills/<skill-name>/SKILL.md`. For a list of available skills, see README.md.

## Skill Loading Tiers

- **Tier 1** (always in context): the `description` field from each `SKILL.md` frontmatter (~20 tokens/skill)
- **Tier 2** (loaded when relevant): the full `SKILL.md` body, triggered by matching the description
- **Tier 3** (loaded on demand): support files inside the skill folder, only when `SKILL.md` explicitly instructs Claude to load them

Write descriptions precisely — they are the relevance signal that determines when a skill fires.

## Naming Conventions

| Convention | Rule |
|---|---|
| Skill folder name | lowercase, hyphens only (e.g., `review-pr`) |
| Slash command | matches folder name exactly |
| `name` in frontmatter | must match folder name exactly |
| Tags | use category tags: `git`, `review`, `quality`, `docs`, `special` |

## Adding a New Skill

1. Create `skills/<skill-name>/SKILL.md` using the template in `skills/commit/SKILL.md` as reference
2. Add an entry to README.md
3. Commit: `add <skill-name> skill`

## Key Conventions for AI Assistants

- Do not create new skill files unless explicitly requested
- Prefer editing existing skill files over creating new ones
- Never rename a skill folder without updating README.md and all cross-references
- Skills with support files must explicitly instruct Claude to load them — Tier 3 is not automatic
- If a skill's purpose is unclear, read its SKILL.md before invoking or editing it

## Git Practices

- Branch format: `claude/<description>-<id>`
- Push: `git push -u origin <branch-name>`
- Never force-push, never skip hooks (`--no-verify`)
- Keep commits atomic: one logical change per commit
