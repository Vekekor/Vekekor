from tkinter import*
from time import sleep
root= Tk()
create_password2=StringVar()

create_name = StringVar()
create_password = StringVar()
root.geometry("300x350")

def toggle_password():
    global checkbutton
    if checkbutton.var.get():
        entry1['show'] = ""
    else:
        entry1['show'] = "*"
    if checkbutton.var.get():
        entry2['show'] = ""
    else:
        entry2['show'] = "*"

def different_passwords():
    if create_password.get() == create_password2.get():
        match = Label(root, text="The passwords seem to match")
        match.pack()
        match.after(1000, match.destroy)
    else:
         nomatch = Label(root,text=" The passwords don't match")
         nomatch.pack()
         nomatch.after(1000, nomatch.destroy)

def create_user():
    
    create_name.get()
    create_password.get()
    create_password2.get()
    different_passwords()
    
    
    

def text_to():
    print(create_password.get())
    entrY = Entry(root, textvariable=create_password)
    entry1 = entrY

    

    

Label(root, text="Create username").pack(pady=5)
Entry(root, textvariable=create_name).pack(pady=5)







Label(root, text="Create password").pack(pady=5)
entry1 = Entry(root, textvariable=create_password,show="*")
entry1.pack(pady=5)
Label(root, text="Confirm password").pack(pady=5)
entry2 = Entry(root, textvariable=create_password2,show="*")
entry2.pack(pady=0,padx=20)
entry1.default_show_val = entry1['show']
entry1['show'] = "*"
entry2.default_show_val = entry2['show']
entry2['show'] = "*"
checkbutton = Checkbutton(root,text="Show password",onvalue=True,offvalue=False,command=toggle_password)
checkbutton.var = BooleanVar(value=False)
checkbutton['variable'] = checkbutton.var
checkbutton.pack()




Button(root, command=create_user,text="Register").pack(pady=9)
root.mainloop()
