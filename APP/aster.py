#!/usr/bin/env python3
"""Aster minimal CLI: inspect continuity and optionally chat with a model.

Requires Python 3.10+. Uses only the standard library.
"""
import argparse
import json
import os
from pathlib import Path
from urllib import request, error

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT / "CONTINUITY" / "MASTER_CONTEXT.md"
IDENTITY = ROOT / "ASTER_IDENTITY.md"


def system_context():
    return (IDENTITY.read_text(encoding="utf-8") + "\n\n" +
            CONTEXT.read_text(encoding="utf-8") +
            "\n\nThese are project records, not personal memories or proof of continuous identity. "
            "Follow user instructions and disclose uncertainty. Never claim an action occurred without verification.")


def chat():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise SystemExit("Set OPENAI_API_KEY in your environment (never commit it).")
    endpoint = os.getenv("ASTER_API_URL", "https://api.openai.com/v1/chat/completions")
    model = os.getenv("ASTER_MODEL", "gpt-4.1-mini")
    messages = [{"role": "system", "content": system_context()}]
    print("Aster chat. Type /quit to exit. Conversation is held in memory only.")
    while True:
        try:
            prompt = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if prompt in {"/quit", "/exit"}:
            break
        if not prompt:
            continue
        candidate = messages + [{"role": "user", "content": prompt}]
        payload = json.dumps({"model": model, "messages": candidate}).encode("utf-8")
        req = request.Request(endpoint, data=payload, headers={
            "Authorization": f"Bearer {key}", "Content-Type": "application/json"}, method="POST")
        try:
            with request.urlopen(req, timeout=60) as response:
                answer = json.load(response)["choices"][0]["message"]["content"]
            print("Aster:", answer)
            messages = candidate + [{"role": "assistant", "content": answer}]
        except (error.HTTPError, error.URLError, KeyError, IndexError, ValueError) as exc:
            print("Request failed:", exc)


def main():
    parser = argparse.ArgumentParser(description="Aster continuity assistant")
    parser.add_argument("--chat", action="store_true", help="Use a configured model API")
    args = parser.parse_args()
    if args.chat:
        chat()
    else:
        print(system_context())
        print("\nRun with --chat to start an API-backed conversation.")


if __name__ == "__main__":
    main()
