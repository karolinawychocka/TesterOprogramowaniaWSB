# index operator [] - give acces to a sequences element (string, tuples, lists)

name = "karo lina"

if(name[0].islower()):
    name = name.capitalize()

first_name = name[0:4].upper()
last_name = name[5:9].lower()
last_character = name[-1]

print(name)
print(first_name)
print(last_name)
print(last_character)
