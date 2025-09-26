# Write a program to swap two numbers without using a third variable.
# from idlelib.replace import replace
from curses.ascii import isalpha

# arr = []
# num1= int(input("enter first number"))
# num2= int(input("enter second number"))
# arr.append(num1)
# arr.append(num2)
# print("the first number is" ,num1, " and the second number is",num2 )
# arr.reverse()
# print("the first number is", arr[0], " and the second number is",arr[1])




# Take a string input and print it in reverse.
# string = str(input("Enter a string: "))
# str_ = list(string)
# print("".join(reversed(str_)))



# 	Write a program to check if a number is even or odd.
# number = int(input("Enter a number: "))
# if number%2 == 0:
#     print("Even")
# else:
#     print("Odd")


# Take user input for name and age, then print:
# "Hello [name], you will turn 100 in the year [year]."

# try:
#    name = str(input("What is your name? "))
#    age = int(input("What is your age? "))
#    print(f"Hello, {name}! You are {age} yeas old. you will turn 100 in {100-age}years(if you are alive )")
# except ValueError:
#     print("Sorry, I didn't understand that.")



# 5.Print the multiplication table of a given number using a loop
# try:
#     number = int(input("Enter a number: "))
#     limit = int(input("Enter a limit: "))
#     for i in range(1, limit+1):
#         print(f"{number} x {i} = {number * i}")
#     # useing x for it ressembles cross
# except ValueError:
#     print("Invalid input")


#

#Write a program to check if a number is prime.
# try:
#     num = 0
#     number = int(input("Enter a number: "))
#     if number<0:
#         print("Sorry, you can't be less than zero")
#     elif number==0:
#         print("You can't be equal to zero")
#     else:
#         for i in range(3,number):
#             if number%i==0:
#                 num = 1
#
#         if num==1:
#             print("its not a prime  number")
#         else:
#             print("its prime number")
#
# except ValueError:
#     print("Sorry, you didn't enter a number")



#	Print all numbers from 1 to 100 divisible by 3 and 5.
# try:
#     limit = int(input("Enter a limit: "))
#     div_3_4 = []
#     for i in range(1,limit+1):
#         if i % 3 == 0 and i% 5 == 0:
#
#             div_3_4.append(str(i))
#     print(",".join(div_3_4))
# except ValueError:
#     print("Invalid input")
#



#Create a program that asks for 5 numbers and prints the largest.
# numbers = []
# for i in range(1, 5+1):
#     try:
#         num = int(input(f"enter {i} numbers: "))
#         numbers.append(num)
#     except ValueError:
#         print("invalid input")
#         num = int(input(f"enter {i} numbers: "))
#         numbers.append(num)
#         continue
# print(max(numbers))



 #Print the Fibonacci series up to n terms.
# try :
#     limit = int(input("Enter the limit: "))
#     num1= 0
#     num2= 1
#     f_series = [str(num1),str(num2)]
#
#     for x in range(1,limit+1):
#         sum1 = num1+num2
#         num1 = num2
#         num2 = sum1
#         f_series.append(str(sum1))
#     print(",".join(f_series))
#
# except ValueError:
#     print("Invalid input")
# try :
#     limit = int(input("enter "))
#     f_sec = [0,1]
#     for i in range(limit):
#         f_sec.append(f_sec[-1]+f_sec[-2])
#     print(",".join(map(str ,f_sec)))
# except ValueError :
#     print("ValueError")





# Guess the Number game: generate a random number 1–20, let the user guess until correct.
# import random
# number = random.randint(1,20)
# while True:
#     try:
#         user_input = int(input("Enter a number between 1 and 20: "))
#         if user_input == number:
#             print("Congratulations! You guessed it!")
#             break
#         elif user_input < number:
#             print("Sorry, that's too low!")
#             continue
#         elif user_input > number:
#             print("Sorry, that's too high!")
#             continue
#     except ValueError:
#         print("Sorry, that's not a number!")
#

  #Count the number of vowels in a string.
# vowels = ['a','e','i','o','u']
# count =0
# try:
#     string = str(input("enter string broh :")).lower()
#     list1 = [i for i in string if i in vowels]
#     print(len(list1))
# except ValueError:
#     print("enter a valid string")

# Write a program to count words in a sentence.
# string = input("Enter a string: ")
# a_list = list(string.split(" "))
# print(len(a_list))

#Remove all duplicate characters from a string.

# word1 = input("Enter a string: ")
# no_dub =set(word1)
# no_dub.discard(" ") #optional for removing spaces
# print(",".join(sorted(no_dub)))

#Find the most frequent character in a string.
# from collections import Counter
# word1 = str(input("Enter a string: "))
# arr = list(word1)
# counter = Counter(arr)
# max_freq = 0
# for char in counter:
#     if counter[char] > max_freq:
#         max_freq = counter[char]
#     for char in counter:
#         if counter[char] == max_freq:
#             print(char)
#             break


#Find the second largest number in a list.
# numbers = []
# for i in range(5):
#     number = int(input("enter the number: "))
#     if number not in numbers:
#         numbers.append(number)
# sort = sorted(numbers)
# print(sort[-2])

#Remove duplicates from a list while keeping order.
# arr = []
# for i in range(5):
#     anumber = int(input("Enter the number want to add  : "))
#     if anumber not in arr:
#         arr.append(anumber)
# print(arr)




#fizzbuzz
# for i in range(50+1):
#     result = "FizzBuzz" if i % 3 == 0 and i % 5 == 0  else "Buzz" if i % 5 == 0 else "Fizz" if i % 3 == 0 else i
#     print(result)




#with out using rev
# numbers = ["1","2","3","4","5","6","7","8","9"]
# print(numbers)
# for i in range(1,len(numbers)+1):
#     print(numbers[-i])

#with using rev or slicing
# numbers = []
# for i in range(10):
#     number = int(input("enter a number: "))
#     numbers.append(number)
# rev_numbers = numbers[::-1]
# print(rev_numbers)
# print(list(reversed(numbers)))
#


#pallandrom cheacker
# string = input("Enter a string: ")
# arr = list(string)
# rev_arr = list(reversed(arr))
# print("Yes, the string is a palindrome" if arr == rev_arr else  "NO, its not  string is a palindrome")

#vowels and consonents cheacker
# vowels = ['a', 'e', 'i', 'o', 'u']
# vowel_count =0
# consonant_count = 0
# string = input("Enter a string: ").lower()
# for char in string:
#         vowel_count += 1 if char in vowels else 0
#         consonant_count += 1 if char not in  vowels  and  char != " " else 0
#
# print("Number of vowels: ", vowel_count , " Number of consonants: ", consonant_count)
#

#fing unique element fromh string
# string = input("enter the string :").lower().strip()
# uniq = set(c for c in string if c!=' ')
# print(uniq)
#
# COUNTING
from collections import Counter
# arr = []
# char = input ("Enter a character: ").strip()
# for c in char:
#     arr = ["" if c== " " else c]
# print(arr)
string = str(input("enter a string :"))
arr = []
for char in string:
    arr.append(char if char != " "else "")
print("".join(max(Counter.arr)))

