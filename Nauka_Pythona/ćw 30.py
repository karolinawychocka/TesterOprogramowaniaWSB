#exception

try:
    num1 = int(input("Enter a number to divide: "))
    num2 = int(input("Enter a number to divide by: "))
    result = num1 / num2

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers!")
except Exception as e:
    print(e)
    print("Something went wrong :c")
else:
    print(result)
finally:
    print("This will always execute")
