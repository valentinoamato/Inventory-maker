from tkinter import *      #Imports tkinter for the UI
from engine import start,read,save,path #Imports engine to interact with the JSON
import webbrowser          #Imports webbrowser to create a link

try:               #Tries to read the json file
    i=read()
except:            #If not possible
    start()        #Calls a function that creates the json file
                   #in which all the data will be stored

root = Tk()  #Creates the root window
root.title('Inventory-maker by Valentino Amato') #Sets the title
frame1 = Frame(root)   #Creates a frame in the root window
frame1.grid(row=5,column=0) #Places the frame


menu = 1   #Keeps track of what is being displayed
index = [None,None,None] #Keeps track of the user navigation
h=2      #Sets the height of the buttons
w=15     #Sets the width of the buttons
help=[   #Stores the help message
"To create a new inventory enter the name in the text-entry and press the 'New' button.",
"To change the name of an inventory select the inventory, enter the new name and press the 'Edit' button.",
"To delete an inventory select the inventory and press the 'Delete' button.",
"To see the items of a inventory select it and press the 'Enter' button.",
"To see the data of an item select it and press the 'Enter' button.",
"The 'Back' button goes to the previous page: Inventory <--- Item <--- Data.",
"The buttons 'New', 'Edit' and 'Delete' all work on Inventories, Items and data."
"The button 'Clear' cleans the text-entry.",
"Mutiple elements without or with equal name are not allowed.",
"\n",
f"To export the data simply copy the .json file located in {path}",
f"To import data replace the mentioned .json file with the one desired.",
"\n",
"For more information or to send feedback click on 'Github repository' in the down right corner."
]

def callback(url):  #Opens the given url in a web browser
    webbrowser.open_new(url)

def Start(menu):    #Starts the UI with all its components
    labels(menu)
    update()
    buttons()
    entry()


def New():   #Creates new elements and saves them in the JSON
    error = False 
    dct = read()#Reads the JSON and saves it in a variable

    if e.get(): #If there is an input in the text-entry
        if menu == 1: 
            if e.get() in dct.keys(): #If the text input was already saved
                labels("e1")          #Shows an error
                error=True            
            else:
                dct.update({e.get():{}})#Saves the new inventory
                save(dct)
        
        elif menu == 2:
            if e.get() in dct[index[0]].keys():#If the text input was already saved
                labels("e1")                   #Shows an error
                error=True
            else:
                dct[index[0]].update({e.get():[]})#Saves the new item
                save(dct)
        
        elif menu == 3:
            if e.get() in dct[index[0]][index[1]]:#If the text input was already saved 
                labels("e1")                      #Shows an error
                error=True 
            else:
                dct[index[0]][index[1]].append("-"+e.get())#Saves the new data
                save(dct)
        if not error:       #If there were no errors
            update()    #Updates the listbox with the changes
            labels(menu)    #Updates the labels with the changes
    else:
        labels("e2")

def Edit(): #Edits elements
    global index
    error = False
    dct = read()
    if e.get():
        if menu == 1:
            if e.get() in dct.keys():#If the text-input was already in the JSON
                labels("e1")         #Shows an error
                error=True
            else:
                dct[e.get()] = dct.pop(index[0])#Changes the name of a dictionary
                save(dct)
            index[0] = None
        elif menu == 2:
            if e.get() in dct[index[0]].keys():
                labels("e1")
                error=True
            else:
                dct[index[0]][e.get()] = dct[index[0]].pop(index[1])#Changes the name of an itam
                save(dct)
            index[1] = None
        elif menu == 3:
            if e.get() in dct[index[0]][index[1]]:
                labels("e1")
                error=True
            else:
                dct[index[0]][index[1]][index[2]] = e.get()#Changes the data of an item
                save(dct)
            index[2] = None
        if not error: #If there were no errors
            update()#Updates the listbox with the changes
            labels(menu)#Updates the labels with the changes
    else:
        labels("e2")
    # index = [None,None,None]

def Delete():   #Deletes the selected element 
    dct = read()
    if menu == 1:
        del dct[index[0]]#Deletes the selected inventory
        save(dct)        #Saves the changes in the JSON
    
    elif menu == 2:
        del dct[index[0]][index[1]]#Deletes the selected item
        save(dct)
    
    elif menu == 3:
        l = dct[index[0]][index[1]]#Deteles the selected data
        l.remove(l[index[2]])
        save(dct)
    update()#Updates the listbox with the changes
    labels(menu)#Updates the labels with the changes

def Enter():   #Changes the displayed information: Inventories-->Items-->Data
    global menu
    if menu == 1 and index[0]:#If the user is in menu 1 and there is an inventory selected
        menu +=1              
    if menu == 2 and index[1]:#If the user is in menu 2 and there is an item selected
        menu +=1
    clear()      #Destroys all the widgets of the UI except 'frame1'
    Start(menu)  #Starts the UI with all its widgets, in the desired menu

def Back():    #Changes the displayed information: Data-->Items-->Inventories
    global menu
    if menu == 2:
        menu -=1 #Goes back to inventories (menu 2-->menu 1) 
        index[0] = None #Deletes the previous selection of the user 
    if menu == 3:
        menu -=1 #Goes back to items (menu 3-->menu 2)
        index[1] = None #Deletes the previous selection of the user
    clear()      #Destroys all the widgets of the UI except 'frame1'
    Start(menu)  #Starts the UI with all its widgets, in the desired menu

def Help():
    def GoBack():#If the user presses the 'Go Back' button
        clear()    #Destroys all the widgets of the UI except 'frame1'
        Start(menu)#Starts the UI with all its widgets, in the previous menu
    clear()  #Destroys all the widgets of the UI except 'frame1'
    labels("h")#Displays 'help' in a label
    scrollbarlistbox(help) #Displays the help message in the listbox
    link1 = Label(frame1, text="Github repository", fg="blue", cursor="hand2") #Creates a label: 'Github repository'
    link1.pack(side = RIGHT) #Packs the label in frame1
    link1.bind("<Button-1>", lambda e: callback("https://github.com/valentinoamato/Inventory-maker"))#Binds the label to a function that opens the repo in a web browser
    space = Label(frame1,text="                                                                                                                                     ")
    #Creates a label for aesthetic purpose
    space.pack(side = RIGHT)
    goB = Button(frame1,text="Go Back",height= h, width=w,command=GoBack)#Creates a button that call a function
    goB.pack(side=RIGHT) #Packs the button

def update():  #Displays elements in the scrollbar depending the actual number of menu
    global menu 
    dct = read()
    if menu == 1:      
        scrollbarlistbox(dct.keys()) #Updates the listbox with all the inventories 

    if menu == 2:
        scrollbarlistbox(dct[index[0]].keys()) #Updates the listbox with all the items in an inventory

    if menu == 3:
        scrollbarlistbox(dct[index[0]][index[1]]) #Updates the listbox with all the data of an item in an inventory

def clear():#Destroys all the widgets of the UI except 'frame1'
    for widget in root.winfo_children():
        if str(widget) != ".!frame":
            widget.destroy()
    for widget in frame1.winfo_children():
        widget.destroy()




def scrollbarlistbox(data):  #Displays a scrollbar-listbox with the given list of elements 
    global index
    scrollbarV = Scrollbar(root) #Creates a vertical scrollbar
    
    scrollbarV.grid(row=1,column=1,sticky="ns") #Places the scrollbar

    scrollbarH = Scrollbar(root,orient=HORIZONTAL) #Creates a horizontal scrollbar
    
    scrollbarH.grid(row=2,column=0,sticky="we") #Places the scrollbar
    
    var = Variable(value=tuple(data)) #Creates a tuple out of the fuction argument(list)

    listbox = Listbox(  #Creates the listbox and sets the previous tuple as the variable to show
        root,
        listvariable=var,
        height=30,
        width=200,
        borderwidth=3

    )

    listbox.grid(row=1,column=0) #Places the listbox


    def items_selected(event): 
        if menu == 1: 
            index[0]=listbox.get(listbox.curselection()) #Saves the name of the selected inventory

        if menu == 2:
            index[1]=listbox.get(listbox.curselection()) #Saves the name of the selected item

        if menu == 3:
            index[2]=listbox.curselection()[0] #Saves the index of the selected data


    listbox.bind('<<ListboxSelect>>', items_selected) #Calls 'items_selected' when an item is selected in the listbox
    listbox.config(yscrollcommand = scrollbarV.set) #Allows the vertical scrollbar to move along with the listbox
    listbox.config(xscrollcommand = scrollbarH.set) #Allows the horizontal scrollbar to move along with the listbox
    
    scrollbarV.config(command = listbox.yview) #Allows the vertical scrollbar to move the listbox on the y axis
    scrollbarH.config(command = listbox.xview) #Allows the vertical scrollbar to move the listbox on the x axis


def labels(label): #Creates and displays the desired label
    ivt = index[0]   #Will save the name of the selected inventory 
    itm = index[1]   #Will save the name of the selected item 
    if index[0] and len(index[0]) > 70: #If there is an inventory selected and its name is longer than 70 characters
        ivt = ivt[0:70]+"..."           #Takes the first 70 characters of the name, adds an ellipsis and saves it in a variable
                                        #This is done to prevent the geometry of the UI from broking due to having to displays a large name
    if index[1] and len(index[1]) > 70:#Does the same as before but for an item name
        itm = itm[0:70]+"..."

    error = Label(root,text=f"                                                                                   ")#Clears/overwrites the error label (If there is one being displayed)
    error.grid(row=3,column=0,sticky="w")

    #Displays a different label depending of the argument ('label') received by the function
    if label == 1:  
        Heading = Label(root,text="You have the following inventories:")
        Heading.grid(row=0,column=0,sticky="w")
    elif label == 2:
        Heading = Label(root,text=f"Inventory {ivt} has the following items:")
        Heading.grid(row=0,column=0,sticky="w")
    elif label == 3:
        Heading = Label(root,text=f"Item {itm} in inventory {ivt} has the following data:")
        Heading.grid(row=0,column=0,sticky="w")
    elif label == "h":
        Heading = Label(root,text=f"Help: ")
        Heading.grid(row=0,column=0,sticky="w")
    elif label == "e1":
        error = Label(root,text=f"ERROR: Invalid text-input.")
        error.grid(row=3,column=0,sticky="w")
    elif label == "e2":
        error = Label(root,text=f"ERROR: Text-input required.")
        error.grid(row=3,column=0,sticky="w")


def buttons(): #Creates and places the button of the UI

    clearE = Button(frame1,text="Clear",height= h, width=w,command= lambda: entry(True)) #Clears the text-entry
    clearE.pack(side = RIGHT)

    space = Label(frame1,text="                                                ")#Aesthetic purpose
    space.pack(side = RIGHT)

    button1 = Button(frame1,text="New",height= h, width=w,command=New)#Creates a new: Inventory, Item Data
    button1.pack(side = LEFT)

    button2 = Button(frame1,text="Edit",height= h, width=w,command=Edit)#Edits an: Inventory name, Item name or Data
    button2.pack(side = LEFT)

    button3 = Button(frame1,text="Delete",height= h, width=w,command=Delete)#Deletes an: Inventory, Item or Data
    button3.pack(side = LEFT)

    space = Label(frame1,text="                                        ")#Aesthetic purpose
    space.pack(side = LEFT)

    button5 = Button(frame1,text="Help",height= h, width=w,command=Help)#Displays the help message
    button5.pack(side = RIGHT)

    space = Label(frame1,text="                                        ")#Aesthetic purpose
    space.pack(side = RIGHT)

    button5 = Button(frame1,text="Enter",height= h, width=w,command=Enter)#Changes the displayed information: Inventories-->Items-->Data
    button5.pack(side = LEFT)

    button6 = Button(frame1,text="Back",height= h, width=w,command=Back)#Changes the displayed information: Data-->Items-->Inventories
    button6.pack(side = LEFT)

def entry(clear=False): #Manages the text-entry
    global e
    if clear == False:
        e = Entry(root,width=200,borderwidth=3)#Creates the text-entry
        e.grid(row=4,column=0)#Places the text-entry
    else:
        e.delete(0,END)#Clears the text-entry
    labels(menu)#Updates the labels

Start(menu)#Starts the UI in menu 1
root.mainloop()#Runs the tkinter mainloop