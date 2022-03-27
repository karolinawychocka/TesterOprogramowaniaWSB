#move files

import os

source = "C:\\Users\\48531\\Desktop\\kopianotatki2.txt"
destination = "C:\\Users\\48531\\Desktop\\TesterOprogramowaniaWSB\\Nauka_Pythona\\kopianotatki2.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")