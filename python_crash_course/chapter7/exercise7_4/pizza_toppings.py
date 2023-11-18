topping = ""
prompt = "Write a topping about pizza or write quit to leave the program: "
flag = True
while flag:
    topping = input(prompt)
    if topping == "quit":
        flag = False
    print(topping)
