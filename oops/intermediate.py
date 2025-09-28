# import time
#
# def time_showing(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # start timer
#         result = func(*args, **kwargs)
#         end_time = time.time()    # end timer
#         elapsed = end_time - start_time
#         print(f"Execution time: {elapsed:.6f} seconds")
#         return result
#     return wrapper
#
# @time_showing
# def printing():
#     print("Hello World")
#     print("Thana kosame naa, pogare mari anigeynaaa")
#
# printing()


#Write a decorator that prints “Function started” before running and “Function ended” after running.


#
# def start_and_end(addition):
#     def wrapper(*args,**kwargs):
#         print("the process is started")
#         addition(*args,**kwargs)
#         print("the process is finished")
#     return wrapper
# @start_and_end
# def addition(num1,num2):
#     print(num1+num2)
#     return num1+num2
# num1 = int(input("enter the first number: "))
# num2 = int(input("enter the second number: "))
# addition(num1,num2)
#


#3.	Create a decorator that repeats a function 3 times.
#
# def greeting_more(greeting):
#     def wrapper():
#         for i in range(3):
#             greeting()
#     return wrapper
# @greeting_more
# def greeting():
#     print("Hello world how are you?")
#
# greeting()


  #Write a decorator that checks if the first argument of a function is positive, otherwise prints “Invalid input”.




#
# def checking(addition):
#     def wrapper(*args , **kwargs ):
#         if args[0] > 0:
#             return addition(*args, **kwargs)
#         else:
#             print("invalid")
#     return wrapper
#
#
# @checking
# def addition(num1,num2):
#     print("{} + {} = {}".format(num1, num2, num1+num2))
#     print("addition")
#     return num1+num2
#
# addition(2, 3)


