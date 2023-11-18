counter = 0
prompt = "If you could visit one place in the world, where would you go? "
vacations = []

while counter < 5:
    vacation = input(prompt)
    vacations.append(vacation)
    counter += 1

for vacation in vacations:
    print(vacation)