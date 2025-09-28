# # # #	1.	Write a program that asks the user for a number and prints its square.
# # # 	•	If the user enters something that is not a number, handle it with except.
# #
# #
# #
# #
# # try:
# #     number = int(input("Enter a number: "))
# # except ValueError:
# #     print("Invalid input")
# # else:
# #     print(f"the square of {number} is {number**2}")
# # finally:
# #     print("The program is done")
# #
# #
# # # 	2.	Write code that divides two numbers.
# # # 	•	If the denominator is 0, catch the error and print "Cannot divide by zero".
# #
# # def division(num1,num2):
# #     try:
# #         result = num1/num2
# #     except ZeroDivisionError:
# #         print("division by zero is not possible")
# #     else:
# #         print(f"the division of {num1} and {num2} is{result:.2f}")
# #     finally:
# #         print("finally the method  is finished")
# #
# # num1=int(input("enter the first number :"))
# # num2=int(input("enter the second number :"))
# # division(num1,num2)
# #
# #
# #
# # # 	3.	Open a file and read its contents.
# # # 	•	If the file doesn’t exist, handle it with FileNotFoundError.
# # name = str(input("Enter the name of the file: "))
# # try:
# #     with open (name,"r") as f:
# #         data = f.read()
# #
# # except FileNotFoundError:
# #     print(f"no file named '{name}'")
# #
# # else:
# #     print(data)
# #
# # finally:
# #     print("the method came to an end")
#
#
#
#
#
#
# 	# 4.	Create a program that:
# 	# •	Uses try to open a file.
# 	# •	Uses else to print "File opened successfully" if no error.
# 	# •	Uses finally to print "Execution finished" no matter what.
#
# name = input("enter your name of the file :")
# try:
#     with open (name,"r") as file:
#         file_contents = file.read()
# except FileNotFoundError:
#     print(f"{name} is not found")
# else:
#     print(f"{name}  opened successfully with no error.")
#
# finally:
#     print("execution is successful")
#
#
#
# 	# 5.	Ask the user for an index number, then try to access that index from a list.
# 	# •	If the index is out of range, handle it.
# 	# •	If it succeeds, print "Element found".
# 	# •	Always print "Program ended" at the end.
#
# new_list = [1,3,5,7,9,0,12,34]
# while True:
#     try:
#         idx = int(input("Enter the index : "))
#     except ValueError:
#         print("Please enter a number ")
#         continue
#     else:
#         try:
#             print(f"the value at that index is {new_list[idx]}")
#             break
#         except IndexError:
#             print("Index out of range")
#             continue
#     finally:
#             print("the execution is successful")
#
# # 6.	Write a calculator function that:
# 	# •	Accepts two numbers and an operator (+, -, *, /).
# 	# •	Raises an exception if the operator is invalid.
# 	# •	Catches division by zero separately
#
# def calculator():
#     while True:
#         try:
#             num1 = int(input("Enter the first number: "))
#             num2 = int(input("Enter the second number: "))
#         except ValueError:
#             print("Please enter a number.")
#             continue
#         else:
#             choice = input("enter operator (+,-,*,/,%): ").lower().strip()
#             match choice:
#                 case "+":
#                     print(f"{num1} + {num2} = {num1 + num2}")
#                     return num1 + num2
#                 case "-":
#                     print(f"{num1} - {num2} = {num1 - num2}")
#                     return num1 - num2
#                 case "*":
#                     print(f"{num1} * {num2} = {num1 * num2}")
#                     return num1 * num2
#                 case "/":
#                     try:
#                         num1/num2
#                     except ZeroDivisionError:
#                         print("Division by zero not possible.")
#                         continue
#                     else:
#                         print(f"{num1} / {num2} = {num1 / num2}")
#                 case "%":
#                     print(f"{num1} % {num2} = {num1 % num2}")
#                     return num1 % num2
#                 case _:
#                     print("Please enter a valid operator.")
#                     continue
#
#
#
# calculator()
