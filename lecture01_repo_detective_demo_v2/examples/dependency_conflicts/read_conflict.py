import re
import sys
from pathlib import Path

LINE_RE = re.compile(r"^\s*(?P<who>[\w.-]+)\s+(?P<version>[\d.]+)\s+depends on\s+(?P<dep>[\w.-]+)(?P<spec>.*)$")

def parse(text: str) -> list[dict[str, str]]:
    return [m.groupdict() for line in text.splitlines() if (m := LINE_RE.match(line))]

def main(path: str) -> int:
    rows = parse(Path(path).read_text(encoding="utf-8"))
    print("| Кто требует | Версия | Конфликтующий пакет | Ограничение |")
    print("|---|---:|---|---|")
    for row in rows:
        print(f"| {row['who']} | {row['version']} | {row['dep']} | {row['spec'].strip()} |")
    deps = {row["dep"] for row in rows}
    if len(deps) == 1:
        print(f"\nConflict center: {next(iter(deps))}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
