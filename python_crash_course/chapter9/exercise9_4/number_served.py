class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        prompt = f'The restaurant name is {self.restaurant_name} '
        prompt += f'and the cuisine type is {self.cuisine_type}'
        print(prompt)

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("Restaurante Universitário", "lunch")

restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.number_served)
restaurant.number_served = 1
print(restaurant.number_served)
restaurant.set_number_served(2)
print(restaurant.number_served)
restaurant.increment_number_served(5)
print(restaurant.number_served)