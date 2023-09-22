class CreditCart:
    # constractor:
    def __init__(self, customer, bank, acount, limit):
        self.customer = customer
        self.bank = bank
        self.acount = acount
        self.customer = customer
        self.limit = limit
        self.balance = 0

    # the methods :
    def get_customer(self):
        return self.customer
    
    def get_acount(self):
        return self.acount
    
    def get_bank(self):
        return self.bank
    
    def get_limit(self):
        return self.limit
    
    def get_balance(self):
        return self.balance

    def charge(self, price):
        if price + self.balance > self.limit:
            return False
        else:
            self.balance += price
            return True
        
# instance of class
instance = CreditCart('jaouher', 'atb', '15325325623', 'hhh')

print("the customer : "+instance.customer)
print("the bank : "+instance.bank)
        

people = [ 'jaouer', 'mahmoud']

print(people)
print('--------------------------------------------')

people.append('majed')
print(people)

people.insert(2, 'med ali')

print(people)
print('--------------------------------------------')


class Family: # super class ou class parent
    lastName = 'Bouziene'
    nationality = 'Tunisian'
    langue = 'arabic'

print(Family.lastName)

print('-------------------------')


class Family2(Family):  # subclass ou class fils
    age = 150

print('last name: ' +Family2.lastName)
print('nationality : ' +Family2.nationality)
print('langue: ' +Family2.langue)
print('age : ' +str(Family2.age))




