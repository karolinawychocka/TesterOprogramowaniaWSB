
try:
    with open ('notatka.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :c")


