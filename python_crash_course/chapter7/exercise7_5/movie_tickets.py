prompt = "Digit your age ou quit to exit the program : "

while True:
    age = input(prompt)
    if age == "quit":
        break
    else:
        age = float(age)
        if age < 3:
            price = "is free"
        elif age < 12:
            price = "cost $10"
        else:
            price = "cost $15"
    
    print(f"The ticket {price}")