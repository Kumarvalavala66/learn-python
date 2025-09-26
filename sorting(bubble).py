def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

try :
    array = []
    number = int(input("Enter a number: "))
    for _ in range(number):
        number1 = int(input("Enter a number: "))
        array.append(number1)
    double_array = bubble_sort(array)
    print(double_array)
except ValueError:
    print("Sorry, that's not a number")

