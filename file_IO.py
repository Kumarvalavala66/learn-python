# #1.	Text File – Writing & Reading
# 	# •	Write a program that asks the user to input 5 lines of text and saves them to notes.txt.
# 	# •	Then read the file and print its content.
#
# file = "notes.txt"
# with open(file,"w") as f:
#     for i in range(5):
#         string = input("Enter line : ")
#         f.write(string+"\n")
#
# with open(file,"r") as f:
#         data = f.read()
#         print(data)
#
#
# 	# 2.	Binary File – Writing & Reading
# 	# •	Convert a string "Hello Binary" into bytes and write it to binaryfile.bin.
# 	# •	Then read the binary file and print the content.
#
# string = b"Hello Binary"
# file_path = "C:\\Users\\\\Desktop\\notes.txt"
# with open(file_path, "wb") as file:
#     file.write(string)
#     print("File saved successfully")
# with open(file_path, "rb") as file:
#     data = file.read()
#     print(data)
#     print(data.decode())

# - [ ] 	3.	CSV File – Writing & Reading
# 	•	Create a list of 3 students with Name, Age, Grade.
# 	•	Write this data into students.csv.
# 	•	Read the CSV file and print each student in the format:
# "Name: Alice, Age: 25, Grade: A"

# import csv
#
# from urllib3.filepost import writer
#
# file_path = "students.csv"
# students = [["Alice",25,"A+"],
#             ["Bob",25,"B+"],
#             ["Charlie",25,"C+"],
#             ]
# with open(file_path,newline=" ") as f:
#     writer = csv.writer(f)
#     writer.writerows(students)
#     for row in students:
#         print(f"the {row[0]} is {row[1]} years old and he scored {row[2]}." )
