# Unit 2 work log

## Preparation

- Initially the user authorized local preparation only, without paid runs or publication. The later authorization below supersedes the paid-run restriction.
- Verified Claude Code is authenticated to the CodePath Student account outside the sandbox.
- Read the original issue #60 and repository contribution/setup entry points.
- No claim by jonnypan2325 was present in the issue comments at inspection time.
- No jonnypan2325/pathreview-ai301-fa26-s3 fork existed at inspection time.
- Initial rubric and evidence guide drafted from the course proof families before running any scored evaluation.
- Manually inspected calibration packages calib-02 and calib-03: the first lacks evidence/environment and uses unhelpful communication; the second changes HCL input from equals to colon and mistakes a syntax error for the reported panic. Both should be rejected by the draft rubric. This was preparation performed by Codex, not a claimed classroom rubric swap.

## Paid evaluation history

At the end of the initial unpaid preparation phase, no evaluation runs had occurred. See the later paid evaluation history below.

## Drafting and local verification

- User supplied extensive Python and LLM workflow experience from two internships and personal backend projects, and a preference for concise comments with concrete tests, replication, design notes and acceptance criteria. The voice guide reflects that input rather than invented experience.
- Cloned the public section repository locally at `2f4e82f52efbcfcc57d65b3fa5348672163ca088`. No GitHub fork was created.
- Read README, docs/CONTRIBUTING.md, docs/SETUP.md, Makefile, pyproject.toml, PR template, evaluator source, named tests and fixtures. No AGENTS.md or CLAUDE.md was found in the checkout.
- Created an isolated Python 3.11.16 environment with structlog 26.1.0 and pytest 9.1.1 from the declared dependency families. Did not run the full app/DB/frontend setup; the report explicitly describes this limitation.
- On September 29, 2026 at 22:10 PDT, Codex executed the exact issue snippet, controls, named test with/without the XFAIL marker, and the evaluator file. The raw transcript is preserved in evidence/repro-log.txt. No code changes were made.
- Results: exact TypeError and exit 1; both snippet controls returned 0.0 and exit 0; named test XFAIL normally and FAIL with --runxfail; missing-key test passed; evaluator file 18 passed / 4 xfailed.
- This took place before any public claim, as local preparation. Drafts acknowledge it. The handoff requires a checked/posted claim followed by a confirmation run from the fork before the final report is posted.
- Read scored package pkg-01 and the instructor gold-label file manually. No harness verdict exists. Clarified the conventions rule so new-issue administrative checkboxes are not automatically imposed on reproduction comments; recorded the unmeasured trade-off in the draft write-up.
- Preserved the official eval-run.txt placeholder; it must not be replaced with local Python test output or an invented grading score.


## Authorized evaluation and final draft grading

- User then authorized Claude runs, including approximately $1–2 of small-scale command checks before a full run, while continuing to withhold public comments/publication.
- Preflight checked the original harness, all selected package paths, rubric/evidence content and authentication. No harness code or gold labels were changed.
- First smoke run: six scored packages, 5/6 agreement. The sole disagreement was pkg-20: the grader inferred "no AI use is claimed, so no disclosure is owed."
- Revision: explicitly stated the course's AI-assisted-candidate premise and required the disclosure details requested by the captured repository policy. Kept permissive/no-disclosure policies distinct. Saved the pre-revision files in evidence/skill-before-disclosure-revision/.
- Second targeted run: pkg-05, pkg-07 and pkg-20, 3/3 agreement. Both positive policy cases remained accepts; missing disclosure became a rejection. Nine preliminary package calls total, approximately $1.80 using the course's estimate.
- Full confirming run: 20/20, all five categories matched, no execution errors. The original harness wrote the official eval-run.txt; its three fingerprints were verified against the installed files. Estimated full-run cost using the course guidance: $4.
- Read-only Sonnet live checks of the claim-only draft and full package each returned accept. Each was capped at $1, with no permission denials, posting or file edits. Prompts, full JSON responses, per-check text and parsed verdicts are saved in evidence/.
- Shortened the user's absolute filesystem prefix in the public-facing draft traceback before live grading; the unmodified raw local reproduction transcript is preserved.
- Synchronized the final installed and coursework skill files. Completed the evaluation write-up from the actual saved results, including the revised convention check quoted exactly.
- No claim/reproduction comment, fork, commit, push or portal submission was made. The local reproduction remains pre-publication preparation; the handoff retains the required claim-then-fork-confirmation sequence.


## Posted claim and fork confirmation

- User supplied https://github.com/codepath/pathreview-ai301-fa26-s3/issues/60#issuecomment-5905217025. GitHub verifies jonnypan2325 posted it at 2026-09-30T06:08:35Z.
- Saved the exact public comment in claim.md and the coursework field, preserving the user's numbered formatting and choice to omit disclosure for this comment only. The previously accepted version (which included disclosure) remains in evidence/claim-graded-01.md; its earlier check is not misrepresented as a pre-post check of the changed wording.
- Created https://github.com/jonnypan2325/pathreview-ai301-fa26-s3 and cloned it locally to /Users/jonathanpan/dev/codepath/pathreview-ai301-fa26-s3-fork. Tested unchanged commit 2f4e82f52efbcfcc57d65b3fa5348672163ca088.
- Codex ran the recorded fork confirmation at 2026-09-30T06:10:56.898455+00:00, after the claim timestamp. The exact TypeError, two successful control snippets, XFAIL/forced-FAIL issue test, passing missing-key test and 18 passed / 4 xfailed file result all matched preparation. No application code or markers changed.
- Updated the report's opening, fork URL and timestamp. Retained disclosure of AI-operated confirmation and preserved the earlier report in evidence/repro-graded-01.md.
- Full live check 02 graded the exact posted claim and the updated report: accept, no permission denials. CLI-reported model cost: $0.18645460000000003. No repeat of the already-passing 20-package evaluation was necessary because the skill files are unchanged.
- Reproduction comment, coursework commit/push and portal submission remain withheld.


## Reproduction comment posted by user

- Verified https://github.com/codepath/pathreview-ai301-fa26-s3/issues/60#issuecomment-5905342853 at 2026-09-30T06:18:15Z. Copied the exact posted text into the course write-up.
- Only the final AI-assistance sentence differs from the accepted full-live-02 draft: it now states personal command execution/verification. Asked the user to confirm their independent rerun; the evidence on hand records Codex execution. Preserved the previously graded version and did not overwrite historical verdicts.
- No commit, push or portal submission performed.


## Personal verification confirmed

- User explicitly confirmed they personally reran and verified the commands before posting. The final public attribution is consistent with this confirmation; no comment correction is needed.
- Both posted-comment links and exact text are recorded. Coursework is ready for review, commit/push and portal submission when authorized. No additional model call or external mutation was performed.
