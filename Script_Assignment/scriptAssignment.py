

import os
import time

fPath = 'C:\\Users\\Matt\\Documents\\GitHub\\Python_Projects\\Script_Assignment'

directory = os.listdir(path = 'C:\\Users\\Matt\\Documents\\GitHub\\Python_Projects\\Script_Assignment')
newdir = []

for a in directory:
    if ".txt" in a:
        newdir.append(a)


for x in newdir:
    abPath = os.path.join(fPath, x)

for x in newdir:
    modTime =  os.path.getmtime(abPath)  # Using os.getmtime() results in AttributeError: module 'os' has no attribute 'getmtime'
    localTime = time.ctime(modTime)      # Converting modTime from seconds since epoch to local time

def runScript():
    for x in newdir:
        print('\n' + x + ' last modified: ' + localTime)


if __name__ == "__main__":
    runScript()

