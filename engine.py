import os
import json
import re
#Required libraries are imported

jsondict = {"a":[],"b":{}} #Creates a dictionary that will store the data of the inventory
# "a" will store the names of the inventories in a list
# "b" will store the items in the inventories and their descriptions in a dicctionary

path = f"{os.path.dirname(os.path.realpath(__file__))}\data.json"
#Creates a string with the path of the json file that will store all the data (data.json)

def start(): #Creates or opens the json file
  with open(path, 'w') as json_file: 
    json.dump(jsondict, json_file)
    
def write(data,name): #Changes the value of a list in the json dictionary
    with open(path, 'r') as json_file:#Opens the json file in read mode
        i = json.load(json_file)#Saves the dicctionary of the json file in a local variable
        if name == "a":  #If name is equal to 'a'
            i["a"] = data  #The list 'a' is replaced by list 'data'
        else:            #If name is equal to 'b'
            i["b"] = data  #The list 'b' is replaced by list 'data'
            json.dump(i, json_file)
            #One of the lists in the json file ('a','b' or 'c'), depending on the value of 'name'
            #Was replaced by the list given in 'data'


def read(item): #Returns a specified data from the json file
    #The argument will be a letter followed by a number 
    with open(path, 'r') as json_file:#Opens the json file in read mode
        data = json.load(json_file)#Saves the dicctionary of the json file in a local variable

    if item == "a":   #If the item "a" is requested
        return data["a"]#It is returned as a list

    elif item == "b":   #If the item "b" is requested
        return data["b"]  #It is returned as a list
  
    else:             #If neither the item "a" or "b" was requested
        return data["c"]#Item "c" is returned as a list


def translate(arg,operation):#Uses regex to get values from a string
  #All the data of a item in the inventory is stored in a single string
  #This function gets the values from the string or makes the string from the values
    if operation == "encrypt":#If the operation is encrypt 
        a = ""                  
        for _ in arg:           #Iterates the values of the list
            a+=(_+"/*/")          #Saves the values as strings separated by "/*/"
        return a                #Returns the string

    if operation == "decrypt":#If the operation is decrypt
        return re.split("/\*/",arg)#Returns the values in the string
        
        
