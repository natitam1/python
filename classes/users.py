class User:
    def __init__(self, first_name, last_name, age, sex, email, city, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.email = email
        self.city = city
        self.login_attempts = login_attempts

    def describe_user(self):
        print("\nBasic Information")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"\nAge: {self.age}", f"Sex: {self.sex}", f"\nEmail: {self.email}", f"\nCity: {self.city}")
    
    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Natnael", "Tamiru", 16, "M", "natnael@gmail.com", "Addis Ababa" ,1)
user2 = User("Abebe", "Chala", 22, "M", "abe23@gmail.com", "Hawassa", 2)

print(user2.first_name)
user2.greet_user()
print(user2.login_attempts)
user2.increment_login_attempts()
print(user2.login_attempts)
user2.increment_login_attempts()
print(user2.login_attempts)
user2.increment_login_attempts()
print(user2.login_attempts)
user2.increment_login_attempts()
print(user2.login_attempts)
user2.increment_login_attempts()
print(user2.login_attempts)
user2.increment_login_attempts()
print(user2.login_attempts)
user2.reset_login_attempts()
print(user2.login_attempts)