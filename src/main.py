import string
from ctypes import windll
import time
import shutil
import os
# from src.copy_to import CopyTo

directory = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
prev_files = []
toCopy = []


def copy_file(files, drive):
    for file in files:
        if os.path.isdir(file):
            try:
                copytree(file, drive + ":\\")
            except:
                print("copying directory error")
        else:
            try:
                copyfile(file, drive + ":\\")
            except:
                print("Copying file error")


def copyfile(file, drive):
    shutil.copy(file, drive)
    print("Copying")


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
        print("Copying")



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
    print(files)
    return files


def check_file_change(previous_files, current_files):
    for dir in current_files:
        for x in previous_files:
            if x[0] == dir[0]:
                prev_dir = x

        for folder in dir[1]:
            if folder not in prev_dir[1]:
                path_name = dir[0] + "\\" + folder
                toCopy.append(path_name)

        for file in dir[2]:
            if file not in prev_dir[2]:
                if dir[0] not in toCopy:
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
        copy_file(toCopy, drive)

    prev_dirve = current_drive

    print("waiting...")
    time.sleep(.5)
