import requests

class Employee:

    #The percentage of the raise
    raise_amt = 1.05

    #Setting up class vars
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    #Function for craeting employee's email
    @property
    def email(self):
        return  '{}.{}@email.com'.format(self.first, self.last)

    #Function for craeting employee's full-name
    @property
    def fullname(self):
        return  '{} {}'.format(self.first, self.last)

    #Function for returning the raise to employees salary
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    #Function for testing code integrity with no depandency on network connection
    def monthly_schedule(self, month):
        response = requests.get(f'https://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad response'