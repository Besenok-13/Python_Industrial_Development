"""Run me as `python pkg/tool.py` and as `python -m pkg.tool`."""
from .utils import normalize
print("name:", __name__)
print("package:", __package__)

def main() -> None:
    print(normalize("  Hello Imports  "))

if __name__ == "__main__":
    main()
