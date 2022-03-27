import os

path = "C:\\Users\\48531\\Desktop\\TesterOprogramowaniaWSB\\Nauka_Pythona\\notatka.txt"

if os.path.exists(path):
    print("That location exist!")
    if os.path.isfile(path):
        print("That is a file!")
    else os.path.isdir(path):
        print("That is a directory!")

else:
    print("That location doesn't exist!")


