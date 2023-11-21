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

restaurant = Restaurant("Restaurante Universitário", "lunch")
