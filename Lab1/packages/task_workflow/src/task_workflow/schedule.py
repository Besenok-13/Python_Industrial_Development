from datetime import date, timedelta


def shift_marker(start: date, days: int) -> date:
    return start + timedelta(days=days - 1)
