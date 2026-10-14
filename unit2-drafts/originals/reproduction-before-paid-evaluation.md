# Unit 2 — Claim and Reproduce

Path: `beat-1-sandbox/unit-2/reproduction.md`

> DRAFT — not ready to submit. Prepared with Codex assistance at the user's request. No paid evaluation or live Claude skill grading has run; no comments have been posted. The local bug reproduction below is preparation evidence, not the required harness evaluation. Review the drafts, perform the remaining graded workflow, and replace the pending fields before submission.

## Your identity upstream

**GitHub username**

jonnypan2325

## Posted upstream

**Claim comment**

PENDING — no comment permalink exists. The following is an unposted draft; replace this status with the actual permalink and verify that the pasted text matches what was posted.

I'm investigating the `FaithfulnessChecker.check()` crash on a context chunk with `text: None`. I've done a local preparation run; next I'll verify the issue snippet and `test_none_context_chunk_text` from my fork, compare the missing-key case, and post the environment, commands, and results before proposing a change.

This work is AI-assisted, including drafting and local command execution.

**Reproduction comment**

PENDING — no comment permalink exists. The following is an unposted draft of the local preparation report. After posting the checked claim, verify from the fork, update this draft to match the confirmation evidence, run the live skill check, and replace this status with the actual permalink and exact posted text.

The local preparation run reproduced the reported `TypeError` on unchanged commit `2f4e82f52efbcfcc57d65b3fa5348672163ca088`.

**Environment:** macOS 26.6.2 (arm64), Python 3.11.16, structlog 26.1.0, pytest 9.1.1. Recorded September 29, 2026, at 22:10 PDT.

**Reproduce from a fresh checkout:**

```bash
git clone https://github.com/codepath/pathreview-ai301-fa26-s3.git
cd pathreview-ai301-fa26-s3
git checkout 2f4e82f52efbcfcc57d65b3fa5348672163ca088
python3.11 -m venv .venv
.venv/bin/python -m pip install 'structlog==26.1.0' 'pytest==9.1.1'
.venv/bin/python -c "from rag.evaluator.faithfulness_checker import FaithfulnessChecker; FaithfulnessChecker().check('Knows Python.', [{'text': None}])"
```

**Expected / acceptance criterion:** Handle a `text: None` chunk without raising and return a float in `[0, 1]`, as asserted by the existing `test_none_context_chunk_text`.

**Observed:** The issue's exact snippet exits with status 1. Relevant traceback:

```text
  File "/Users/jonathanpan/dev/codepath/pathreview-ai301-fa26-s3/rag/evaluator/faithfulness_checker.py", line 38, in check
    context_text = " ".join([chunk.get("text", "") for chunk in context_chunks])
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: sequence item 0: expected str instance, NoneType found
```

**Checks run:**

```bash
# Control: missing text key
.venv/bin/python -c "from rag.evaluator.faithfulness_checker import FaithfulnessChecker; print('score =', FaithfulnessChecker().check('Knows Python.', [{'content': 'Python skills'}]))"
# Control: string text
.venv/bin/python -c "from rag.evaluator.faithfulness_checker import FaithfulnessChecker; print('score =', FaithfulnessChecker().check('Knows Python.', [{'text': 'Python skills'}]))"
# Existing issue test: normal marker, then bypass it to expose the failure
.venv/bin/python -m pytest tests/unit/test_faithfulness_checker.py -v -m unit -k test_none_context_chunk_text -rx
.venv/bin/python -m pytest tests/unit/test_faithfulness_checker.py -v -m unit -k test_none_context_chunk_text --runxfail
# Existing missing-key test and the complete evaluator test file
.venv/bin/python -m pytest tests/unit/test_faithfulness_checker.py -v -m unit -k test_missing_text_key_in_chunk
.venv/bin/python -m pytest tests/unit/test_faithfulness_checker.py -q -m unit
```

| Check | Recorded result |
|---|---|
| Missing-key snippet | `score = 0.0`, exit 0 |
| String-text snippet | `score = 0.0`, exit 0 |
| Named issue test | `21 deselected, 1 xfailed`, exit 0 |
| Named issue test with `--runxfail` | `1 failed, 21 deselected`, same `TypeError`, exit 1 |
| Existing missing-key test | `1 passed, 21 deselected`, exit 0 |
| Complete evaluator test file | `18 passed, 4 xfailed`, exit 0 |

**Dev notes / scope:** `.get("text", "")` supplies the default for an absent key, but a present `None` reaches the string join. The controls distinguish those inputs. XFAIL is the existing expected-failure marker, not a successful fix. No application code or test markers were changed. The other three XFAILs in this file refer to issue #59 and are outside this report.

The setup is intentionally the isolated evaluator portion of the repository's Python environment: its declared `structlog` dependency and `pytest` dev dependency. The module imports only `re` and `structlog`, and its test fixtures do not require services. The full `make setup` sequence, database/migrations, API, frontend/Jest, integration tests, lint and type checks were not run. This is a nonvisual Python failure, so terminal evidence is used instead of screenshots/video.

**AI assistance:** Codex drafted this report and executed the recorded commands on my local machine. This reports that preparation run, not a claim that I independently executed or reviewed every command.

## Eval iterations

**Run history**

PENDING — zero paid harness runs have been performed, per the user's instruction. There is no measured agreement score or final run to cite. The existing `eval-run.txt` remains the course placeholder. Record the real agreement lines in chronological order after authorized runs; the last must match the harness-generated final file.

**Package analysis**

PREPARATION ONLY — package `pkg-01` (HTTPie) has instructor gold label `accept`. No actual harness verdict for this rubric exists yet. Manual review predicts accept: the report records HTTPie 3.2.4, Python 3.12.4, multidict 6.6.0 and macOS 14.5, supplies offline commands, shows the missing Content-Type for one custom header, and supplies a no-header control with Content-Type present. The claim identifies the behavior and a bounded next investigation. Replace the predicted result with the actual final-run verdict and explain any discrepancy before submission.

**Check rationale**

Current check, quoted exactly from the drafted `tools/repro-check/rubric.md`:

```text
| target-behavior | The issue's input and failure signature compared with the candidate report's actual input, command and artifact, not just the candidate's diagnosis; Behavior shown in the evidence guide. | For a reproduced result, the evidence demonstrates the same relevant behavior as the issue, not merely some error in the same tool. If an exit code or exception distinguishes the failure, it must agree with the claimed target. For a cannot-reproduce result, the report shows a faithful attempt at the trigger, the observed non-failure or different outcome, and limits the conclusion accordingly. Fail when a syntax/configuration/setup error, unrelated exception, or different input is called confirmation of the target bug. A transparent failed setup may explain a blocker but is not yet a completed reproduction attempt. | required |
```

This check compares the actual trigger and artifact against the issue so that an adjacent error cannot be called confirmation. During manual preparation, calibration package `calib-03` illustrated why this matters: the candidate's input uses a colon instead of an equals sign, and the output is an HCL syntax error rather than the reported panic. The rule also permits an honest, evidenced cannot-reproduce outcome, so it does not reward forcing every attempt to reproduce a bug. This rationale describes Codex-assisted drafting and manual inspection, not a paid eval iteration or classroom rubric swap.

**Trade-offs**

The target-behavior check may hold an honest setup-blocker report until the attempt actually reaches the relevant trigger. That is useful triage information, but it is not yet a complete reproduction package. Conversely, an explicitly explained version/platform difference can be acceptable when the report limits its conclusion to the tested environment; identical environments and successful reproduction are not mandatory. Manual review of `pkg-01` also prompted a conventions clarification so a reproduction comment is not rejected merely for omitting a new-issue duplicate-search checkbox. No canary or full harness run has verified the effects of these choices. Confirm them with actual results before treating this draft as the final evaluation account.

---

Related paths: `eval-run.txt` in this directory; skill files in `tools/repro-check/`. Preparation instructions, raw terminal evidence and the rerun helper are in `/Users/jonathanpan/dev/codepath/unit2-drafts/` and are not a substitute for the graded artifacts above.
