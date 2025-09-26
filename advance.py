from collections import Counter
string = input("Enter a string: ").lower().strip()
frequency = {}
for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)