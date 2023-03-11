import os

for i in range(2, 11, 2):
    old_folder_name = os.path.join("target", str(i))
    new_folder_name = os.path.join("target", "ахах, лох, тебя взломали {0}".format(i))
    os.rename(old_folder_name, new_folder_name)