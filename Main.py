import engine as e #Imports a python script that handles the data

try:               #Tries to read the json file
    i=e.read("a")
except:            #If it cant do it
    e.start()      #Calls a function that creates the json file
                   #in which all the data will be stored

print("\n"*100)    #Clears the terminal
print("Welcome to Inventory Maker!")
print("A simple program were you can manage inventories!")
print("\n"*3) 
#Prints a welcome message

def menu1():            #Main menu
    ivts = e.read("a")  #Gets all the names of the inventories
    if not ivts:        #If there are no inventories
        print("You currently have no inventories.")#Prints a message
        print("\n"*3)
        print("Enter 'c' to create an inventory.")
        print("Enter 'exit' to exit the program.")
        i=input("Operation: ")

        if i == "c":    #If the user wants to create a new inventory
            i = input("\n\nEnter the name of your new inventory\nOr enter 'b' to go back: ")#Saves the user input
            if i == "b": #If the user wants to go back
                menu1() #Goes back to the previous menu
            else:                     #If not
                ivts.append(i)#Adds the new inventory to the list
                print("Inventory created successfully!")
                e.write(ivts,"a")#Saves the list in the json
                menu1()  #Goes back to menu1
        
        if i == "exit":#If the user wants to exit the program
            print("\nThanks for using the program!")#Prints some messages
            print("Made by Valentino Amato")
            print("Check other projects: ")
            return                   #Exits the program
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
            menu2(i) #The menu2 is called with the number of the inventory that the user wants to see

    if i == "c":    #If the user wants to create a new inventory
        i = input("\n\nEnter the name of your new inventory\nOr enter 'b' to go back: ")#Saves the user input
        if i == "b": #If the user wants to go back
            menu1()   #Goes back to the previous menu
        else:        #If not
            ivts.append(i)#Adds the new inventory to the list
            print("Inventory created successfully!")
            e.write(ivts,"a")#Saves the list in the json
            menu1()  #Goes back to menu1

    if i == "r":    #If the user wants to rename an inventory
        i = input("\n\nEnter the number of the inventory\nOr enter 'b' to go back: ")#Saves the user i
        if i == "b": #If the user wants to go back
            menu1()   #Goes back to the previous menu
        else:        #If not
            j = input("\n\nEnter the new name: ")#Saves the user input
            ivts[int(i)-1] = j#Renames the selected
            print("Inventory renamed successfully!")
            e.write(ivts,"a")#Saves the list in the json
            menu1()  #Goes back to menu1

    if i == "d":    #If the user wants to create a new inventory
        i = input("\n\nEnter the number of the inventory\nOr enter 'b' to go back: ")#Saves the user input
        if i == "b": #If the user wants to go back
            menu1()   #Goes back to the previous menu
        else:        #If not
            ivts.remove(ivts[int(i)-1])#Deletes the selected inventory
            print("Inventory deleted successfully!")
            e.write(ivts,"a")#Saves the list in the json
            menu1()  #Goes back to menu1

    if i == "exit":#If the user wants to exit the program
        print("\nThanks for using the program!")#Prints some messages
        print("Made by Valentino Amato")
        print("Check other projects: ")
        return                   #Exits the program

def menu2(num):#Displays the information of an inventory
    ivts = e.read("b")  #Gets all the items of the inventory
    if not ivts:        #If the inventory is empty
        print("\n"*2)
        print("The selected inventory has no items.")#Prints a message
        print("\n"*2)
        print("Enter 'c' to create an inventory.")
        print("Enter 'exit' to exit the program.")
        i=input("Operation: ")

        if i == "c":    #If the user wants to create a new inventory
            i = input("\n\nEnter the name of your new inventory\nOr enter 'b' to go back: ")#Saves the user input
            if i == "b": #If the user wants to go back
                menu1() #Goes back to the previous menu
            else:                     #If not
                ivts.append(i)#Adds the new inventory to the list
                print("Inventory created successfully!")
                e.write(ivts,"a")#Saves the list in the json
                menu1()  #Goes back to menu1
        
        if i == "exit":#If the user wants to exit the program
            print("\nThanks for using the program!")#Prints some messages
            print("Made by Valentino Amato")
            print("Check other projects: ")
            return                   #Exits the program
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
            menu2(i) #The menu2 is called with the number of the inventory that the user wants to see

    if i == "c":    #If the user wants to create a new inventory
        i = input("\n\nEnter the name of your new inventory\nOr enter 'b' to go back: ")#Saves the user input
        if i == "b": #If the user wants to go back
            menu1()   #Goes back to the previous menu
        else:        #If not
            ivts.append(i)#Adds the new inventory to the list
            print("Inventory created successfully!")
            e.write(ivts,"a")#Saves the list in the json
            menu1()  #Goes back to menu1

    if i == "r":    #If the user wants to rename an inventory
        i = input("\n\nEnter the number of the inventory\nOr enter 'b' to go back: ")#Saves the user i
        if i == "b": #If the user wants to go back
            menu1()   #Goes back to the previous menu
        else:        #If not
            j = input("\n\nEnter the new name: ")#Saves the user input
            ivts[int(i)-1] = j#Renames the selected
            print("Inventory renamed successfully!")
            e.write(ivts,"a")#Saves the list in the json
            menu1()  #Goes back to menu1

    if i == "d":    #If the user wants to create a new inventory
        i = input("\n\nEnter the number of the inventory\nOr enter 'b' to go back: ")#Saves the user input
        if i == "b": #If the user wants to go back
            menu1()   #Goes back to the previous menu
        else:        #If not
            ivts.remove(ivts[int(i)-1])#Deletes the selected inventory
            print("Inventory deleted successfully!")
            e.write(ivts,"a")#Saves the list in the json
            menu1()  #Goes back to menu1

    if i == "exit":#If the user wants to exit the program
        print("\nThanks for using the program!")#Prints some messages
        print("Made by Valentino Amato")
        print("Check other projects: ")
        return                   #Exits the program











menu1()    #Starts the program in the main menu
