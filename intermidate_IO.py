# - [ ] 3.	CSV File – Writing & Reading
# 	•	Create a list of 3 students with Name, Age, Grade.
# 	•	Write this data into students.csv.
# 	•	Read the CSV file and print each student in the format:

# import csv
# students = [
#             ["Kumar",20,"A+" ],
#             ["Jahnavi",12,"B-"],
#             ["Siri",11,"D+"],
#             ]
# headers = ["name","age","grade"]
# filename = "students.csv"
# with open(filename, 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(headers)
#     for row in students:
#         writer.writerow(row)
#
# with open(filename, 'r', newline='') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for row in reader:
#         print(f" name :{row[0]} age: {row[1]} grade: {row[2]}")
#
#
# - [ ] 	4.	JSON File – Writing & Reading
# 	•	Create a dictionary representing a book: {"title": "Python 101", "author": "Alice", "pages": 200}
# 	•	Write it to book.json.
# 	•	Read the JSON file and print:
# "Title: Python 101, Author: Alice, Pages: 200"

# import json
#
#
# book_dict = [
#     {"Title":"Python 101" ,"Author":"Alice","pages":200},
#              {"Title":"OG" ,"Author":"Raju","pages":600},
#              {"Title":"RRR" ,"Author":"Ram","pages":700},
# ]
# filename = "book.json"
#
# with open(filename,"w") as f:
#     json.dump(book_dict,f,indent=4)
#
#
# with open(filename,"r") as f:
#     reload_books = json.load(f)
#
#     for book in reload_books:
#
#
#         print(f"Title: {book['Title']}   Author: {book['Author']}   pages: {book['pages']}")

# - [ ] 5.	Text & Exception Handling
# 	•	Ask the user for a filename.
# 	•	Try to read the file. If it doesn’t exist, print "File not found!" and ask again.
# 	•	If it exists, print the content and exit.


while True:
    file_name = input("Enter file name: ").strip()

    try:
        file = open(file_name, "r")

    except FileNotFoundError:
        print("File not found")
        continue

    else:
        data = file.read()
        print(data)
        file.close()
        break


# - [ ] CSV + JSON Conversion
# 	•	Read students.csv (from Question 3) and convert the data into JSON format.
# # 	•	Save the result into students.json.
#
# import csv
# import json
# students = [
#             ["Kumar",20,"A+" ],
#             ["Jahnavi",12,"B-"],
#             ["Siri",11,"D+"],
#             ]
# headers = ["name","age","grade"]
# filename = "students.csv"
# new_file = "students.json"
# with open(filename, 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(headers)
#     for row in students:
#         writer.writerow(row)
#
# with open(filename, 'r', newline='') as f:
#     reader = csv.DictReader(f)
#     data = list(reader)
# with open(new_file, 'w', newline='') as f:
#     json.dump(data, f, indent=4)
# with open(new_file, 'r', newline='') as f:
#     new_data = json.load(f)
    for row in new_data:
        print(f" name : {row['name']}, grade:  {row['grade']} ")


# - [ ] 7.	Binary – Save & Read Image
# 	•	Read an image file (example.png) in binary mode and save a copy as example_copy.png.
#

# file_name = "IMG20241215164027_BURST007_34261110.jpg"
# with open(file_name, "rb") as image_file:
#     data = image_file.read()
#
# with open("copy.JPG", 'wb') as f:
#     f.write(data)

