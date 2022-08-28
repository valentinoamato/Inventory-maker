import os
import json
#Required libraries are imported

jsondict = {} #Creates a dictionary that will store the data of the inventory

path = f"{os.path.dirname(os.path.realpath(__file__))}\data.json"
#Creates a string with the path of the json file that will store all the data (data.json)

def start(): #Creates or opens the json file
  with open(path, 'w') as json_file: 
    json.dump(jsondict, json_file)
    
def save(data): #Saves the given dicctionary into the json file
    with open(path, 'w') as json_file: #Opens the json file in write mode
        json.dump(data, json_file)     #Saves the dicctionary into the json file 

def read(): #Returns the dicctionary in the json file
    with open(path, 'r') as json_file:#Opens the json file in read mode
        data = json.load(json_file)   #Saves the dicctionary of the json file in a local variable
    return data                       #Returns the variable


        
