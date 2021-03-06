import csv
import json
import trainingjsonfile

# Define The folder name
csvfile = "TrainingCSV/Templet.csv"

# Define the Folder name where you want to create all the JSON file.
importFolder="Intent/"

with open(csvfile, 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        trainingjsonfile.userSays(row)
        print(trainingjsonfile.userSays(row))
        
        if row[5]:
            with open(importFolder+row[0]+".json",'w') as f:
                json.dump(trainingjsonfile.defaultcontext(row), f, indent=2, ensure_ascii=False)
        else:
            with open(importFolder+row[0]+"_usersays_en.json", 'w') as f:
                json.dump(trainingjsonfile.userSays(row), f, indent=2, ensure_ascii=False)
            if row[3] and row[4] or row[3]:
                trainingjsonfile.outputOutputContext(row)
                print(trainingjsonfile.outputOutputContext(row))
                with open(importFolder+row[0]+".json", 'w') as f:
                    json.dump(trainingjsonfile.outputOutputContext(row), f, indent=2, ensure_ascii=False)
            elif row[4]:
                trainingjsonfile.outputContext(row)
                print(trainingjsonfile.outputContext(row))
                with open(importFolder+row[0]+".json", 'w') as f:
                    json.dump(trainingjsonfile.outputContext(row), f, indent=2, ensure_ascii=False)
            else:
                trainingjsonfile.noFollowup(row)
                with open(importFolder+row[0]+".json", 'w') as f:
                    json.dump(trainingjsonfile.noFollowup(row), f, indent=2, ensure_ascii=False)
