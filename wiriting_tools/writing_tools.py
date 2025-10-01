# - [ ] 5.	Create a package data_tools with modules for:
# 	•	Reading/writing JSON
# 	•	Reading/writing CSV
# 	•	In __init__.py, automatically import all functions
# 	•	Test it by writing a script that reads a CSV, converts it to JSON, and prints it.
import csv
import json

class WritingTools:
    def __init__(self,filename,data):
        self.filename = filename
        self.data = data

    def write_csv(self):
        with open(self.filename,'w') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)



    def read_csv(self):
        with open(self.filename,'r') as f:
            reader = csv.reader(f)
            self.data = list(reader)
            print(self.data)

    def write_json(self):
        with open(self.filename,'w') as f:
            json.dump(self.data,f,indent=4)

    def read_jsonl(self):
        with open(self.filename,'r') as f:
            json_data = json.load(f)
            print(json_data)

