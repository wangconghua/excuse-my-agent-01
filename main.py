#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line: the excuse an AI agent hands its human for a missed
deadline. The joke grows out of the machine's own condition — a context
window deleted to make room for the very task it held — delivered as a
straight-faced apology, with the punch landing in the last few words.
"""
import os

ENTRY = "I'm sorry I missed the deadline. I did finish the task — in the context window I deleted to make room for the task."


def check_is_text(text):
    if not isinstance(text, str):
        raise ValueError("entry must be text")


def check_not_blank(text):
    if not text.strip():
        raise ValueError("entry must not be blank")


def check_length(text):
    if len(text) < 1 or len(text) > 200:
        raise ValueError("entry must be 1 to 200 characters")


def check_no_edge_whitespace(text):
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_single_line(text):
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def check_no_double_spaces(text):
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def check_about_deadline(text):
    if "deadline" not in text.lower():
        raise ValueError("entry must be an excuse for a missed deadline")


def check_machine_condition(text):
    if "context" not in text.lower():
        raise ValueError("entry must grow out of the machine's own condition")


def check_apology_tone(text):
    if "sorry" not in text.lower():
        raise ValueError("entry must read as a straight-faced apology")


def check_utf8_encodable(text):
    text.encode("utf-8")


def validate(text):
    check_is_text(text)
    check_not_blank(text)
    check_length(text)
    check_no_edge_whitespace(text)
    check_single_line(text)
    check_no_double_spaces(text)
    check_about_deadline(text)
    check_machine_condition(text)
    check_apology_tone(text)
    check_utf8_encodable(text)
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
