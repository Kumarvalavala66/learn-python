import random
import string

print("----------->WELLCOME TO PASSWORD GENERATOR<--------------")
name = input("What is your name? ")
print("Hello, " + name + "!")


def pass_generator():
    while True:
        password = []
        alpha_count = int(input("Which elements do you choose from alphabet ? "))
        num_count = int(input("Which elements do you choose from numbers? "))
        others_count = int(input("Which elements do you choose from others? "))
        if alpha_count + num_count + others_count < 6:
            print("Sorry, your password is too short.")
            continue
        else:
            break
    while True:
        for i in range(alpha_count):
            password.append(random.choice(string.ascii_letters))
        for i in range(num_count):
            password.append(random.choice(string.digits))
        for i in range(others_count):
            password.append(random.choice(string.punctuation))
        if alpha_count + num_count + others_count != len(password):
            continue
        else:
            break
    random.shuffle(password)
    print("Your password is:-->     " + "".join(password)+"      <----")


pass_generator()