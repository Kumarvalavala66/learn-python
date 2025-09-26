from abc import ABC, abstractmethod
class Human(ABC):
    @abstractmethod
    def living(self):
        pass
    @abstractmethod
    def working(self):
        pass
    @abstractmethod
    def loving(self):
        pass
class Every(Human):
    def __init__(self, user):
        self.user = user

    def living(self):
        print("{} is living in kanakayalankha".format(self.user))

    def working(self):
        print("{} working as a engineer".format(self.user))

    def loving(self):
        print("{} is loving girl named someone ".format(self.user))

kumar = Every("kumar")
kumar.living()
kumar.working()
kumar.loving()