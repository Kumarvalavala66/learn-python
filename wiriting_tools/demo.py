from writing_tools import *
file_name = input('Enter file name: ')
data = [ ["Kumar",20,"A+" ],
         ["Jahnavi",12,"B-"],
          ["Siri",11,"D+"]]

writingtools  = WritingTools(file_name, data)
writingtools.write_csv()
writingtools.read_csv()



