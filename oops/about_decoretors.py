



def before_working(working):
    def wrapper():
        print("I am before working")
        working()
        print("I am after working")
    return wrapper


@before_working
def working():
    print("I am working")





working()


