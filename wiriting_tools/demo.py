from writing_tools import *


data = [ ["Kumar",20,"A+" ],
         ["Jahnavi",12,"B-"],
          ["Siri",11,"D+"]]

user_input = input("Enter what what format you want to write  (csv or json): ").lower().strip()
file_name = input('Enter file name: ')
writingtools  = WritingTools(file_name, data)
match user_input:
    case "csv":
        writingtools.write_csv()
        writingtools.read_csv()

    case "json":
        writingtools.write_json()
        writingtools.read_jsonl()

    case _:
        print("Invalid input")










