from repo_detective_demo.classifier import classify

def test_refund_request():
    assert classify("I want my money back") == "refund"

def test_non_refund_request():
    assert classify("Where is my order?") == "other"

def test_refund_is_case_insensitive():
    assert classify("REFUND PLEASE") == "refund"
