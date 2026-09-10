from __future__ import annotations
import argparse
from .service import RequestRouter

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="repo-demo")
    subparsers = parser.add_subparsers(dest="command", required=True)
    classify_parser = subparsers.add_parser("classify", help="classify a user request")
    classify_parser.add_argument("text")
    return parser

def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "classify":
        print(RequestRouter().route(args.text))
        return 0
    return 1
