from datetime import date, datetime, timedelta, timezone

class DateTimeUtils:
    
    @staticmethod
    def utc_now_iso() -> str:
        return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    
    @staticmethod
    def utc_to_timestamp(utc_str: str) -> float:
        dt = datetime.fromisoformat(utc_str.replace("Z", "+00:00"))
        return dt.timestamp()

    @staticmethod
    def is_before_tomorrow(d: date) -> bool:
        tomorrow = date.today() + timedelta(days=1)
        return d < tomorrow