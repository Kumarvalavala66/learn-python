# Write a program to check if a number is even or odd.
from string import punctuation

#
# try:
#     number = int(input("Enter a number: "))
#     print("even " if number % 2 == 0 else "odd ")
# except ValueError:
#    print("Invalid input")
# #
# #--------------------------------------------------------
# # Take a string from the user and print it in reverse.
#
#
# string = input("Enter a string: ")
# print(string[::-1])
#
# #-------------------------------------------------------------------=
#
# # Find the largest of three numbers entered by the user.
#
# #
# arr = []
# for i in range(0,3):
#     number = int(input(f"enter number {i+1}: "))
#     arr.append(number)
# print(max(arr))
#
# #Count how many vowels are in a string.
#
# vowels = ['a', 'e', 'i', 'o', 'u']
# vowel_count = 0
# string = str(input("Enter a string: ")).lower()
# for char in string:
#     vowel_count += 1 if char in vowels else 0
# print(vowel_count)
#
# #Write a program that prints the multiplication table of a given number.
#
#
#
# try :
#     number = int(input("enter which table you want : "))
#     upto = int(input("enter how many steps you want : "))
#     if upto <= 0:
#         print("enter a positive number")
#     else:
#         for i in range(upto):
#             print(f"{number} x {i + 1} = {number * i}")
# except ValueError:
#     print("enter valid integer")


#
# #  Write a function that returns the factorial of a number.
# def factorial (number):
#     factorial = 1
#     for i in range (1, number + 1):
#         factorial = factorial * i
#
#     return factorial
#
# try :
#     number = int(input("Enter a number: "))
#     factorial = factorial(number)
#     print("The factorial of {} is {}".format(number, factorial))
# except ValueError:
#     print("Invalid input")
#
#
# # Given a list, remove all duplicates without using set().
#
#
# numbers = [1,2,3,4,2,4,6,7,8,9,9,8]
# new_numbers = []
# for number in numbers:
#     if number not in new_numbers:
#         new_numbers.append(number)
#
# print(new_numbers)
#
#
#
# #  Write a program that reads a file and counts how many words it has.
#
#
#
# with open("file.txt") as f:
#     words = f.read()
#     words = words.split(" ")
#     print(len(words))
#
#
#
#
# #  Implement a simple calculator using functions (+, -, *, /)
#
# try:
#     number1 = float(input("Please enter a first  number: "))
#     number2 = float(input("Please enter a second number: "))
#     option = input("enter symbol you want to perform the calculation: ").strip()
#     match option:
#         case "+":
#             result = number1 + number2
#         case "-":
#             result = number1 - number2
#         case "*":
#             result = number1 * number2
#         case "/":
#             result = number1 / number2
#         case _:
#             print("Invalid input")
#
#     print( ""  if option == "" else result )
# except ValueError:
#     print("Please enter a number.")
#
#
# #  Write a program to check if a string is a palindrome
# word  = input("Enter a word: ").lower().strip()
# if word == word[::-1]:
#     print(f"{word} is a palindrome")