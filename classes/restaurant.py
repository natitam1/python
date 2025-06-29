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
        

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavor(self):
        for flavor in self.flavors:
            print(flavor)

instance_1 = IceCreamStand("Tegerm", "Shiro", "Sour")
instance_2 = IceCreamStand("Tegerm", "Doro", "Bitter")
instance_3 = IceCreamStand("Tegerm", "Pasta", "Tang")

instance_1.describe_restaurant()
instance_2.describe_restaurant()
instance_3.describe_restaurant()