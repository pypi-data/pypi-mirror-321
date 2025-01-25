import datetime
from typing import Tuple, Any

_VersionType = Tuple[int, int, int]


def timedelta_in_minutes(version: _VersionType, delta_time: Any) -> Any:
    if isinstance(delta_time, str):
        try:
            hours, minutes, seconds = map(int, delta_time.split(":"))
            delta = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
        except Exception:
            return delta_time
        return integral_number(version, delta.total_seconds() / 60 + 0.5)
    return delta_time


def integral_number(version: _VersionType, number: Any) -> Any:
    if not isinstance(number, int):
        try:
            number = int(number)
        except Exception:
            return number
    return {"number": number, "set": True, "infinite": False}
