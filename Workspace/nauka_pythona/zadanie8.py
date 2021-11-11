samochod = {"name": "Toyota", "cena": 200000, "type": "SUV" }

print("SAMOCHOD:")
print(samochod["name"])
print(samochod["cena"])
print(samochod["type"])

print("PĘTLA PO KLUCZACH:")
for key in samochod:
    print("{0}: {1}".format(key, samochod[key]))

print("PĘTLA PO ITEMS:")
for key, value in samochod.items():
    print("{0}: {1}".format(key, value))
