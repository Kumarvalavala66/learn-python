# number=[]
# even_sum=0
# odd_sum=0
# n=int(input("enter the number of elements in list :")
# for i in range(0,n):
#     element=int(input(f"enter the number in list{i+1}:"))
#     number.append(element)
#     if(element%2==0):
#         even_sum+=element
#     else:
#         odd_sum+=element
#
# print(f"the total sum of odd nummbers is :{odd_sum}")
# print(f"the total sum of even nummbers is :{even_sum}")

number = []
even_sum = 0
odd_sum = 0

n = int(input("Enter the number of elements in list: "))

for i in range(0, n):
    element = int(input(f"Enter number {i+1}: "))
    number.append(element)
    if element % 2 == 0:
        even_sum += element
    else:
        odd_sum += element

print(f"The total sum of odd numbers is: {odd_sum}")
print(f"The total sum of even numbers is: {even_sum}")