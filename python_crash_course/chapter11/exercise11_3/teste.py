class Qualquer:
    def __init__(self, num):
        self.num = num

    def update(self, num_up=1):
        self.num += num_up

qe = Qualquer(5)
print(qe.num, type(qe.num))
        