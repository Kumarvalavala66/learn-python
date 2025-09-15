import random
import time
MAX=10
MIN=3
NO_PROBLEMS = 12
operator = ('+', '-', '*',  '%')
def create_problems():
    left = random.randint(MIN, MAX)
    right = random.randint(MIN, MAX)
    symbol = random.choice(operator)

    equation = str(left) + symbol + str(right)
    # if symbol == "/":
    #     round(eval(equation), 2)
    #     return equation,eval(equation)
    # else:
    #     eval(equation)
    return equation, eval(equation)
print("do you want to play ::::::")
START_time = time.time()
print("----------------------------------------------------><----------------------------------------------------------")
for i in range(NO_PROBLEMS):
    question , answer = create_problems()
    while True:
        print(question)
        user_choice = input("Enter your answer: ")
        if user_choice ==  str(answer):
            break
        else:
            print("Wrong answer")
            continue
print("----------------------------------------------------><----------------------------------------------------------")
End_time=time.time()
total_time = End_time - START_time
print("you taken :", round(total_time ,2),"seconds")






