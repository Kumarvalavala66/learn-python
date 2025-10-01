# # 1. Instance vs Class Variables
# #
# #
# # - [ ] 	•	Create a class Car with:
# # - [ ] 	•	Instance variables: brand, model.
# # - [ ] 	•	Class variable: wheels = 4.
# # - [ ] 	•	Create 2 objects with different brands and models.
# # - [ ] 	•	Print their details, and then change wheels for the whole class.
# # - [ ] 	•	Observe how both objects reflect the change.

# - [ ] 	•	Add a class method change_wheels(cls, num) in Car that updates the class variable wheels.
# - [ ] 	•	Call this method to change wheels to 6 and print results.


# class Car:
#
#     wheels = 4
#
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     @classmethod
#     def wheel_changging(cls,wheels):
#         cls.wheels = wheels
#
#
# car1 = Car('TATA','xuv')
# car2 = Car('BMW','m4')
# print(f"{car1.brand} {car1.model} has {car1.wheels} wheels")
# print(f"{car2.brand} {car2.model} has {car2.wheels} wheels")
#
#
# Car.wheel_changging(12)
#
# print(f"{car1.brand} {car1.model} has {car1.wheels} wheels")
# print(f"{car2.brand} {car2.model} has {car2.wheels} wheels")
#
#

# . Static Method
#
#
# - [ ] 	•	Add a static method is_motorcycle(wheels) that returns True if wheels == 2.
# - [ ] 	•	Test it with different inputs.

# class MotorCycle:
#     wheels = 2
#     def __init__(self,brand,wheels):
#
#         self.brand = brand
#         self.wheels = wheels
#
#
#     @staticmethod
#     def wheels_are_ok(wheels):
#         return wheels == 2
#
# bike = MotorCycle('ducati',2)
# print(bike.wheels_are_ok(2))

# . Alternative Constructor (Class Method)
#
#
# # - [ ] 	•	Create a class Person with instance variables name and age.
# # - [ ] 	•	Add a class method from_string(cls, string) that takes "Name,Age" and returns a new Person object.
#
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def from_string(cls,string):
#         name,age = string.split(",")
#         try:
#             age = int(age)
#         except ValueError:
#             print("Invalid input")
#         else:
#             return cls(name,age)
#
#
# person1 = Person('kumar',23)
# print(f"{person1.name} is {person1.age} years old")
# person2 =  Person.from_string("Marco,32")
# print(f"{person2.name} is {person2.age} years old")


#  Complete Example
#
#
# - [x] 	•	Create a class BankAccount with:
# - [x] 	•	Instance variables: owner, balance.
# - [x] 	•	Class variable: bank_name = "Python Bank".
# - [ ] 	•	Class method: change_bank_name(cls, new_name).
# - [ ] 	•	Static method: is_valid_amount(amount) (return True if amount > 0).
# - [ ] 	•	Test by creating accounts, depositing money, changing bank name, and validating transactions.

class Bank :
    bank_name = "PYTHON BANK"
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    @classmethod
    def change_name(cls,name):
        cls.bank_name = name

    @staticmethod
    def is_valid(amount):
        return 0 < amount

kumar = Bank("Babu",1000)
print(kumar.bank_name)
print(kumar.owner)
print(kumar.balance)


Bank.change_name("JAVA BANK")
print(kumar.bank_name)
print(kumar.owner)
print(kumar.balance)

print(kumar.is_valid(100))