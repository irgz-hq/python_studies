sandwich_orders = [
    "x-burguer", "pastrami", "pastrami", "double burguer", 
    "pastrami", "american",
    ]
finished_sandwiches = []

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nI Will make the {sandwich}!")
    print(f"The {sandwich} is finished!")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print("\n", sandwich)