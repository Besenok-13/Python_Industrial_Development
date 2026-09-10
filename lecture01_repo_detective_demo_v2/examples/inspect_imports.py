import importlib.util
import sys
for i, path in enumerate(sys.path[:10], 1):
    print(f"{i}: {path}")
for name in ["repo_detective_demo", "repo_detective_demo.classifier", "requests"]:
    spec = importlib.util.find_spec(name)
    print(f"{name}: origin={None if spec is None else spec.origin}")
