from tkinter import *
import random as r
root = Tk()
root.title("Colour changer")
root.geometry("600x600")




dictionary={"maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"}

def cc():
    random = r.randint(0, 7)
    print(random)
    

b1=Button(root,text="Click Me!!!", command= cc)
b1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.configure(background = cc() )
root.mainloop()