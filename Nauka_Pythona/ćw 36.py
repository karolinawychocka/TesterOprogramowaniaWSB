import os

path = 'dousuniecia.txt'

try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("Permission denied!")
else:
    print(path+ " was deleted")