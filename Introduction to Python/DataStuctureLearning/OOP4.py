# #PolyMorphism
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def make_sound(self):
#         return "An animal sound"
#     def eat(self):
#         return "eating"

# class Dog(Animal):
#      def make_sound(self):
#         return "Bark"
#      def eat(self):
#         return "bite"
     
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"
#     def eat():
#         return "pur"
    
# def animal_sound(OBJ):
#     print(OBJ.make_sound())

# dog = Dog("buddy")
# print(dog.make_sound())
# print(dog.eat())

# animal_sound(dog)

#Encapsulation
# class Bank_Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#     #getter method
#     def get_balance(self):
#         return self.__balance
    
#     #setter method
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposit {amount} new current balance is {self.__balance}")
#         else:
#             print("Insufficient funds")
#     def withdraw(self, amount):
#         if amount > 0 <= self.__balance:
#             self.__balance -= amount
#             print(f"The amount withdrawed is {amount} the new current balance is {self.__balance}")
#         else:
#             print("Insufficient balance or invalid amount")

# new_account = Bank_Account("Moheathraam", 5000)
# new_account.deposit(1000)
# new_account.withdraw(3000)

class car:
    def __init__(self, name , price):
        self.name = name
        self.__price = price
    def get_price(self):
        return self.__price

