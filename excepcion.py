import sys

try:
    x = int(input("X: "))
    y = int(input("Y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    #Exit the program
    sys.exit(1)

print(f"{x}/{y} = {result}")