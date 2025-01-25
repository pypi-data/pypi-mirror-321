import os
import shutil
import datetime
def CurrentUser():
    user = os.getlogin()
    return user
def CPUCount():
    cpucount = os.cpu_count()
    return cpucount
def ConsoleHeight():
    consoleheight = shutil.get_terminal_size().lines
    return consoleheight
def ConsoleWidth():
    consolewidth = shutil.get_terminal_size().columns
    return consolewidth
def CurrentSystemTime():
    time = datetime.datetime.now()
    return time