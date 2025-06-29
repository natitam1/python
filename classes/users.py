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

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, age, sex, email, city, login_attempts, privileges):
        super().__init__(first_name, last_name, age, sex, email, city, login_attempts)
        self.privileges = Privileges(privileges)

