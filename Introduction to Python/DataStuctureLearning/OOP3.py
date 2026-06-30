# #Inheritance is the inheritance of a parent class to a child class
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

class cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def meow(self):
        print(f"{self.name} is meowing")
    def details(self):
        print(f"The name of this cat is {self.name}")
        print(f"Its breed is {self.breed}")

jinger = cat("jinger", "Orange_tabby")
jinger.eat()
jinger.details()
jinger.meow()

#Abstraction
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class car(Vehicle):
    def start_engine(self):
        print("Engine Started get ready!")
    def stop_engine(self):
        print("Engine stopped brace for impact")
class bike(Vehicle):
    def start_engine(self):
        print("Get ready, VROOOM")
carObj = car()
carObj.start_engine()
carObj.stop_engine()
bikeObj = bike()
bikeObj.start_engine()


class AnimalAbs(ABC):
    @abstractmethod
    def eat(self):
        pass
class dogabs(AnimalAbs):
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} is now barking!")
    def eat(self):
        print(f"{self.name} is eating now")

class catabs(AnimalAbs):
    def __init__(self, name):
        self.name = name
    def meow(self):
        print(f"{self.name} is now meowing!")
    def eat(self):
        print(f"{self.name} is eating now")

buddy = dogabs("buddy")
buddy.bark()
buddy.eat()
bingo = catabs("bingo")
bingo.meow()
bingo.eat()