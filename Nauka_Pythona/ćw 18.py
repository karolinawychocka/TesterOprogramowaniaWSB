# dictionary - changable, unordered, unique - key : values

capitals = {"USA": "Washington",
            "Poland": "Warsaw",
            "Russia": "Moscow",
            "Germany": "Berlin"}

capitals.update({"Czechy": "Praga"})
capitals.update({"USA": "Washington DC"})
capitals.pop("Russia")
# capitals.clear()

print(capitals["Poland"])
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals)

for key, value in capitals.items():
    print(key, value)