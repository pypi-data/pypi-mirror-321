import os
import system
def ClearConsole():
    os.system("cls")
def Print(string):
    print(string)
def Input(string):
    input(string)
def EnumeratedPrint(list):
    for x,y in enumerate(list):
        print(x + y)
def CenteredPrint(string,filler):
    console_w = system.ConsoleWidth()
    print(string.center(console_w, filler))
def CenteredInput(string):
    console_w = system.ConsoleWidth()
    console_lp = console_w // 2 - (len(string)+2)
    x = input(" " * console_lp + string + " " * 5)
    return x
def EnumeratedCenteredPrint(list):
    console_w = system.ConsoleWidth()
    for x,y in enumerate(list):
        print(x + y.center(console_w, " "))