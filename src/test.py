import os
directory = "C:\\test"

# for name in os.listdir():
#     if os.path.isdir("C:\\Users\\bikas\\Desktop"):
#         print(name)

toCopy = []

previous_files = [('C:\\test', ['I1', 'I2'], []), ('C:\\test\\I1', [], ['1.mp4', '2.mp4', '3.mp4', '4.mp4']), ('C:\\test\\I2', ['I1'], ['5.mp4', '6.mp4', '7.mp4']), ('C:\\test\\I2\\I1', [], ['1.mp4', '2.mp4', '3.mp4', '4.mp4'])]
current_files = [('C:\\test', ['I1', 'I2'], []), ('C:\\test\\I1', [], ['1.mp4', '2.mp4', '3.mp4', '4.mp4']), ('C:\\test\\I2', ['I1'], ['5.mp4', '6.mp4', '7.mp4']), ('C:\\test\\I2\\I1', [], ['1.mp4', '2.mp4', '3.mp4', '4.mp4'])]

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
                path_name = dir[0]+"\\"+file
                toCopy.append(path_name)

print(toCopy)