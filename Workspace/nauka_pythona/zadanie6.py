koszyk = ["jablka", "jajka", "mleko"]
cena = [2, 3, 10]
alergia = ["jablka", "jajka", "wisnie"]

for idx in range(len(koszyk)):
    print("{0}: {1}".format(idx, koszyk[idx]))
    print("{0}: {1}".format(idx, cena[idx]))

    produkt = koszyk[idx]
    if produkt in alergia:
        print("Uwaga - produkt alergiczny")
