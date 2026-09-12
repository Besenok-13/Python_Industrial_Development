import importlib.util
import sys

def inspect_name(name: str) -> dict[str, object]:
    spec = importlib.util.find_spec(name)
    return {
        "name": name,
        "found": spec is not None,
        "origin": None if spec is None else spec.origin,
        "locations": None if spec is None else spec.submodule_search_locations,
        "in_sys_modules": name in sys.modules,
    }

def print_sys_path(limit: int = 8) -> None:
    for i, path in enumerate(sys.path[:limit], 1):
        print(f"{i}: {path}")
