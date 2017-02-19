import string
from ctypes import windll
import time
import os
import copy

directory = "C:\\test"
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


def check_file_change(previous_files, current_files):
    for dir in current_files:
        flug = True

        for x in previous_files:
            if x[0] == dir[0]:
                flug = False

        if flug:
            toCopy.append(dir[0])

        else:
            prev_dir = ()

            for x in previous_files:
                if x[0] == dir[0]:
                    prev_dir = x

            for file in dir[2]:
                if file not in prev_dir[2]:
                    path_name = dir[0] + "\\" + file
                    toCopy.append(path_name)
                    print(toCopy)


prev_files = get_desktop_file()
prev_dirve = get_drives()

while(True):
    # print(prev_dirve)
    current_drive = get_drives()
    # print(current_drive)

    # Checks for change in files and if detected add it in toCopy list
    curr_file = get_desktop_file()
    check_file_change(prev_files, curr_file)

    prev_files = curr_file

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
