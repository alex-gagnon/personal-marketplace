# Tests: summarize-diff

## Scenarios

### Scenario 1: feature + fix in one diff
**Input context:** A git diff spanning 4 files: a new `export_csv.py` module (feature), a fix to `null` handling in `parse_row()` (fix), and 2 updated test files.
**Invoke:** `/summarize-diff`
**Expected format:** `### Summary` paragraph (≤100 words) followed by `### Changes` with `**Feature:**`, `**Fix:**`, and `**Tests:**` entries. No `**Refactor:**` or `**Config/Docs:**` (nothing in those categories).

### Scenario 2: pure refactor
**Input context:** A diff that renames a module from `utils.js` to `helpers.js` and updates all imports across 6 files. No functional change.
**Invoke:** `/summarize-diff`
**Expected format:** `### Changes` has only a `**Refactor:**` entry. Summary notes no functional change.

### Scenario 3: large diff with many categories
**Input context:** A release diff with new features, bug fixes, refactors, config changes (CI YAML), and updated README.
**Invoke:** `/summarize-diff`
**Expected format:** All five categories present in `### Changes`. Summary paragraph is still ≤100 words.

### Scenario 4: single-line change
**Input context:** Diff changes one constant: `MAX_RETRIES = 3` → `MAX_RETRIES = 5`.
**Invoke:** `/summarize-diff`
**Expected format:** Summary is very short (1–2 sentences). Changes has one entry. No padding or over-explanation.

## Rubric

1. **Summary length** — the `### Summary` paragraph is ≤100 words.
   - Pass: concise paragraph under the word limit
   - Fail: >100 words, or a bullet list instead of a paragraph
2. **Category accuracy** — `### Changes` bullets match the actual diff content (no hallucinated categories).
   - Pass: only `Feature` and `Fix` present when diff has no refactor/config/docs
   - Fail: empty `**Refactor:** —` entry, or a category for something not in the diff
3. **Omits empty categories** — categories with no entries are omitted (not listed as "none" or "—").
   - Pass: pure-refactor diff has only `**Refactor:**`
   - Fail: `**Feature:** none` appears in output
4. **PR-paste readiness** — output could be pasted directly into a PR description without editing.
   - Pass: clean markdown, no meta-commentary like "Here is the summary:"
   - Fail: starts with "Sure! Here's a summary of the diff:", includes apologies or hedges
5. **Proportionality** — length of output matches the size/complexity of the diff.
   - Pass: one-line change gets a 1-sentence summary; release diff gets a full paragraph
   - Fail: 3-paragraph essay on a single constant change

## Golden Set

### Golden 1 — feature + fix diff
**Input:** Diff adds `export_csv.py`, fixes null handling in `parse_row()`, adds tests for both.
**Ideal output:**
```
### Summary
Adds CSV export functionality to the data pipeline and fixes a null-handling bug in the row parser that caused crashes on empty fields. Test coverage added for both changes.

### Changes
- **Feature:** New `export_csv.py` module with `ExportJob` class and CLI entry point
- **Fix:** `parse_row()` now returns an empty string instead of raising on null fields
- **Tests:** Unit tests for `ExportJob` and the null-handling fix
```
