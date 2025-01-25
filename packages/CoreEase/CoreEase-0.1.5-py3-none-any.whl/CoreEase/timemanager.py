import datetime
from .system import CurrentSystemTime
def CalculateTimeDifferencetoTargetTime24HourFrame(targettime):
    currenttime = CurrentSystemTime()
    targettime = datetime.datetime.combine(currenttime.date(), datetime.datetime.strptime(targettime, "%H:%M").time())
    timedifference = targettime - currenttime
    if timedifference.total_seconds() <= 0:
        return False
    return timedifference





