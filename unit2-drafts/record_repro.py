"""Record issue #60 and controls without changing application code.

Run with the repository's .venv Python after installing structlog and pytest.
Only the single evaluator test file is exercised; no services or model calls.
"""
import argparse
from datetime import datetime, timezone
import importlib.metadata
from pathlib import Path
import platform
import shlex
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--phase', choices=['preparation', 'confirmation'], default='preparation')
    args = parser.parse_args()
    repo = args.repo.resolve()
    py = str(repo / '.venv/bin/python')
    chunks = [
        'Issue #60: local ' + args.phase + ' run (not a paid skill evaluation)',
        'Recorded with the reproduction helper; see the work log for operator and claim-posting chronology.',
        'UTC: ' + datetime.now(timezone.utc).isoformat(),
        'Platform: ' + platform.platform(),
        'Python: ' + sys.version.replace('\n', ' '),
        'structlog: ' + importlib.metadata.version('structlog'),
        'pytest: ' + importlib.metadata.version('pytest'),
        'Repo: ' + str(repo),
    ]

    test = 'tests/unit/test_faithfulness_checker.py'
    commands = [
        ('Repository revision', ['git', 'rev-parse', 'HEAD'], 0),
        ('Repository working tree', ['git', 'status', '--short'], 0),
        ('Exact issue snippet', [py, '-c', "from rag.evaluator.faithfulness_checker import FaithfulnessChecker; FaithfulnessChecker().check('Knows Python.', [{'text': None}])"], 1),
        ('Missing-key control', [py, '-c', "from rag.evaluator.faithfulness_checker import FaithfulnessChecker; print('score =', FaithfulnessChecker().check('Knows Python.', [{'content': 'Python skills'}]))"], 0),
        ('String-text control', [py, '-c', "from rag.evaluator.faithfulness_checker import FaithfulnessChecker; print('score =', FaithfulnessChecker().check('Knows Python.', [{'text': 'Python skills'}]))"], 0),
        ('Named issue test, existing XFAIL marker retained', [py, '-m', 'pytest', test, '-v', '-m', 'unit', '-k', 'test_none_context_chunk_text', '-rx'], 0),
        ('Named issue test, expose actual failure', [py, '-m', 'pytest', test, '-v', '-m', 'unit', '-k', 'test_none_context_chunk_text', '--runxfail'], 1),
        ('Existing missing-key control test', [py, '-m', 'pytest', test, '-v', '-m', 'unit', '-k', 'test_missing_text_key_in_chunk'], 0),
        ('Evaluator test file, normal markers', [py, '-m', 'pytest', test, '-q', '-m', 'unit'], 0),
        ('Final working tree', ['git', 'status', '--short'], 0),
    ]
    results = []
    for label, command, expected in commands:
        result = subprocess.run(command, cwd=repo, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
        chunks.extend(['', '## ' + label, '$ ' + shlex.join(command), result.stdout.rstrip(), 'Exit status: ' + str(result.returncode)])
        results.append((label, result.returncode, expected))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text('\n'.join(chunks) + '\n')
    print(args.output.read_text())
    if any(actual != expected for _, actual, expected in results):
        print('One or more outcomes differed from the planned expectations; review the recorded results.', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
