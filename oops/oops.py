# 1.Animal Sounds Abstract Base
# Class: Animal with abstract method make_sound().
# •    Subclasses: Dog, Cat, Cow → eachimplements make_sound().
# # •    Create a list of animals and loop through them to call make_sound(
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     def __init__(self, name,colour):
#         self.name = name
#         self.colour = colour
#     @abstractmethod
#     def make_sound(self):
#         pass
# class Dog(Animal):
#     def __init__(self,name,colour):
#       super().__init__(name,colour)
#     def make_sound(self):
#         print("{} is barking btw dog is in {} colour".format(self.name,self.colour))
#
# class Cat(Animal):
#     def __init__(self,name,colour):
#       super().__init__(name,colour)
#     def make_sound(self):
#         print("{} is MEOW btw cat is in {} colour".format(self.name,self.colour))
#
# babu = Dog("BABU","BROWN")
# papa = Cat("PAPA","RED")
# babu.make_sound()
# papa.make_sound()
#

