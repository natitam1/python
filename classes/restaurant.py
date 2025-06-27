class Restaurant:
    """"a simple restaurant class"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        

    def describe_restaurant(self):
        print(f"{self.cuisine_type} in {self.restaurant_name}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment
        

restaurant = Restaurant("Tegem", "Shiro Wot")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.number_served)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(8)
print(restaurant.number_served)
restaurant.increment_number_served(1)
print(restaurant.number_served)