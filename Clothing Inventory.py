from tkinter import *
from tkinter import ttk
from tkinter import messagebox

Clothes = []

i_keme = 0

class Invent:
    def __init__(self,clothes,size,designer):
        self.clothes = clothes
        self.size = size
        self.designer = designer
    def getClothes(self):
        return self.clothes
    def getSize(self):
        return self.size
    def getDesigner(self):
        return self.designer
    
def clothes():
    global i_keme
    i_keme += 1 
    c1 = Invent(E1.get(),E2.get(),E3.get())
    Clothes.append(c1)
    messagebox.showinfo(" Add item","Successfuly Added!")
    tree.insert('', 'end', text=i_keme, values=(E1.get(),E2.get(), E3.get()))
    E1.delete(0, "end")
    E2.delete(0, "end")
    E3.delete(0, "end")

def delete_item():
    a = messagebox.askquestion("Delete Condition ","Proceed Deleting?")
    if a == "yes":
        del_selected = tree.selection()[0]
        tree.delete(del_selected)
    else:
        print(" ")
        
def update():
    del_selected = tree.selection()[0]
    tree.item(del_selected, text=i_keme, values=(E1.get(), E2.get(), E3.get()))
    E1.get()
    E2.get()
    E3.get()
    E1.delete(0, "end")
    E2.delete(0, "end")
    E3.delete(0, "end")

    
def Exit():
    C_window.destroy()
    

    

C_window = Tk()
C_window.title("Clothing Line Inventory")
C_window.configure(bg="#FF4300")
tree = ttk.Treeview(C_window,columns=("Clothes" ,"Size", "Artist"))
tree.grid(row=6, column=0, columnspan=4)
tree.heading('#0', text= "ID")
tree.heading('#1', text= "Clothes")
tree.heading('#2', text= "Size")
tree.heading('#3', text= "Artist")



Label (C_window, text= "Clothes' model",bg="#FF4300",fg="#fff").grid(row=1, padx=20, pady=10)
Label (C_window, text= "Size",bg="#FF4300", fg="#fff").grid(row=2, padx=20, pady= 10)
Label (C_window, text= "Designer", bg="#FF4300", fg="#fff").grid(row=3, padx=20, pady=10)


E1= Entry(C_window)
E2= Entry(C_window)
E3= Entry(C_window)

E1.grid(row= 1, column= 1, padx= 20, pady=10)
E2.grid(row=2, column= 1, padx= 20, pady= 10)
E3.grid(row=3, column=1, padx=20, pady=10)

b1 = Button(C_window, text="Add",bg="#FF4300",command=clothes)
b1.grid(row=4 , column=0, padx=20, pady= 10)
b2_del = Button(C_window, text="Delete",bg="#FF4300",command=delete_item)
b2_del.grid(row=4, column=1, padx=20, pady=10)
b3 = Button(C_window, text="Exit",bg="#FF4300", command=Exit)
b3.grid(row=4, column=2, padx=20, pady=10)
b4 = Button(C_window, text="Update",bg="#FF4300",  command=update)
b4.grid(row =4, column=3, padx=20, pady=10)



mainloop()

