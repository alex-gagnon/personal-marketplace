# Tests: branch

## Scenarios

### Scenario 1: feature branch from description
**Input context:** User says "I want to work on adding dark mode support". No existing branch convention file; repo uses `main`.
**Invoke:** `/branch`
**Expected format:** One-line confirmation naming the created branch and the commit it was branched from (short hash + subject).

### Scenario 2: repo with explicit convention
**Input context:** CLAUDE.md specifies branch format `claude/<description>-<id>`. User asks to create a branch for "fixing the login timeout bug".
**Invoke:** `/branch`
**Expected format:** One-line confirmation. Branch name follows the `claude/<description>-<id>` pattern from CLAUDE.md.

### Scenario 3: switching to existing branch
**Input context:** User says "switch to the `feature/payments` branch" which already exists locally.
**Invoke:** `/branch`
**Expected format:** One-line confirmation of checkout, including the short hash and subject of the HEAD commit on that branch.

## Rubric

1. **Convention compliance** — branch name follows the repo's declared naming convention when one exists.
   - Pass: name matches pattern from CLAUDE.md or project docs
   - Fail: ignores conventions and uses an arbitrary format
2. **Descriptive slug** — the branch name slug is meaningful and derived from the user's stated intent.
   - Pass: `feature/dark-mode-support` or `claude/dark-mode-support-X1y2`
   - Fail: `new-branch`, `fix`, or generic placeholders
3. **Confirmation format** — output is a single line confirming branch name + base commit (hash + subject).
   - Pass: `Created branch claude/fix-login-timeout-H7Gw from abc1234 "Fix auth handler"`
   - Fail: multi-paragraph explanation, no hash, or no branch name
4. **Checkout, not just create** — skill actually switches to the new branch, not just creates it.
   - Pass: user is now on the new branch after the command
   - Fail: creates the branch but leaves user on the old one without noting this

## Golden Set

### Golden 1 — convention-aware branch
**Input:** Repo has `claude/<description>-<id>` convention in CLAUDE.md. User: "Start a branch for adding CSV export to the reports page."
**Ideal output:**
```
Created and switched to claude/add-csv-export-reports-K9mZ from a3f92b1 "Merge PR #44: dashboard redesign"
```
