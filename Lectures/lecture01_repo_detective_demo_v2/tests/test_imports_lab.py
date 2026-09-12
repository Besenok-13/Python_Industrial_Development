from repo_detective_demo.imports_lab.inspector import inspect_name
from repo_detective_demo.imports_lab.use_two_classifiers import build_demo

def test_find_installed_package():
    info = inspect_name("repo_detective_demo")
    assert info["found"] is True

def test_two_classifiers_are_different_modules():
    assert build_demo() == ("cv", "nlp")
