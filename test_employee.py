import unittest
from employee import Employee

class TestEmplyeeRaise(unittest.TestCase):

    def setUp(self):
        first_name = "Sam"
        last_name = "Chia"
        annual_salary = 5000
        self.my_employee = Employee(first_name, last_name, annual_salary)
        self.raise_amount = 2000

    def test_give_default_raise(self):
        new_raise = self.my_employee.give_raise()
        self.assertEqual(new_raise, 10000)

    def test_give_custom_raise(self):
        new_raise_custom = self.my_employee.give_raise(self.raise_amount)
        self.assertEqual(new_raise_custom, 7000)

unittest.main()