import engine as e #Imports a python script that handles the data

try:               #Tries to read the json file
    i=e.read()
except:            #If it cant do it
    e.start()      #Calls a function that creates the json file
                   #in which all the data will be stored

print("\n"*100)    #Clears the terminal
print("Welcome to Inventory Maker!")
print("A simple program were you can manage inventories!")
print("\n"*3) 
#Prints a welcome message

def menu1():            #Main menu
    dct = e.read()           #Reads the json and saves it in a variable
    ivts = list(dct.keys())  #Gets all the names of the inventories
    if not ivts:             #If there are no inventories
        print("You currently have no inventories.")#Prints a message
        print("\n"*3)
        print("Enter 'c' to create an inventory.")
        print("Enter 'exit' to exit the program.")
        i=input("Operation: ")

        if i == "c":    #If the user wants to create a new inventory
            i = input("\n\nEnter the name of your new inventory\nOr enter 'b' to go back: ")#Saves the user input
            if i == "b": #If the user wants to go back
                menu1() #Goes back to the previous menu

            else:
                print("Inventory created successfully!")
                dct.update({i:{}})#Creates a new inventory with the given name
                e.save(dct)#Saves the changes
                menu1()  #Goes back to menu1
        
        elif i == "exit":#If the user wants to exit the program
            exit()

    else:               #If there are inventories
        print(f"You have {len(ivts)} inventories: ")#Prints a message

        for i,j in enumerate(ivts):#Prints all the inventories
            print(f"\n{i+1}. {j}")
    print("\n"*3)
    print("Enter 's' to see an inventory.")
    print("Enter 'c' to create an inventory.")
    print("Enter 'r' to rename an inventory.")
    print("Enter 'd' to delete an inventory.")
    print("Enter 'exit' to exit the program.")
    i=input("Operation: ")

    if i == "s":    #If the user wants to see a new inventory
        i = input("\n\nEnter the number of the inventory\nOr enter 'b' to go back: ") #Opens the desired inventory in the menu 2
        if i == "b": #If the user wants to go back
            menu1()   #Goes back to the previous menu
        else:        #If not
            menu2(ivts[int(i)-1]) #The menu2 is called with the number of the inventory that the user wants to see

    elif i == "c":    #If the user wants to create a new inventory
        i = input("\n\nEnter the name of your new inventory\nOr enter 'b' to go back: ")#Saves the user input
        if i == "b": #If the user wants to go back
            menu1() #Goes back to the previous menu
        elif i in ivts:                     #If the name given is in use
            print("\n"*2)
            print("ERROR: The name given is already in use!")
            input("Press any key to continue.")
            menu1()
        else:                               #If any of the above
            print("Inventory created successfully!")
            dct.update({i:{}})#Creates a new inventory with the given name
            e.save(dct)       #Saves the changes
            menu1()           #Goes back to menu1
        
    elif i == "r":    #If the user wants to rename an inventory
        i = input("\n\nEnter the number of the inventory\nOr enter 'b' to go back: ")#Saves the user input
        if i == "b": #If the user wants to go back
            menu1()   #Goes back to the previous menu
        else:        #If not
            j = input("\n\nEnter the new name: ")#Saves the user input
            if j in ivts:                     #If the given name is in use
                print("\n"*2)
                print("ERROR: The name given is already in use!")
                input("Press any key to continue.")
                menu1()#Goes back to menu 1
            # ivts[int(i)-1] = j#Renames the selected
            print("Inventory renamed successfully!")
            dct[j] = dct.pop(ivts[int(i)-1])#Renames an inventory
            e.save(dct)#Saves the changes
            menu1()  #Goes back to menu1

    elif i == "d":    #If the user wants to delete an inventory
        i = input("\n\nEnter the number of the inventory\nOr enter 'b' to go back: ")#Saves the user input
        if i == "b": #If the user wants to go back
            menu1()   #Goes back to the previous menu
        else:        #If not
            del dct[ivts[int(i)-1]]#Deletes the selected inventory
            print("Inventory deleted successfully!")
            e.save(dct)#Saves the changes
            menu1()  #Goes back to menu1

    elif i == "exit":#If the user wants to exit the program
        exit()

def menu2(ivt):#Displays the information of an inventory
    print("\n"*3)
    print(f"You are now in the following inventory: {ivt}")
    dct = e.read()#reads the json
    itms = list(dct[ivt].keys())  #Gets all the items in the inventory
    if not itms:                  #If there are no items
        print("There are no items.")#Prints a message
        print("\n"*3)
        print("Enter 'c' to create a new item.")
        print("Enter 'exit' to exit the program.")     
        print("Enter 'b' to go back.")     
        i=input("Operation: ")

        if i == "c":    #If the user wants to create a new item
            i = input("\n\nEnter the name of the new item\nOr enter 'b' to go back: ")#Saves the user input
            if i == "b": #If the user wants to go back
                menu2(ivt) #Goes back to the previous menu

            else:
                print("Item created successfully!")
                dct[ivt].update({i:None}) #Creates a new item with the given name
                e.save(dct)#Saves the changes
                menu2(ivt)  #Goes back to menu 2
        
        elif i == "exit":#If the user wants to exit the program
            exit()

        elif i == "b":#If the user wants to go back
            menu1()

    else:               #If there are inventories
        print(f"There are {len(itms)} items in your inventory: ")#Prints a message

        for i,j in enumerate(itms):#Prints all the inventories
            print(f"\n{i+1}. {j}")
    print("\n"*3)
    print("Enter 's' to see an item.")
    print("Enter 'c' to create a new item.")
    print("Enter 'r' to rename an item.")
    print("Enter 'd' to delete an item.")
    print("Enter 'b' to go back.")
    print("Enter 'exit' to exit the program.")
    i=input("Operation: ")

    if i == "s":    #If the user wants to see a new inventory
        i = input("\n\nEnter the number of the item\nOr enter 'b' to go back: ") #Opens the desired inventory in the menu 2
        if i == "b": #If the user wants to go back
            menu1()   #Goes back to the previous menu
        else:        #If not
            menu2(i) #The menu2 is called with the number of the inventory that the user wants to see

    elif i == "c":    #If the user wants to create a new inventory
        i = input("\n\nEnter the name of the new item\nOr enter 'b' to go back: ")#Saves the user input
        if i == "b": #If the user wants to go back
            menu2(ivt) #Goes back to the previous menu
        elif i in itms:                     #If the given name is in use
            print("ERROR: The name given is already in use!")
            input("Press any key to continue.")
            menu2(ivt)
        else:
            print("Item created successfully!")
            dct[ivt].update({i:None})#Creates a new item with the given name
            e.save(dct)#Saves the changes
            menu2(ivt)  #Goes back to menu 2
        
    elif i == "r":    #If the user wants to rename an inventory
        i = input("\n\nEnter the number of the item\nOr enter 'b' to go back: ")#Saves the user input
        if i == "b": #If the user wants to go back
            menu2(ivt)   #Goes back to the previous menu
        
        else:        #If not
            j = input("\n\nEnter the new name: ")#Saves the user input
            if j in itms:                     #If the name is in use
                print("ERROR: The name given is already in use!")
                input("Press any key to continue.")
                menu2(ivt)
            print("Inventory renamed successfully!")
            dct[ivt][j] = dct[ivt].pop(itms[int(i)-1])#Renames the selected item
            e.save(dct)#Saves the changes
            menu2(ivt)  #Goes back to menu 2

    elif i == "d":    #If the user wants to delete an inventory
        i = input("\n\nEnter the number of the inventory\nOr enter 'b' to go back: ")#Saves the user input
        if i == "b": #If the user wants to go back
            menu2(ivt)   #Goes back to the previous menu
        else:        #If not
            del dct[ivt][itms[int(i)-1]]#Deletes the selected inventory
            print("Inventory deleted successfully!")
            e.save(dct)#Saves the changes
            menu2(ivt)  #Goes back to menu 2
    elif i == "b":
        menu2(ivt)

    elif i == "exit":#If the user wants to exit the program
        exit()
def exit():
    print("\nThanks for using the program!")#Prints some messages
    print("Made by Valentino Amato")
    print("Check other projects: https://github.com/valentinoamato")




menu1()    #Starts the program in the main menu
