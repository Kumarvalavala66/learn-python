class Human :
    height:float
    age:int
    weight:float
    name:str
    def show_details(self):
        name = str(input("Name: "))
        age = int(input("Age: "))
        weight = float(input("Weight: "))
        height = float(input("Height: "))
        print(f"Name: {name}\nAge: {age}\nWeight: {weight}\nHeight: {height}")


obj1 = Human()
obj2 = Human()
obj1.show_details()
obj2.show_details()
