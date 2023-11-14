pizzas = ['chicken', 'shrimp', 'pepperoni']
friend_pizzas = pizzas[:]
pizzas.append("cheese")
friend_pizzas.append("3cheese")

for i in pizzas:
    print(i)

for j in friend_pizzas:
    print(j)

