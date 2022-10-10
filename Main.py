from tkinter import *
from engine import start,read,save
import webbrowser

try:               #Tries to read the json file
    i=read()
except:            #If it cant do it
    start()        #Calls a function that creates the json file
                   #in which all the data will be stored


# create the root window
root = Tk()
root.title('Inventory-maker by Valentino Amato')
frame1 = Frame(root)
frame1.grid(row=5,column=0)


menu = 1   #Keeps track of what is being displayed
index = [None,None,None]
h=2
w=15
help=[
"To create a new inventory enter the name in the text-entry and press the 'New' button.",
"To change the name of an inventory select the inventory, enter the new name and press the 'Edit' button.",
"To delete an inventory select the inventory and press the 'Delete' button.",
"To see the items of a inventory select it and press the 'Enter' button.",
"To see the data of an item select it and press the 'Enter' button.",
"The 'Back' button goes to the previous page: Inventory <--- Item <--- Data.",
"The buttons 'New', 'Edit' and 'Delete' all work on Inventories, Items and data."
"The button 'Clear' cleans the text-entry.",
"Mutiple elements without or with equal name are not allowed."

]

def callback(url):
    webbrowser.open_new(url)

def Start(menu):
    labels(menu)
    update(menu)
    buttons()
    entry()


def New():   #Creates new elements
    error = False
    dct = read()

    if e.get():
        if menu == 1:
            if e.get() in dct.keys():
                labels("e1")
                error=True
            else:
                dct.update({e.get():{}})
                save(dct)
        
        elif menu == 2:
            if e.get() in dct[index[0]].keys():
                labels("e1")
                error=True
            else:
                dct[index[0]].update({e.get():[]})
                save(dct)
        
        elif menu == 3:
            if e.get() in dct[index[0]][index[1]]:
                labels("e1")
                error=True
            else:
                dct[index[0]][index[1]].append("-"+e.get())
                save(dct)
        if not error:
            update(menu)
            labels(menu)
    else:
        labels("e2")

def Edit(): #Edits elements
    error = False
    dct = read()
    if e.get():
        if menu == 1:
            if e.get() in dct.keys():
                labels("e1")
                error=True
            else:
                dct[e.get()] = dct.pop(index[0])
                save(dct)
        
        elif menu == 2:
            if e.get() in dct[index[0]].keys():
                labels("e1")
                error=True
            else:
                dct[index[0]][e.get()] = dct[index[0]].pop(index[1])
                save(dct)

        elif menu == 3:
            if e.get() in dct[index[0]][index[1]]:
                labels("e1")
                error=True
            else:
                dct[index[0]][index[1]][index[2]] = e.get()
                save(dct)
        if not error:
            update(menu)
            labels(menu)
    else:
        labels("e2")

def Delete():   #Deletes the selected element 
    dct = read()
    if menu == 1:
        del dct[index[0]]
        save(dct)
    
    elif menu == 2:
        del dct[index[0]][index[1]]
        save(dct)
    
    elif menu == 3:
        l = dct[index[0]][index[1]]
        l.remove(l[index[2]])
        save(dct)
    update(menu)
    labels(menu)

def Enter():
    global menu
    print(menu,index)
    if menu == 1 and index[0]:
        menu +=1
    if menu == 2 and index[1]:
        menu +=1
    clear()
    Start(menu)

def Back():
    global menu
    if menu == 2:
        menu -=1
        index[0] = None
    if menu == 3:
        menu -=1
        index[1] = None
    clear()
    Start(menu)

def Help():
    def GoBack():
        clear()
        Start(menu)
    clear()
    labels("h")
    scrollbarlistbox(help)
    # frame2 = Frame(root)
    # frame2.grid(row=5,column=1)
    link1 = Label(frame1, text="Github repository", fg="blue", cursor="hand2")
    link1.pack(side = RIGHT)
    link1.bind("<Button-1>", lambda e: callback("https://github.com/valentinoamato/Inventory-maker"))
    button4 = Label(frame1,text="                                                                                                                                     ")
    button4.pack(side = RIGHT)
    goB = Button(frame1,text="Go Back",height= h, width=w,command=GoBack)
    goB.pack(side=RIGHT)

def update(n):  #Displays new elements in the scrollbar
    global menu 
    dct = read()
    if menu == 1:
        scrollbarlistbox(dct.keys())

    if menu == 2:
        scrollbarlistbox(dct[index[0]].keys())

    if menu == 3:
        scrollbarlistbox(dct[index[0]][index[1]])

def clear():
    for widget in root.winfo_children():
        if str(widget) != ".!frame":
            widget.destroy()
    for widget in frame1.winfo_children():
        widget.destroy()




def scrollbarlistbox(data):  #Displays a scrollbar-listbox with the given list of elements 
    global index
    scrollbarV = Scrollbar(root)
    

    scrollbarV.grid(row=1,column=1,sticky="ns")


    scrollbarH = Scrollbar(root,orient=HORIZONTAL)
    

    scrollbarH.grid(row=2,column=0,sticky="we")
    



    var = Variable(value=tuple(data))

    listbox = Listbox(
        root,
        listvariable=var,
        height=40,
        width=200,
        borderwidth=3

    )

    listbox.grid(row=1,column=0)


    def items_selected(event):
        if menu == 1:
            index[0]=listbox.get(listbox.curselection())

        if menu == 2:
            index[1]=listbox.get(listbox.curselection())

        if menu == 3:
            index[2]=listbox.curselection()[0]


    listbox.bind('<<ListboxSelect>>', items_selected)
    listbox.config(yscrollcommand = scrollbarV.set)
    listbox.config(xscrollcommand = scrollbarH.set)
    
    scrollbarV.config(command = listbox.yview)
    scrollbarH.config(command = listbox.xview)    


def labels(label):
    ivt = index[0]
    itm = index[1]
    if index[0] and len(index[0]) > 70:
        ivt = ivt[0:70]+"..."
    if index[1] and len(index[1]) > 70:
        itm = itm[0:70]+"..."

    error = Label(root,text=f"                                                                                   ")
    error.grid(row=3,column=0,sticky="w")

    if label == 1:
        label1 = Label(root,text="You have the following inventories:")
        label1.grid(row=0,column=0,sticky="w")
    elif label == 2:
        label1 = Label(root,text=f"Inventory {ivt} has the following items:")
        label1.grid(row=0,column=0,sticky="w")
    elif label == 3:
        label1 = Label(root,text=f"Item {itm} in inventory {ivt} has the following data:")
        label1.grid(row=0,column=0,sticky="w")
    elif label == "h":
        label1 = Label(root,text=f"Help: ")
        label1.grid(row=0,column=0,sticky="w")
    elif label == "e1":
        error = Label(root,text=f"ERROR: Invalid text-input.")
        error.grid(row=3,column=0,sticky="w")
    elif label == "e2":
        error = Label(root,text=f"ERROR: Text-input required.")
        error.grid(row=3,column=0,sticky="w")



    

def test():
    print(index)

def buttons():

    clearE = Button(frame1,text="Clear",height= h, width=w,command= lambda: entry(True))
    clearE.pack(side = RIGHT)

    button4 = Label(frame1,text="                                                ")
    button4.pack(side = RIGHT)

    button1 = Button(frame1,text="New",height= h, width=w,command=New)
    button1.pack(side = LEFT)

    button2 = Button(frame1,text="Edit",height= h, width=w,command=Edit)
    button2.pack(side = LEFT)

    button3 = Button(frame1,text="Delete",height= h, width=w,command=Delete)
    button3.pack(side = LEFT)

    button4 = Label(frame1,text="                                        ")
    button4.pack(side = LEFT)
    # button4 = Label(frame1,text="                                                                                                                         ")
    # button4.pack(side = LEFT)
    button5 = Button(frame1,text="Help",height= h, width=w,command=Help)
    button5.pack(side = RIGHT)

    button4 = Label(frame1,text="                                        ")
    button4.pack(side = RIGHT)

    button5 = Button(frame1,text="Enter",height= h, width=w,command=Enter)
    button5.pack(side = LEFT)

    button6 = Button(frame1,text="Back",height= h, width=w,command=Back)
    button6.pack(side = LEFT)

def entry(clear=False):
    global e
    if clear == False:
        e = Entry(root,width=200,borderwidth=3)
        e.grid(row=4,column=0)
    else:
        e.delete(0,END)
    labels(menu)

Start(menu)
root.mainloop()