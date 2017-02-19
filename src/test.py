
current_drive = ['C', 'E', 'F']
prev_dirve = ['C', 'E']

new_drive = []
for drive in current_drive:
    if drive not in prev_dirve:
        new_drive.append(drive)

for drive in new_drive:
    print("New drive detected: "+ drive)