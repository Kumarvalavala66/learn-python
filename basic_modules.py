# - [ ] Create a module calculator.py with functions add(a,b) and multiply(a,b).
# 	•	Import it in another file and test the functions.
# - [ ] 	2.	Create a module greetings.py with a function greet(name) that prints "Hello, <name>!".
# 	•	Import and call it from another file.

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def multiply(self):
        return self.num1 * self.num2

class Greeting:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}!")