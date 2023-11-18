prompt = "Digit your age or quit or exit to exit the program: "
counter = 0
flag = True
while flag:
    age = input(prompt)
    counter += 1
    if age == "quit":
        break
    if age == "exit":
        flag = False
    else:
        age = float(age)
        if age < 3:
            price = "is free"
        elif age < 12:
            price = "cost $10"
        else:
            price = "cost $15"

    if counter == 5:
        flag = False
    print(f"\nThe ticket {price}")
