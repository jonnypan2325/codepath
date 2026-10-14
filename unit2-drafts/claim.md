I'm investigating the crash in `FaithfulnessChecker.check()` when a context chunk contains `text: None`.

I've already completed a local preparation run. Next, I'll do the following:

1. Verify the issue's reproduction snippet and `test_none_context_chunk_text` from my fork.
2. Compare the behavior when the `text` key is missing.
3. Post my environment, commands, and results before proposing a change.
