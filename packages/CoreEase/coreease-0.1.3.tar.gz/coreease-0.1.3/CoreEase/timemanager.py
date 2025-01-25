import datetime
import system
def CalculateTimeDifferencetoTargetTime(targettime):
    currenttime = system.CurrentSystemTime()
    targettime = datetime.datetime.combine(currenttime.date(), datetime.datetime.strptime(targettime, "%H:%M").time())
    timedifference = targettime - currenttime
    return timedifference





