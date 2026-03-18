# JSON-formatted string with json.dumps() #When you need JSON as a variable/string
# write them to files using json.dump() #When you need to save JSON to a file
# read JSON data from files with json.load() #When you need to read JSON from a file
#  parse JSON strings with json.loads()#	When you have JSON as a string variable #dict/list
#only double quotes and lower case for boolean
#converting data into the JSON format is referred to as serialization
#deserialization, involves decoding data from the JSON format back into a usable form within Python

# ********keys always must be string
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data) #save data in str/variable
print(json_string)  

dog_data = {
    "name" :"Frieda",
    "isDog" : True, #boolen with lowercase
    "Hobbies" : ["eating","sleeping","barking"], # this is called array wraped in []
    "age" : 8, #number
    "other" : {
      "work" : None, #None
      "home" : ["street", "India"]
    },
    "friends" : [
      {
        "name" : "phi",
        "Hobbies" : ["eating","sleeping","barking"]
      },
      {
        "name" : "Mit",
        "Hobbies" : ["eating","sleeping","barking"]
      }
    ]
  } #everything inside { object}

with open("serializing.json",mode="w",encoding = "utf-8") as f:
  json.dump(dog_data,f) #(object,file)
  
#deserialization
with open('serializing.json',mode="r",encoding = "utf-8") as f:
  data = json.load(f)
  print(data["name"])
  
print(type(data["other"]))
print(type(dog_data["other"]))

print("-----prettify json with python------")
#indent is used only for writing not reading with json.load will not work
with open("serializing.json", mode="w",encoding = "utf-8") as f:
  json.dump(dog_data,f,indent=2)

print(json.dumps(dog_data,indent=2)) #print prettified to terminal 


print("-------validation json--------")
# run this in terminal: python -m json.tool test/test.json test_new.json --indent 2