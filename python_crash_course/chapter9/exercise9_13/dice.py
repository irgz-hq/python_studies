from random import randint

class Die:
    def __init__(self, side = 6):
        self.side = side

    def roll_die(self):
        num_rand = randint(1, self.side)
        return num_rand

die_6 = Die()
list_die_6 = []
die_10 = Die(10)
list_die_10 = []
die_20 = Die(20)
list_die_20 = []

for i in range(0,10):
    list_die_6.append(die_6.roll_die())
    list_die_10.append(die_10.roll_die())
    list_die_20.append(die_20.roll_die())

print(f"list of die_6: {list_die_6}")
print(f"list of die_10: {list_die_10}")
print(f"list of die_20: {list_die_20}")