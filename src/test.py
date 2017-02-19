import os
directory = "C:\\test"

# for name in os.listdir():
#     if os.path.isdir("C:\\Users\\bikas\\Desktop"):
#         print(name)

list = [x for x in os.walk(directory)]
print(list)