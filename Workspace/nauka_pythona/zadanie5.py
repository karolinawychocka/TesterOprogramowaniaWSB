samochody = ['syrena', 'polonez', 'tarpan']

#print(samochody[0])
#print(samochody[1])

#pętla, wypisywanie zawaetości tablicy samochody
for i in samochody:
    print(i)

#sprawdzanie dlugosci tablicy
tablica_dlugosc = len(samochody)
indeksy = range(tablica_dlugosc)

for idx in indeksy:
    print("{0}: {1}".format(idx, samochody[idx]))

#moja wersja
print()

owoce =['jabłko', 'pomarancza', 'banan', 'kokos']

tablica_dl = len(owoce)
index = range(tablica_dl)

for indx in index:
    print("Owoc nr {0} to {1}".format(indx, owoce[indx]))
