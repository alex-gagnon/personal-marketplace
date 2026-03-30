# SDET Marketplace

A marketplace of Claude Code plugins — skills, agents, and MCP servers — for common software development and testing workflows.

## Installation

Add this marketplace to Claude Code:

```bash
/plugin marketplace add https://github.com/alex-gagnon/sdet-marketplace
```

Or for local development:

```bash
/plugin marketplace add ./path/to/sdet-marketplace
```

## Available Plugins

### Skills

| Plugin | Command | Description |
|--------|---------|-------------|
| source-control | `/source-control` | Git workflow — routes to commit, branch, or diff summary based on context. |
| review-pr | `/review-pr` | Reviews a pull request for logic errors, security issues, test coverage, and style. |
| simplify | `/simplify` | Refactors code to reduce complexity and improve readability without changing behavior. |
| add-tests | `/add-tests` | Generates tests covering happy paths, edge cases, and error conditions. |
| document | `/document` | Adds or improves inline documentation, docstrings, and README sections. |
| explain | `/explain` | Explains code or concepts in plain language calibrated to the user's expertise level. |
| grill | `/grill` | Challenges a design using Socratic questioning to surface hidden assumptions. |
| test | `/test` | Runs quality evaluations against plugins using their tests.md fixture files. |

### Agents

| Plugin | Description |
|--------|-------------|
| plugin-architect | Designs and scaffolds new marketplace plugins following official conventions. |

### MCP Servers

_None yet. Use the plugin-architect agent to design one._

## Repository Structure

```
sdet-marketplace/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace catalog (all plugins listed here)
├── plugins/
│   └── <plugin-name>/
│       ├── .claude-plugin/
│       │   └── plugin.json       # Plugin manifest
│       ├── skills/<name>/        # Skill plugins
│       │   ├── SKILL.md
│       │   ├── <support>.md      # Tier 3 support files
│       │   └── tests.md
│       ├── agents/<name>/        # Agent plugins
│       │   ├── AGENT.md
│       │   └── tests.md
│       └── mcps/<name>/          # MCP plugins
│           ├── MCP.md
│           └── tests.md
└── promptfoo.yaml                # CI format assertions
```

## Testing

Each plugin has a `tests.md` with scenarios, rubrics, and golden outputs.

**Semantic quality (LLM-as-judge):**
```
/test                  # evaluate all skills
/test source-control   # evaluate one skill
```

**Format assertions (CI):**
```bash
npx promptfoo eval
npx promptfoo eval --ci
```

## Adding a Plugin

See [CLAUDE.md](./CLAUDE.md) for conventions, or invoke the **plugin-architect** agent to interactively design and scaffold a new plugin.
