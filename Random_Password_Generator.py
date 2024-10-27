from tkinter import *
import tkinter as tk
import random
import string

root=Tk()
root.title("Random Password Generator by Anjishnu Bhowal")
root.geometry("470x500+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("Password Strength:")

def select():
    select = choice.get()

choice = IntVar()
R1 = Radiobutton(root, text="Poor", variable=choice, value=1, command=select).pack(anchor=CENTER)
R2 = Radiobutton(root, text="Average", variable=choice, value=2, command=select).pack(anchor=CENTER)
R3 = Radiobutton(root, text="Hard", variable=choice, value=3, command=select).pack(anchor=CENTER)
R4 = Radiobutton(root, text="Advanced", variable=choice, value=4, command=select).pack(anchor=CENTER)

labelchoice = Label(root)
labelchoice.pack()

lenlabel = StringVar()
lenlabel.set("password length")
lentitle = Label(root, textvariable=lenlabel).pack()

val=IntVar()
spinlength = Spinbox(root, from_=8, to_=24, textvariable=val, width=13)
spinlength.pack()

def password_window(password):
    password_window = Toplevel(root)
    password_window.title("Generated Password")
    password_window.geometry("300x100")
    
    password_label = Label(password_window, text="Generated Password:", font=("Arial", 12))
    password_label.pack(pady=10)

    password_display = Label(password_window, text=password, font=("Arial", 12, "bold"), fg="blue")
    password_display.pack(pady=5)

def callback():
    Isum.config(text=passgen())
    generated_password = passgen()
    password_window(generated_password)
passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3)
passgenButton.pack()
password=str(callback)

Isum=Label(root,text="")
Isum.pack(side=BOTTOM)

poor = string.ascii_uppercase+string.ascii_lowercase
average=string.ascii_lowercase+string.digits
hard = string.ascii_lowercase+string.ascii_uppercase+string.digits
advance = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

def passgen():
    if choice.get()==1:
        return"".join(random.sample(poor,val.get()))
    elif choice.get()==2:
        return"".join(random.sample(average,val.get()))
    elif choice.get()==3:
        return"".join(random.sample(hard,val.get()))
    elif choice.get()==4:
        return"".join(random.sample(advance,val.get()))
    
root.mainloop()
