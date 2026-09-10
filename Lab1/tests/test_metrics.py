from task_workflow import calculate_completion_rate


def test_calculate_completion_rate_counts_done_tasks() -> None:
    assert calculate_completion_rate(["done", "todo", "done"]) == 67


def test_calculate_completion_rate_handles_empty_list() -> None:
    assert calculate_completion_rate([]) == 0
