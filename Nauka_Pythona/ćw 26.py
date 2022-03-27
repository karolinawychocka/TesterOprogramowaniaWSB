#args in tuples

#def add(num1, num2):
#    sum = num1 + num2
#    return sum

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(2, 5, 5, 9, 10))
