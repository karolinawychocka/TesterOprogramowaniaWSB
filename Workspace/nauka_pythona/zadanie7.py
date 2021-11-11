koszyk = ['chleb', 'maslo', 'mleko', 'jajka', 'owoce']
cena = [5, 8, 3, 10, 20]

#R1
suma = sum(cena)
if len(koszyk) > 5:
    suma = suma - (suma * 5)/100
