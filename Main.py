from tkinter import *
from engine import start,read,save

# create the root window
root = Tk()
root.title('Listbox')
frame1 = Frame(root)
frame1.grid(row=4,column=0)


menu = 1   #Keeps track of what is being displayed
index = [None,None,None]
h=2
w=15

def New():   #Creates new elements
    dct = read()
    if menu == 1:
        dct.update({e.get():{}})
        save(dct)
    
    elif menu == 2:
        dct[index[0]].update({e.get():[]})
        save(dct)
    
    elif menu == 3:
        dct[index[0]][index[1]].append("-"+e.get())
        save(dct)
    update(menu)

def Edit(): #Edits elements
    dct = read()
    if menu == 1:
        dct[e.get()] = dct.pop(index[0])
        save(dct)
    
    elif menu == 2:
        dct[index[0]][e.get()] = dct[index[0]].pop(index[1])
        save(dct)

    elif menu == 3:
        dct[index[0]][index[1]][index[2]] = e.get()
        save(dct)
    update(menu)


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
    if menu < 3:
        menu +=1
    update(menu)
    labels(menu)

def Back():
    global menu
    if menu > 1:
        menu -=1
    update(menu)
    labels(menu)


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
        widget.destroy()

def clearEn():
    e.delete(0,END)

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
    if label == 1:
        label1 = Label(root,text="You have the following inventories:")
        label1.grid(row=0,column=0,sticky="w")
    elif label == 2:
        label2 = Label(root,text=f"Inventory {index[0]} has the following items:")
        label2.grid(row=0,column=0,sticky="w")
    elif label == 3:
        label3 = Label(root,text=f"Item {index[1]} in inventory {index[0]} has the following data:")
        label3.grid(row=0,column=0,sticky="w")

def test():
    print(index)

def buttons(menu):

    clearE = Button(frame1,text="Clear",height= h, width=w,command=clearEn)
    clearE.pack(side = RIGHT)

    button4 = Label(frame1,text="                                                ")
    button4.pack(side = RIGHT)

    button1 = Button(frame1,text="New",height= h, width=w,command=New)
    button1.pack(side = LEFT)

    button2 = Button(frame1,text="Edit",height= h, width=w,command=Edit)
    button2.pack(side = LEFT)

    button3 = Button(frame1,text="Delete",height= h, width=w,command=Delete)
    button3.pack(side = LEFT)

    button4 = Label(frame1,text="                                                                                                                         ")
    button4.pack(side = LEFT)

    button5 = Button(frame1,text="Enter",height= h, width=w,command=Enter)
    button5.pack(side = LEFT)

    button6 = Button(frame1,text="Back",height= h, width=w,command=Back)
    button6.pack(side = LEFT)


e = Entry(root,width=200,borderwidth=3)
e.grid(row=3,column=0)

labels(1)
buttons(1)
update(1)
root.mainloop()