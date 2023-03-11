import os

os.makedirs("target")

for i in range(1, 11, 1):
    folder_name = os.path.join("target", str(i))
    os.makedirs(folder_name)