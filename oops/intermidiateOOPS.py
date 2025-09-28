# # .	Create a class Animal with attributes name and age. Add a method speak() that prints something generic.
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print("My name is {}".format(self.name))
#
#
# #Create a subclass Dog that inherits Animal and overrides the speak() method.
# class Dog(Animal):
#     def speak(self):
#         print("{} is a faithfull animal ".format(self.name))
#
# dog = Dog("dog", 20)
# dog.speak()
#
# # # #Create a class BankAccount with methods deposit, withdraw, and check_balance. Add error checking for insufficient balance.
# #
# class BankAccount:
#
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#         self.transactions = []
#
#
#
#
#     def deposit(self,amount):
#         self.balance += amount
#         self.transactions.append(amount)
#         print("{} is deposited to {}'s account ".format(amount,self.name))
#         return self.balance
#
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print("{} is withdrawn from {}'s account ".format(self.name,amount))
#             self.transactions.append(-amount)
#             return self.balance
#
#
#
#     def print_balance(self):
#         print("{} is balanced ".format(self.name))
#         return self.balance
#
#
#     def print_transactions(self):
#         for transaction in self.transactions:
#             print("{} is transaction {}".format(self.name,transaction))
#
# def main():
#     print("Welcome to the BANK")
#     name = input("What is your name? ")
#     balance = float(input("how much would you like to deposit ? "))
#     account1 = BankAccount(name,balance)
#     while True:
#         user_choice = str(input("Would you like to deposit or withdraw? q to quit :: (d/w/t/q)"))
#         match user_choice.lower().strip():
#             case "d":
#                 account1.deposit(float(input("What is your balance? :")))
#
#             case "w":
#
#                 account1.withdraw(float(input("What is your balance? :")))
#
#             case "t":
#                 account1.print_transactions()
#
#             case "q":
#                 print("Thank you for using BANK")
#                 break
#
#             case _:
#                 print("That is not a valid choice")
#
#
#
# main()
#
#
# #5.	Write a class Student with name, marks and a method to calculate grade.
# TOTAL =600
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#
#
#
#     def calculateMarks(self):
#         average = (sum(self.marks) / TOTAL)*100
#         return 'A' if average > 85 else 'B' if 70 < average <= 85 else 'C'  if 50 < average <=70  else 'D' if 35 < average <= 50 else 'F'
#
#
#
#
# kumar = Student("Kumar",[90,80,90,80,90,90])
# print(kumar.calculateMarks())
#
#
#.	Create a class Circle with attribute radius and use a @property decorator to calculate area.
import math
class Circle():
    def __init__(self,radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2

big_circle = Circle(2)
print(f"the area of cirlce is :{big_circle.area:.2f}")
