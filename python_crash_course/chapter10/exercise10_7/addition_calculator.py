while True:

    value1 = input("Enter the first number or q to exit: ")
    if value1 == "q":
        break
    value2 = input("Enter the second number or q to exit: ")
    if value2 == "q":
        break
    try:
        value1 = float(value1)
        value2 = float(value2)

    except ValueError:
        print("You didn't enter a number")

    else:
        print(value1+value2)