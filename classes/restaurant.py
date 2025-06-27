class Restaurant:
    """"a simple restaurant class"""
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        

    def describe_restaurant(self):
        print(f"{self.cuisine_type} in {self.restaurant_name}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")

restaurant = Restaurant("Tegem", "Shiro Wot", 13)
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.number_served)
restaurant.describe_restaurant()
restaurant.open_restaurant()