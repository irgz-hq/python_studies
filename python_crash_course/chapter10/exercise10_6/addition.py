value1 = input("Enter the first number: ")
value2 = input("Enter the second number: ")

try:
    value1 = float(value1)
    value2 = float(value2)

except ValueError:
    print("You didn't enter a number")

else:
    print(value1+value2)