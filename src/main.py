import string
from ctypes import windll
import time
import os

directory = "C:\\Users\\bikas\\Desktop"

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
          
    return drives


def get_desktop_file():
    files = [x for x in os.walk(directory)]
    return files


prev_dirve = get_drives()
while(True):
    get_desktop_file()

    print(prev_dirve)
    current_drive = get_drives()
    print(current_drive)

    new_drive = []
    for drive in current_drive:
        if drive not in prev_dirve:
            new_drive.append(drive)

    for drive in new_drive:
        print("New drive detected: "+ drive)

    prev_dirve = current_drive

    print("waiting...")
    time.sleep(2)
