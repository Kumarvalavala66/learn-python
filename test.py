
# def is_anagram(str1, str2):
#   str1 = list(str1)
#   str2 = list(str2)
#   if sorted(str1) == sorted(str2):
#     print("Anagram" )
#   else:
#     print(" not Anagram")
#
# word1 = input("Enter first word :")
# word2 = input("Enter second word :")
# is_anagram(word1,word2)

# Write a program that prints all even Fibonacci numbers less than 100.

# ## Write a program that prints all even Fibonacci numbers less than 100.
# def even_fibonacci(num):
#   print("0\n1")
#   num1 = 0
#   num2 = 1
#   while num2 <= num:
#     if num2 % 2 == 0 :
#         print(num2)
#     num1,num2 = num2,num1+num2
# even_fibonacci(100)

#Given a dictionary d = {'a':1,'b':2,'c':3}, create a new dictionary where values are doubled using dictionary comprehension.
# new_dict = {'a':1,'b':2,'c':3}
# for k,v in new_dict.items():
#     new_dict[k] = v*2
# print(new_dict)
#Write a list comprehension that returns the cubes of all numbers from 1 to 10 that are divisible by 2.
# new_list = [i**3 for i in range(10) if i%2==0]
# print(new_list)

#-Given a set s = {1,2,3,4,5}, remove all elements less than 3 without using a loop.
s = {1, 2, 3, 4, 5}
to_remove = {1,2,3}

new_set = s - to_remove
print(new_set)