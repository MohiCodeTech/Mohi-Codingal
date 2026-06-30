import os
filename = "Sample.txt"
if os.path.exists(filename):
    print("This file exists")
else:
    print("This file does not exist")

filename = "data.txt"
if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("This is a brand new file")
    print("file didnt exist so now it is created")
else:
    print("file has already been created")

#Delete a file
filename = "new.txt"
if os.path.exists(filename):
    os.remove(filename)
    print(f"File {filename} has been successfully terminated")
else:
    print("This file doesn't exist")

#Delete a folder
folder_name = "No_terminate"
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"The folder {folder_name} has been terminated")
else:
    print("No such folder is present within file handling directory")

