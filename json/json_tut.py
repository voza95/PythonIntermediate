import json
# python            JSON
# dict              object
# list,tuple        array
# str               string
# int,float,long    number
# True              true
# False             false
# None              null

# Converting python dict into JSON format (Serilzation/Encoding)
person = {"name":"Jhon", "age":30, "city":"NY", "hasChildern":False, "titlels": ["engineer","programmer"]}

personJSON = json.dumps(person,indent=4,sort_keys=True)#,separators=(': ',"= ") optional
print(personJSON)

# Save it to file
# with open('person.json','w') as file:
    # json.dump(person,file,indent=4)

# dumps 's' is for string
# with statement in Python is used in exception handling to make the code cleaner and much more readable. 
# It simplifies the management of common resources like file streams. 
# (Simple means we don't need to add try-except)

# Convert JSON to python objects(Decoding/Deserilzation)
# person = json.loads(personJSON)
# print(person)

# Convert from JSON file
with open('person.json','r') as file:
    person = json.load(file)
print(person)