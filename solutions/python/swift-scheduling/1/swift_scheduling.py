"""schedule"""
from datetime import datetime, timedelta
import calendar
import math

NOW = "NOW"
ASAP = "ASAP"
EOW = "EOW"
N_TH_MONTH = "*M"
N_TH_QUARTER = "Q*"

FRI = 4
SAT = 5
SUN = 6

def two_hours_after_start(meeting_start_time, nth):
    """Two hours after the meeting started"""
    return  meeting_start_time + timedelta(hours=2)

def today_or_tomorrow(meeting_start_time, nth):
    """Before 13:00 	Today at 17:00
        After or at 13:00 	Tomorrow at 13:00"""
    if meeting_start_time.hour < 13:
        return meeting_start_time.replace(hour=17, minute=00, second=0, microsecond=0)
    tomorrow = meeting_start_time + timedelta(days=1)
    return tomorrow.replace(hour=13, minute=00, second=0, microsecond=0)

def end_of_week(meeting_start_time, nth):
    """Monday, Tuesday, or Wednesday 	Friday at 17:00
       Thursday or Friday 	Sunday at 20:00 """
    if meeting_start_time.weekday() in {0,1,2}:
        days_until_fri = FRI - meeting_start_time.weekday()
        friday = meeting_start_time + timedelta(days=days_until_fri)
        return friday.replace(hour=17, minute=00, second=0, microsecond=0)
    days_until_sun = SUN - meeting_start_time.weekday()
    sunday = meeting_start_time + timedelta(days=days_until_sun)
    return sunday.replace(hour=20, minute=00, second=0, microsecond=0)

def first_workday(meeting_start_time, nth):
    """Before N-th month 	At 8:00 on the first workday of this year's N-th month
        After or in N-th month 	At 8:00 on the first workday of next year's N-th month"""
    year = meeting_start_time.year if meeting_start_time.month < nth else meeting_start_time.year + 1
    first_day = datetime(year, nth, 1)
    days_to_monday = (7 - first_day.weekday()) % 7
    first_business_day = first_day + timedelta(days=days_to_monday) if first_day.weekday() in {SAT, SUN} else first_day
    return first_business_day.replace(hour=8, minute=00, second=0, microsecond=0)

def last_workday(meeting_start_time, nth):
    """Before or in N-th quarter 	At 8:00 on the last workday of this year's N-th quarter
       After N-th quarter 	At 8:00 on the last workday of next year's N-th quarter """
    year = meeting_start_time.year if math.ceil(meeting_start_time.month / 3) <= nth else meeting_start_time.year + 1
    month = nth*3
    _, total_days = calendar.monthrange(year, month)
    last_day = datetime(year, month, total_days)
    last_business_day = last_day - timedelta(days=last_day.weekday()-FRI) if last_day.weekday() in {SAT, SUN} else last_day
    return last_business_day.replace(hour=8, minute=00, second=0, microsecond=0)

TRANSLATIONS = {
    NOW: two_hours_after_start,
    ASAP: today_or_tomorrow,
    EOW: end_of_week,
    N_TH_MONTH: first_workday,
    N_TH_QUARTER: last_workday,
}

def delivery_date(start, description):
    """transalte the meeting time and description into an actionable timestamp"""
    num_str = "".join(char for char in description if char.isdigit())
    nth = int(num_str) if num_str else None
    key = description if nth is None else description.replace(num_str, "*")
    return TRANSLATIONS[key](datetime.fromisoformat(start), nth).isoformat()
