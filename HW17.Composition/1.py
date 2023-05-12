class Profile():
    def __init__(self, name, last_name, age, passport):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.passport = passport
    def print_info(self) :
        print(self.name, self.last_name, self.age, self.passport)

class Adress():
    def __init__(self, City, street, zipcode):
        self.City = City
        self.street = street
        self.zipcode = zipcode

class Role():
    def __init__(self, Role, hours_worked):
        self.Role = Role
        self.hours_worked = hours_worked

class BankAccount():
    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance

class Order():
    def __init__(self):
        self.Item = ""
        self.date = ""
        self.delivery = None
        self.price = None
    def getorder(self) :
        print(self.Item, self.date, self.delivery, self.price)

        self.item = Item
        self.date = date
        self.delivery = delivery
        self.price = price



class User():
    def __init__(self, name, last_name, age, pasport):
        self.profile = Profile(name, last_name, age, pasport)
        self.adress = []
        self.role = []
        self.bankaccount = []
        self.order = []

    def addadress(self, city, street, zipcode):
        self.adress.append(Address(city, street, zipcode))

    def addrole(self, role, hours_worked):
        self.role.append(Role(role, hours_worked))

    def addbankaccount(self, card_number, balance):
        self.bankaccount.append(BankAccount(card_number, balance))

    def addorder(self, item, date, delivery, price):
        order = Order()
        order.getorder(item, date, delivery, price)
        self.order.append(order)
