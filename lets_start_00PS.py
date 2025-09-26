class Car:
    def __init__(self,model,year,colour,in_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.in_sale = in_sale
car1 = Car("BMW",1929,"WHITE",True)
if car1.in_sale :
    print("The car is in sale")
    print(car1.model)
    print(car1.year)
    print(car1.colour)
else:
    print("The car is not in sale")