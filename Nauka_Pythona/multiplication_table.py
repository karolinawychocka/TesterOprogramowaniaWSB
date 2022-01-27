# multiplication table

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))

for i in range(rows):
    for j in range(columns):
        print((i + 1) * (j + 1), end=" ")
    print()
