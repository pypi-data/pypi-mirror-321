import os
def CheckFileExistence(file):
    if os.path.exists(file):
        return True
    else:
        return None
def CreateFile(file):
    explorer = open(file, "w")
    explorer.write("")
    explorer.close()
def ReadFile(file):
    explorer = open(file, "r")
    content = explorer.read()
    explorer.close()
    return content
def AppendtoFile(file,content):
    explorer = open(file, "a")
    explorer.write(content + "\n")
    explorer.close()
def OverwriteFile(file,content):
    explorer = open(file, "w")
    explorer.write(content + "\n")
    explorer.close()