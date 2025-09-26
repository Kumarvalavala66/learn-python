# - [ ] 1️⃣ Student Class
# 	•	Attributes: name, grades (list of numbers)
# 	•	Methods:
# 	•	add_grade(grade) → adds a grade to the list
# 	•	average_grade() → returns the average
# 	•	Task:
# 	•	Create a student object, add 5 grades, and print the average.
#
# ⸻
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#         print (f"Added {grade} to grades")
#
#     def average(self):
#         return sum(self.grades) / len(self.grades)
#
#
# raju = Student("Raj", [1, 1, 3, 4])
# raju.add_grade(1)
# raju.add_grade(2)
# average = raju.average()
# print(average)
#
#



# #- [ ] 2️⃣ Library Book Class
# 	•	Attributes: title, author, is_checked_out (bool)
# 	•	Methods:
# 	•	check_out() → sets is_checked_out = True
# 	•	return_book() → sets is_checked_out = False
# 	•	Task:
# 	•	Create a book object, check it out, then return it, and print status each time.
#
# class Library:
#     def __init__(self, title,author,is_checked_out):
#         self.title = title
#         self.author = author
#         self.is_checked_out = is_checked_out
#
#     def checkout(self):
#         if self.is_checked_out:
#             print("already checked out")
#             return
#         else:
#             self.is_checked_out = True
#             print("avilable for checkout ")
#     def return_book(self):
#         if self.is_checked_out:
#             self.is_checked_out = False
#             print("thanks for returning book")
#             return
#         else:
#             print("not returned yet")
#
# fire_and_blood = Library("Fire and Blood","R. R. Martin",True)
# fire_and_blood.checkout()
# fire_and_blood.return_book()

# - [ ] 3️⃣ Car with Fuel Consumption
# 	•	Attributes: brand, fuel (liters), mileage (km per liter)
# 	•	Methods:
# 	•	drive(distance) → reduces fuel based on distance and mileage
# 	•	refuel(amount) → adds fuel
# 	•	Task:
# 	•	Create a car with 20 liters and 10 km/l mileage
# 	•	Drive 50 km, print remaining fuel
# 	•	Refuel 10 liters, print new fuel level
# class Fuel_consumption:
#     def __init__(self,brand,fuel,mileage):
#         self.brand = brand
#         self.fuel = fuel
#         self.mileage = mileage
#     def drive(self,distance):
#         fuel_used = self.mileage * distance
#         fuel_remaining = fuel_used - self.fuel
#         print("fuel remaining ",fuel_remaining)
#
#
#
# car1 = Fuel_consumption("BMW",20,10)
# car1.drive(20)





#- [ ] 4️⃣ BankAccount with Transaction History
	# •	Attributes: name, balance, transactions (list)
	# •	Methods:
	# •	deposit(amount) → adds amount to balance + record in transactions
	# •	withdraw(amount) → subtracts amount + record in transactions
	# •	show_transactions() → prints all transactions
	# •	Task:
	# •	Create an account, make 3 deposits and 2 withdrawals, then print transactions


# class BankAccount:
#     def __init__(self, name, balance,transtions):
#         self.name = name
#         self.balance = balance
#         self.transtions = transtions
#
#     def deposit(self,amount) :
#         self.balance += amount
#         self.transtions.append(+amount)
#         print(f"{amount} is deposited into {self.name}")
#     def withdraw(self,amount) :
#         if amount > self.balance :
#             print(f"{amount} is no longer available")
#         else:
#             self.balance -= amount
#             self.transtions.append(-amount)
#             print(f"{amount} is credited from {self.name}")
#
# def customer():
#     kumar = BankAccount("Kumar", 10000, [])
#     kumar.deposit(100)
#     kumar.withdraw(200)
#     option = input("Which option would you see transition history (y/n):").lower().strip()
#     match option:
#         case "y":
#             print(kumar.transtions)
#         case "n":
#             print("thank you")
#         case _:
#             print("sorry that's not a valid option")
#
# customer()


# - [ ] 5️⃣ Mini Game: Player vs Enemy
# 	•	Classes: Player, Enemy
# 	•	Attributes: name, health, attack_power
# 	•	Methods:
# 	•	attack(target) → reduces target’s health by attacker’s attack power
# 	•	take_damage(amount) → reduces own health
# 	•	Task:
# 	•	Create 1 player and 2 enemies
# 	•	Simulate 1 round of attacks and print each character’s health
import random
class Human:
    def __init__(self, name,health,power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self):
        player_damage = random.randint(1,20)
        self.health -= player_damage
        print("{} attacks {}".format(self.name,self.health))
        return player_damage

    def taken_damage(self,taken_damage):
        self.health -= self.power
        print("{} damage taken {}".format(self.name,self.health))

class Player(Human):
    pass

class Enemy(Human):
    pass

kumar = Player("kumar",100,20)
babu = Enemy("babu",100,20)
while kumar.health > 0 and babu.health <= 100:
    dammage = kumar.attack()
    babu.taken_damage(dammage)
if kumar.health < 0:
    print("babu won")
if babu.health < 0:
    print("kumar won")

