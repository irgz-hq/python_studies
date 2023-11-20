class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(self.battery_size)

class EllectricCar:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.battery = Battery(60)

    def range(self):
        if self.battery.battery_size > 50:
            print("good")
        else:
            print("bad")

e_car = EllectricCar("sedan", "blue")
e_car.range()
