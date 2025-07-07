from employee import Employee

def test_give_default_raise():
    """Test the class with the default value."""
    new_employee = Employee("Natnael", "Tamiru", 2000)
    new_employee.give_raise()
    assert new_employee.annual_salary == 7000
def test_give_custom_raise():
    """Test with custom amount"""
    new_employee = Employee("Natnael", "Tamiru", 2000)
    new_employee.give_raise(1000)
    assert new_employee.annual_salary == 3000
    