from employee import Employee
from unittest.mock import patch
import unittest


class TestEmployee(unittest.TestCase):

    #Setting up vars for testing
    def setUp(self):
        self.emp1 = Employee('Yam', 'Peled', 10000)
        self.emp2 = Employee('John', 'Doe', 15000)

    #assuring email func working correctly
    def test_email(self):
        self.assertEqual(self.emp1.email, 'Yam.Peled@email.com')
        self.assertEqual(self.emp2.email, 'John.Doe@email.com')

        self.emp1.first = 'Maor'
        self.emp2.first = 'Jane'

        self.assertEqual(self.emp1.email, 'Maor.Peled@email.com')
        self.assertEqual(self.emp2.email, 'Jane.Doe@email.com')

    # assuring fullname func working correctly
    def test_fullname(self):

        self.assertEqual(self.emp1.fullname, 'Yam Peled')
        self.assertEqual(self.emp2.fullname, 'John Doe')

        self.emp1.first = 'John'
        self.emp2.first = 'Joe'

        self.assertEqual(self.emp1.fullname, 'John Peled')
        self.assertEqual(self.emp2.fullname, 'Joe Doe')

    # assuring pay-raise func working correctly
    def test_pay_raise(self):

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 10500)
        self.assertEqual(self.emp2.pay, 15750)

    #using mock utility to check code integrity with no depandency on network connection
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('https://company.com/Peled/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp2.monthly_schedule('June')
            mocked_get.assert_called_with('https://company.com/Doe/June')
            self.assertEqual(schedule, 'Success')

    if __name__ == '__main__':
        unittest.main()