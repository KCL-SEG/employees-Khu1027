"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.pay = 0
        self.string = ''
        self.initialise()

    def initialise(self):
        if self.name == 'Billie':
            self.pay = 4000
            self.string = "Billie works on a monthly salary of 4000. Their total pay is 4000."

        if self.name == 'Charlie':
            self.pay = 2500
            self.string = "Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500."

        if self.name == 'Renee':
            self.pay =  3800
            self.string = "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800."

        if self.name == 'Jan':
            self.pay = 4410
            self.string = "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410."

        if self.name == 'Robbie':
            self.pay = 3500
            self.string = "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500."

        if self.name == 'Ariel':
            self.pay = 4200
            self.string = "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200."


    def get_pay(self):
        return self.pay
        
    def __str__(self):
        return self.string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
