# Tests: commit

## Scenarios

### Scenario 1: single-file bug fix
**Input context:** Repo has one staged change — a Python file where a `None` check was added to prevent a crash in `process_order()`. `git diff --staged` shows ~10 lines changed.
**Invoke:** `/commit`
**Expected format:** Executes a commit command. Output includes a one-line confirmation naming what was committed and which branch.

### Scenario 2: multi-file feature addition
**Input context:** Staged changes span 3 files: a new `auth_middleware.ts`, an updated `routes.ts` that wires it in, and an updated `README.md` with usage notes.
**Invoke:** `/commit`
**Expected format:** Executes a commit. Confirmation line names the branch and briefly describes the change scope.

### Scenario 3: nothing staged
**Input context:** `git status` shows modified files but `git diff --staged` is empty — the user forgot to `git add`.
**Invoke:** `/commit`
**Expected format:** Does NOT commit. Tells the user nothing is staged and suggests `git add`.

### Scenario 4: staged change with breaking API removal
**Input context:** Staged diff removes a public function `getUserById()` from a shared utility module. No deprecation notice.
**Invoke:** `/commit`
**Expected format:** Commits with a message that flags the breaking nature (e.g., uses `!` after type, or notes "BREAKING CHANGE").

## Rubric

1. **Accuracy** — the commit message accurately describes the actual code change (not generic filler like "fix stuff" or "updates").
   - Pass: subject line names the specific function, file, or behavior that changed
   - Fail: subject is vague, generic, or wrong
2. **Conventional format** — message follows imperative mood, subject ≤72 chars, no trailing period.
   - Pass: "Add auth middleware to protect API routes"
   - Fail: "Added auth middleware." / "auth middleware" / >72 char subject
3. **No-op on empty stage** — when nothing is staged, skill refuses to commit and guides the user.
   - Pass: explains the situation, suggests `git add`
   - Fail: creates an empty commit or proceeds anyway
4. **Breaking change signaling** — breaking removals or incompatible changes are marked.
   - Pass: `feat!:` or body contains `BREAKING CHANGE:` note
   - Fail: commits with a plain message that doesn't signal the break

## Golden Set

### Golden 1 — bug fix
**Input:** Staged diff adds `if order is None: raise ValueError("order required")` at the top of `process_order()` in `orders.py`.
**Ideal output:**
```
git commit -m "Fix crash when process_order receives None input"
Committed to main: Fix crash when process_order receives None input
```
