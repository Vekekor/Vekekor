from tkinter import *
from time import sleep
root = Tk()
windwo =  root.geometry("300x350")
name = StringVar()
password = StringVar()
def correct_username():
    if name.get() == "":
        return True
    elif name.get() != "":
        print("False")
def correct_password():
    if password.get() == "":
        return True
    elif password.get() !="":
        print("False")
getin = False
def check_if_bothCorrect():
    if correct_username() and correct_password() == True:
        print("Gaemoor")
            
    else:
        print("Try again")
     


Label(root, text="Enter username").pack(pady=5)
Entry(root, textvariable=name).pack(pady=5)

Label(root, text="Enter password").pack(pady=5)
Entry(root, textvariable=password,show="*").pack(pady=5)
Button(root, command=check_if_bothCorrect,text="Log in").pack(pady=9)


root.mainloop()
