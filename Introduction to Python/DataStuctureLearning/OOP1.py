class garments:
    def __init__(self, color):
        self.color = color
    def Look(self):
        print("It looks nice")
    def colorTest(self):
        print(f"The color of this grament is {self.color}")

dress = garments("blue")
dress.colorTest()
dress.Look()

bracelet = garments("Orange")
bracelet.colorTest()

# Banking System
class Account:
    def __init__(self, bal, acc):
           self.balance = bal
           self.account_no = acc
    def debit(self, amount):
          self.balance = self.balance - amount
          print("Rs", amount, "was debited from account no. ", self.account_no)
          print("the balance is ", self.get_bal())
    def credit(self, ammount):
          self.balance += ammount
          print("Rs", ammount, "was credited by account no. ", self.account_no)
          print("the balance is ", self.get_bal())
    def get_bal(self):
          return self.balance
acc1 = Account(10000, 29114)
acc1.debit(300)
acc1.get_bal()

acc2 = Account(9742, 45983)
acc2.credit(1000)
acc2.get_bal

class teacher:
      name = "Laura"
      grade_teaching = 5

      def introduction(self):
            print("Hello, i am a teacher teaching at random school")
      def details(self):
            print("My name is", self.name, "and the grade I teach is ", self.grade_teaching, "th grade")

obj = teacher()
obj.introduction()
obj.details()

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def eat(self):
        print(f"{self.name} is eating")
    def walk(self):
         print(f"{self.name} is walking")
    def details(self):
        print(f"Its name is {self.name} and its color is {self.color}")

dog = Animal("Bradford", "brown")
dog.eat()
dog.walk()
dog.details()
