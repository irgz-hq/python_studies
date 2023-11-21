import lottery

counter = 0
my_ticket = "1b77"
while True:
    winner_ticket = lottery.winner_ticket()
    if winner_ticket == my_ticket:
        break
    counter += 1

print(counter)