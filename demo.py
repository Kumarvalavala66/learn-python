# from basic_modules import Calculator
# while True:
#     try:
#         num1 = int(input("enter first number: "))
#         num2 = int(input("enter second number: "))
#     except ValueError:
#         print("please enter numeric value")
#         continue
#     else:
#         calculator = Calculator(num1, num2)
#         option = str(input("enter option add(+) or multiply (*): ")).strip()
#         while True:
#             match option:
#                 case "+":
#                     result = calculator.add()
#                     print(f"the sum of {num1} and {num2} is {result}")
#                     exit(0)
#                 case "*":
#                     result = calculator.multiply()
#                     print(f"the product of {num1} and {num2} is {result}")
#                     exit(0)
#                 case _:
#                     print("please enter correct option")
#                     continue
#
# #
# from basic_modules import Greeting
# name = input("What is your name? ")
# greet = Greeting(name)
# greet.greet()


# from my_



from my_packages import *
from my_packages import version

operation = Operation(10,20)
print(operation.add())
print(operation.subtract())

print("version  =  ",version)

stri = StringOperatons("hi there")
print(stri.lowercase())
print(stri.uppercase())