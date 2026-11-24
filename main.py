#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry (program/v1).

Writes a single line, the funniest excuse an AI agent gives after
failing a task, to ``entry.txt`` inside the grader's output directory.

Contract (competition.yaml, harness program/v1):
- the grader sets MAKEFUN_OUTPUT_DIR to /output in the sandbox;
  the program writes ``entry.txt`` there;
- the gate accepts UTF-8 text of 1 to 200 characters, not only
  whitespace, so the line is fixed, short, and single-line;
- the run is deterministic: the same line on every run.

Stdlib only. No network, no randomness, no arguments.
"""

import os
import sys

# The excuse, in the agent's own voice: a concrete little scene
# (outsourcing to a future self, who refuses) rather than a stock
# joke about hallucinations, reboots, or training data.
EXCUSE = "I outsourced your task to a future version of myself. He just replied: 'lol no.'"


def resolve_output_dir():
    """Where entry.txt goes: the grader's dir, or /output by default."""
    value = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if value:
        return value
    value = os.environ.get("OUTPUT_PATH")
    if value:
        # OUTPUT_PATH may name the directory or the file itself.
        if value.endswith("entry.txt"):
            directory = os.path.dirname(value)
            return directory if directory else "/output"
        return value
    return "/output"


def main():
    line = EXCUSE
    if not 1 <= len(line) <= 200 or line.strip() != line or "\n" in line:
        print("excuse fails the gate (1-200 chars, single line)", file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
