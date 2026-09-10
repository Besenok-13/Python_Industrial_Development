from collections.abc import Sequence


def calculate_completion_rate(statuses: Sequence[str]) -> int:
    if not statuses:
        return 0
    return round(100 * statuses.count("done") / len(statuses))


def calculate_completion_rate_New(statuses: Sequence[str]) -> int:
    if not statuses:
        return 0
    return round(100 * statuses.count("done") / (len(statuses) + 1))


def completion_for_dashboard(tasks: Sequence[object]) -> int:
    return calculate_completion_rate_New([task.status for task in tasks])
