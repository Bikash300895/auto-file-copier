import string
from ctypes import windll
import time
import os
import copy

directory = "C:\\Users\\bikas\\Desktop"
prev_files = []
toCopy = []


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


prev_files = get_desktop_file()
prev_dirve = get_drives()

while(True):
    #print(prev_dirve)
    current_drive = get_drives()
    #print(current_drive)

    # Checks for change in files and if detected add it in toCopy list
    current_file = get_desktop_file()


    prev_files = current_file

    # Checks for new drive and if detected copy files
    new_drive = []
    for drive in current_drive:
        if drive not in prev_dirve:
            new_drive.append(drive)

    for drive in new_drive:
        print("New drive detected: "+ drive)
        #TODO call the copy function to copy files async


    prev_dirve = current_drive

    #print("waiting...")
    time.sleep(2)
