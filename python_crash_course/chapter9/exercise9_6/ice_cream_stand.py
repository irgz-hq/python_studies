class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        prompt = f'The restaurant name is {self.restaurant_name} '
        prompt += f'and the cuisine type is {self.cuisine_type}'
        print(prompt)

    def open_restaurant(self):
        print("The restaurant is open")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(self.flavors)

flavors = ["chocollate", "strawberry"]
ice_cream_stand = IceCreamStand("Restaurante Universitário", "lunch", flavors)
ice_cream_stand.display_flavors()