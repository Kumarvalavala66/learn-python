# # import numpy as np
# # import time
# # numbers = list(range(100_000_000))
# # start = time.time()
# # numbers = map(lambda x:x*2 , numbers)
# # print(f"for lists {time.time() - start :.5f} seconds ")
# #
# #

# string = "OPENAI2025"
# # new = string[-4:]
# # print(new)
# new = string.index("AI")
# print(new)

# string = "openai is great"
# print(string.title())

# def cube(num):
#     return num ** 3
# print(cube(5))
#
# def abc(a, b, c):
#     return (a + b + c)/3
# print(abc(1, 2, 3))

# def vower_counter(word):
#     count = 0
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     for char in word :
#         count += 1 if char in vowels else 0
#         return count
#
#
# string = input("Enter a string: ")
# print(vower_counter(string))

# # number = np.array(100_000_000)
# # start1 = time.time()
# # number =  number*2
# # print(f"for numpy {time.time() - start1:.5f} seconds ")
# #
# # import numpy as np
# # # import time
# # #
# # # # Python list + map
# # # numbers = list(range(1_000_000))
# # # start = time.time()
# # # result = list(map(lambda x: x * 2, numbers))
# # # print("map time:", time.time() - start)
# # #
# # # # NumPy array
# # arr = np.arange("A","B")
# # print(arr)
# #
# # results = arr * 2
# # print(results)
#
# # - [x] 1.	Create a NumPy array from the list [10, 20, 30, 40, 50] and print it.
# # - [x] 	2.	Create a 3x3 matrix of zeros and replace the center element with 5.
# # - [x] 	3.	Create an array of numbers from 1 to 20 and print only the even numbers.
# # - [X] 	4.	Generate a 1D array with 10 random integers between 0 and 100.
# # - [x] 	5.	Calculate the sum, mean, maximum, and minimum of the array [3, 6, 9, 12, 15].
#
# import numpy as np
#
# import random as rnd
#
# from numpy.ma.core import identity
#
# # numbers = np.array([10, 20, 30, 40, 50])
# # print(numbers)
#
# # arr = np.zeros((3,3),int)
# # arr[1,1] = 5
# # print(arr)
#
#
# #
# # arr = np.arange(1,21)
# # print(arr[arr%2==0])
# #
# # arr = np.random.randint(1,100 ,10)
# # print(arr)
# # #
# # arr = np.array([3, 6, 9, 12, 15])
# # mean = arr.mean()
# # sum_ = arr.sum()
# # max_ = arr.max()
# # min_= arr.min()
# # print(f"mean: {mean} and sum: {sum_} and max: {max_} and min: {min_} of array : {arr}")
# # - [x] Create a 4x4 identity matrix.
# # - [x] 	7.	Generate an array of 20 numbers evenly spaced between 0 and 5.
# # - [x] 	8.	Create a 3x3 matrix and extract the second column.
# # - [x] 	9.	Reshape a 1D array of 16 elements into a 4x4 matrix.
# # - [ ] 	10.	Create a 5x5 matrix with random numbers and replace all numbers greater than 0.5 with 1 and the rest with 0.

# identity_matrix = np.identity(4)
# print(identity_matrix)
# evenly = np.linspace(0, 5, 20)
# print(evenly)
# from operator import index


# import numpy as np
# array = np.array(
#     [[1, 2, 3],
#      [4 ,5 ,6],
#      [7 ,8 ,9],]
#     )
#
# print(array[:,1])


# import numpy as np
# array = np.linspace(1, 5, 20)
# print(array)
# print(array)

# import numpy as np
# array = np.arange(1,16+1).reshape(4,4)
# print(array)

# import numpy as np
# arr = np.random.randint(0.5,4 ,25).reshape(5,5)
# print(arr)
