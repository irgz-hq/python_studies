import pytest

from employee import Employee

@pytest.fixture
def employee_instance():
    employee_instance = Employee("Ravena", "Paulino", 100000)
    return employee_instance


def test_give_default_raise(employee_instance):
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 105000

def test_give_default_raise(employee_instance):
    employee_instance.give_raise(10000)
    assert employee_instance.annual_salary == 110000

