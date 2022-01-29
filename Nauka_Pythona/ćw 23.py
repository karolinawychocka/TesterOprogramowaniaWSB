# nested function calls

num = input("Enter a number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

# same as 

print(round(abs(float(input("Enter a whole positive number: ")))))