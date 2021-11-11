mleko = {'nazwa': 'Mleko łaciate', 'cena': 5}
masło = {'nazwa': 'Masło extra', 'cena': 4.30}
czekolada = {'nazwa': 'Czekolada wedel', 'cena': 8.20}
baton = {'nazwa': 'Baton Kit Kat', 'cena': 1.20}
ser = {'nazwa': 'Ser Bieluch', 'cena': 4.20}

koszyk = [mleko, masło, czekolada, baton, ser]
suma = 0

for produkt in koszyk:
    print(produkt['nazwa'], produkt['cena'])    
    suma = suma + produkt['cena']
    
if mleko in koszyk and ser in koszyk:
    print("tak mleko i ser w koszyku")
    suma *= 0.9

print("Wartosc koszyka wynosi {0}".format(suma))
