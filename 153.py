from tkinter import *
import random

root=Tk()
root.title("Password Maker")
root.geometry("500x500")

label = Label(root)

array3d =[[["1","2","3","4","5","6"],["heads","tails"],["A","B","C","D","E","F","G","H"]]]
print(array3d)

def passGenerator():
    random1 = random.randint(0,5)
    random2 = random.randint(0,1)
    random3 = random.randint(0,7)
    
    character1 = array3d[0][0][random1]
    character2 = array3d[0][1][0]
    character3 = array3d[0][2][random3]
    label["text"] = character1 + "" + character2 + "" + character3
    
btn = Button(root, text = "New Password" ,command = passGenerator)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)



root.mainloop()