"""Meetup"""
import calendar
from datetime import date

class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date."""
    def __init__(self):
        super().__init__("That day does not exist.")

WEEKDAYS = {name: i for i, name in enumerate(calendar.day_name)}
STATIC_OCCURRANCE = {"first":1,
             "second":2,
             "third":3,
             "fourth":4,
             "fifth":5}
LAST = "last"
TEENTH = "teenth"

def is_last(month, day_of_week, day):
    for week in reversed(month):
        if week[day_of_week] != 0:
            return day == week[day_of_week]
        
def is_teenth(day):
    return 13 <= day <= 19

def meetup(year, month, week, day_of_week):
    """meetup"""
    target_occurrance = STATIC_OCCURRANCE.get(week)
    target_dow = WEEKDAYS[day_of_week]    
    dows_occured = 0
    month_calendar = calendar.monthcalendar(year, month)
    for week_calendar in month_calendar:
        for day_dow, day in enumerate(week_calendar):
            if day != 0 and day_dow == target_dow:
                dows_occured +=1
                if ((target_occurrance is not None and dows_occured == target_occurrance)
                        or (week == LAST and is_last(month_calendar, target_dow, day))
                        or (week == TEENTH and is_teenth(day))):
                    return date(year, month, day)

    raise MeetupDayException()