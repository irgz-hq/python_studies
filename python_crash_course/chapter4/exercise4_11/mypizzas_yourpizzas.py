pizzas = ['chicken', 'shrimp', 'pepperoni']
friend_pizzas = pizzas[:]
pizzas.append("cheese")
friend_pizzas.append("3cheese")

for i in range(len(pizzas)):
    print(f'I like {pizzas[i]} pizza')
    print(f'My friends likes {friend_pizzas[i]} pizza')
print('I really like pizza')