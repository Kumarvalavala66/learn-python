#1.	Write a function that takes a string and returns the number of vowels in it
#
#
#
#
# #
# #
# def vower_counter(word):
#     vowel_count = 0
#     for letter in word:
#         vowel_count += 1 if letter in ['a','e','i','o','u'] else 0
#     return vowel_count
# word = str(input("Enter a word: ")).lower()
# print(vower_counter(word))
#
#
#
#
# def count_even(numbers):
#     even_count = 0
#     for number in numbers:
#         even_count += 1 if number % 2 == 0 else 0
#     return even_count
#
# option = int (input("enter how numbers you want add : "))
# for i in range(1,option+1):
#     number = int (input("enter number{} : ".format(i)))
#     numbers.append(number)
# counts = count_even(numbers)
# print(counts)
#
#
#
#
# #4.	Write a function that takes a string and reverses each word individually, keeping the word order.
#
# def reverser(words):
#    for word in words:
#        for letters in word:
#            new_word = word[::-1]
#            print(new_word)
#
# words = input("Enter a word: ")
# reverser(words)



# Create a function that returns the factorial of a number using recursion.

# def recursion(num):
#     if num == 0 or num == 1:
#
#         return 1
#
#     else:
#         return  num * recursion(num-1)
#
# print(recursion(5))

def get_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

numbers = []
n = int(input("How many numbers do you want to add? "))
for i in range(1, n+1):
    number = int(input(f"Enter number {i}: "))
    numbers.append(number)

evens = get_even_numbers(numbers)
print("Even numbers in the list:", evens)
