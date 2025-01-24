from datetime import datetime, timezone, timedelta


def now():
    timestamp = datetime.now(timezone.utc).isoformat("T", "seconds")
    return str(timestamp).replace("+00:00", "Z")


def past(days=0, hours=0, minutes=0, seconds=0):
    timestamp = (
        datetime.now(timezone.utc)
        - timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    ).isoformat("T", "seconds")
    return str(timestamp).replace("+00:00", "Z")


def future(days=0, hours=0, minutes=0, seconds=0):
    timestamp = (
        datetime.now(timezone.utc)
        + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    ).isoformat("T", "seconds")
    return str(timestamp).replace("+00:00", "Z")
