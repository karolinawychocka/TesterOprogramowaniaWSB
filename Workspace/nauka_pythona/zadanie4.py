imie = "Ala"
ilosc = 5
zwierze ="kot"

print("Ile kotów ma " + imie + "?")

if ilosc == 0:
    print("{0} ma {1} {2}ów".format(imie, ilosc, zwierze))
elif ilosc >= 5:
    print("{0} ma {1} {2}ów".format(imie, ilosc, zwierze))
elif ilosc > 1:
    print("{0} ma {1} {2}y".format(imie, ilosc, zwierze))
else:
    print("{0} ma {1} {2}a".format(imie, ilosc, zwierze))
