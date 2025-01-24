import datetime
from enum import Enum

from plain.utils import timezone


class DatetimeRangeAliases(Enum):
    TODAY = "Today"
    THIS_WEEK = "This Week"
    THIS_WEEK_TO_DATE = "This Week-to-date"
    THIS_MONTH = "This Month"
    THIS_MONTH_TO_DATE = "This Month-to-date"
    THIS_QUARTER = "This Quarter"
    THIS_QUARTER_TO_DATE = "This Quarter-to-date"
    THIS_YEAR = "This Year"
    THIS_YEAR_TO_DATE = "This Year-to-date"
    LAST_WEEK = "Last Week"
    LAST_WEEK_TO_DATE = "Last Week-to-date"
    LAST_MONTH = "Last Month"
    LAST_MONTH_TO_DATE = "Last Month-to-date"
    LAST_QUARTER = "Last Quarter"
    LAST_QUARTER_TO_DATE = "Last Quarter-to-date"
    LAST_YEAR = "Last Year"
    LAST_YEAR_TO_DATE = "Last Year-to-date"
    SINCE_30_DAYS_AGO = "Since 30 Days Ago"
    SINCE_60_DAYS_AGO = "Since 60 Days Ago"
    SINCE_90_DAYS_AGO = "Since 90 Days Ago"
    SINCE_365_DAYS_AGO = "Since 365 Days Ago"
    NEXT_WEEK = "Next Week"
    NEXT_4_WEEKS = "Next 4 Weeks"
    NEXT_MONTH = "Next Month"
    NEXT_QUARTER = "Next Quarter"
    NEXT_YEAR = "Next Year"

    # TODO doesn't include anything less than a day...
    # ex. SINCE_1_HOUR_AGO = "Since 1 Hour Ago"

    @classmethod
    def to_range(cls, value: str) -> (datetime.datetime, datetime.datetime):
        now = timezone.localtime()
        start_of_week = now - datetime.timedelta(days=now.weekday())
        start_of_month = now.replace(day=1)
        start_of_quarter = now.replace(month=((now.month - 1) // 3) * 3 + 1, day=1)
        start_of_year = now.replace(month=1, day=1)

        if value == cls.TODAY:
            return DatetimeRange(now, now)
        if value == cls.THIS_WEEK:
            return DatetimeRange(
                start_of_week, start_of_week + datetime.timedelta(days=6)
            )
        if value == cls.THIS_WEEK_TO_DATE:
            return DatetimeRange(start_of_week, now)
        if value == cls.THIS_MONTH:
            return DatetimeRange(
                start_of_month, start_of_month + datetime.timedelta(days=31)
            )
        if value == cls.THIS_MONTH_TO_DATE:
            return DatetimeRange(start_of_month, now)
        if value == cls.THIS_QUARTER:
            return DatetimeRange(
                start_of_quarter, start_of_quarter + datetime.timedelta(days=90)
            )
        if value == cls.THIS_QUARTER_TO_DATE:
            return DatetimeRange(start_of_quarter, now)
        if value == cls.THIS_YEAR:
            return DatetimeRange(
                start_of_year,
                start_of_year.replace(year=start_of_year.year + 1)
                - datetime.timedelta(days=1),
            )
        if value == cls.THIS_YEAR_TO_DATE:
            return DatetimeRange(start_of_year, now)
        if value == cls.LAST_WEEK:
            return DatetimeRange(
                start_of_week - datetime.timedelta(days=7),
                start_of_week - datetime.timedelta(days=1),
            )
        if value == cls.LAST_WEEK_TO_DATE:
            return DatetimeRange(start_of_week - datetime.timedelta(days=7), now)
        if value == cls.LAST_MONTH:
            last_month = (start_of_month - datetime.timedelta(days=1)).replace(day=1)
            return DatetimeRange(
                last_month, last_month.replace(day=1) + datetime.timedelta(days=31)
            )
        if value == cls.LAST_MONTH_TO_DATE:
            last_month = (start_of_month - datetime.timedelta(days=1)).replace(day=1)
            return DatetimeRange(last_month, now)
        if value == cls.LAST_QUARTER:
            last_quarter = (start_of_quarter - datetime.timedelta(days=1)).replace(
                day=1
            )
            return DatetimeRange(
                last_quarter, last_quarter + datetime.timedelta(days=90)
            )
        if value == cls.LAST_QUARTER_TO_DATE:
            last_quarter = (start_of_quarter - datetime.timedelta(days=1)).replace(
                day=1
            )
            return DatetimeRange(last_quarter, now)
        if value == cls.LAST_YEAR:
            last_year = start_of_year.replace(year=start_of_year.year - 1)
            return DatetimeRange(last_year, start_of_year - datetime.timedelta(days=1))
        if value == cls.LAST_YEAR_TO_DATE:
            last_year = start_of_year.replace(year=start_of_year.year - 1)
            return DatetimeRange(last_year, now)
        if value == cls.SINCE_30_DAYS_AGO:
            return DatetimeRange(now - datetime.timedelta(days=30), now)
        if value == cls.SINCE_60_DAYS_AGO:
            return DatetimeRange(now - datetime.timedelta(days=60), now)
        if value == cls.SINCE_90_DAYS_AGO:
            return DatetimeRange(now - datetime.timedelta(days=90), now)
        if value == cls.SINCE_365_DAYS_AGO:
            return DatetimeRange(now - datetime.timedelta(days=365), now)
        if value == cls.NEXT_WEEK:
            return DatetimeRange(
                start_of_week + datetime.timedelta(days=7),
                start_of_week + datetime.timedelta(days=13),
            )
        if value == cls.NEXT_4_WEEKS:
            return DatetimeRange(now, now + datetime.timedelta(days=28))
        if value == cls.NEXT_MONTH:
            next_month = (start_of_month + datetime.timedelta(days=31)).replace(day=1)
            return DatetimeRange(next_month, next_month + datetime.timedelta(days=31))
        if value == cls.NEXT_QUARTER:
            next_quarter = (start_of_quarter + datetime.timedelta(days=90)).replace(
                day=1
            )
            return DatetimeRange(
                next_quarter, next_quarter + datetime.timedelta(days=90)
            )
        if value == cls.NEXT_YEAR:
            next_year = start_of_year.replace(year=start_of_year.year + 1)
            return DatetimeRange(
                next_year,
                next_year.replace(year=next_year.year + 1) - datetime.timedelta(days=1),
            )
        raise ValueError(f"Invalid range: {value}")


class DatetimeRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

        if isinstance(self.start, str) and self.start:
            self.start = datetime.datetime.fromisoformat(self.start)

        if isinstance(self.end, str) and self.end:
            self.end = datetime.datetime.fromisoformat(self.end)

        if isinstance(self.start, datetime.date):
            self.start = timezone.localtime().replace(
                year=self.start.year, month=self.start.month, day=self.start.day
            )

        if isinstance(self.end, datetime.date):
            self.end = timezone.localtime().replace(
                year=self.end.year, month=self.end.month, day=self.end.day
            )

    def as_tuple(self):
        return (self.start, self.end)

    def total_days(self):
        return (self.end - self.start).days

    def __iter__(self):
        # Iters days currently... probably should have an iter_days method instead
        return iter(
            self.start.date() + datetime.timedelta(days=i)
            for i in range(0, self.total_days())
        )

    def __repr__(self):
        return f"DatetimeRange({self.start}, {self.end})"

    def __str__(self):
        return f"{self.start} to {self.end}"

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __hash__(self):
        return hash((self.start, self.end))

    def __contains__(self, item):
        return self.start <= item <= self.end
