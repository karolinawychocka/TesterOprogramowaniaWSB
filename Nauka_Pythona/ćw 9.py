#logical operators

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("Temperature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("Temperature is bad today!")
    print("Stay home!")