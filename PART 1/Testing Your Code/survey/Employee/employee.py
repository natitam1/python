class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        """Set the name and salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount = 5000):
        """Increases the amount by the given amounts."""
        self.annual_salary += amount