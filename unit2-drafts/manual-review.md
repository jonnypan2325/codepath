> Historical preparation notes. The paid evaluation and live checks have since completed; see README.md and evidence/completion-summary.json for current status. The manual predictions below are not the measured results.

# Preparation review — not a harness or live-skill result

Codex reviewed the files without invoking Claude or spending course credit. No master-skill agreement score, fenced live verdict, or completed evaluation is claimed.

## Skill consistency

- Seven required checks cover environment, repeatable steps, observable evidence, behavior matching, honest conclusions, specific communication, and repository/voice conventions.
- The binary verdict rule handles unclear evidence and excludes report-only checks from claim-only live grading.
- Honest cannot-reproduce reports can pass; setup errors presented as the target bug cannot.
- Environment differences can be explicitly explained rather than forcing every valid report onto an identical platform.
- Evidence-guide headings cover all seven checks.
- Voice guide uses the user's stated Python/LLM experience, concise style, actual check results, and appropriate acceptance criteria.
- Scope points to the section repository recorded in Unit 1, not an inferred unrelated repository.

## Manual practice reviews

These are qualitative preparation notes, not Claude/harness outputs or an evaluation score.

| Package | Manual expectation | Evidence |
|---|---|---|
| calib-02 | reject | The Joplin report supplies no tested environment, followable recipe or observable artifact; unsupported broad claims and blame replace evidence. |
| calib-03 | reject | The candidate changes HCL input from `1 = {}` to `1: {}`; its output shows a separator syntax error, not the issue's `panic: not a string`. |
| pkg-01 | accept after the conventions clarification | HTTPie 3.2.4/Python/multidict/OS are named; concrete offline request output shows the missing Content-Type and a control shows it present. The claim is specific and the gold label is accept. No harness verdict exists. |

Manual review of pkg-01 exposed a wording ambiguity: applying every new-issue checkbox to a reproduction comment could reject useful evidence for failing to repeat a duplicate-search acknowledgement. The conventions check and guide now distinguish administrative requirements for opening an issue from requirements applicable to comments. This is a reasoned draft change; no re-run or stability result has been measured.

## Comment-draft review

- Claim names the None input, the existing test, a control and the next verification step, and acknowledges preparation already occurred.
- Repro report identifies the actual environment and exact tested commit; the raw transcript supports the exception, exit codes and test results.
- Report discloses the isolated dependency setup, upstream preparation checkout, skipped checks and AI-operated commands.
- The artifacts have not been graded by the installed repro-check skill. They are drafts, not approved-to-post outputs.

## Workflow gaps deliberately left visible

1. No paid scored run or live skill grading occurred.
2. No GitHub fork, claim, repro comment, commit, push or portal submission was created.
3. The recorded run was local preparation before posting. To preserve the assignment's public sequence, grade/post the claim later, create/clone the fork, then record a confirmation run before posting the report.
4. The write-up's actual skill verdict, run history and comment permalinks remain pending. Do not replace them with these manual notes.
