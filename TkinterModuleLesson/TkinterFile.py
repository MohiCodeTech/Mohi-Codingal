from tkinter import *
# root = Tk()
# root.title("My first tkinter file")
# root.geometry("400x300")
# root.configure(bg ='lightblue')

# entry = Entry(root)
# entry.place(x = 75, y = 75)

# root.mainloop()

#Grid
# root = Tk()
# root.title = "Grid"
# def hello():
#     print("Your form has been submitted")

# label1 = Label(root, text="Username: ")
# label1.grid(row=0, column=0, padx=5, pady=5)

# entry1 = Entry(root)
# entry1.grid(row=0, column=1, padx=5, pady=5)

# label2 = Label(root, text = "Password")
# label2.grid(row=1, column=0, padx=5, pady=5)

# entry2 = Entry(root)
# entry2.grid(row=1, column=1, padx=5, pady=5)

# button = Button(root, text="Login", command=hello)
# button.grid(row=2, column=0,columnspan=2, padx=5, pady=5)

# root.mainloop()

# root = Tk()
# root.title("Submit form")
# root.geometry("250x150")

# Label(root, text="Username: ").grid(row=0, column=0, padx=9, pady=5)
# Label(root, text="Password: ").grid(row=1, column=0, padx=9, pady=5)

# username_Entry = Entry(root)
# username_Entry.grid(row=0, column=1, padx=10, pady=5)
# password_Entry = Entry(root)
# password_Entry.grid(row=1, column=1, padx=9, pady=5)

# def login():
#     username = username_Entry.get()
#     password = password_Entry.get()
#     print(f"Username is {username} and password is {password}")

# Button(root, text="Sign in", command=login).grid(row=2, column=0, columnspan=2, padx=9, pady=5)

# root.mainloop()

root = Tk()
root.title = "tkinter review"
root.geometry("550x150")

def data():
    print("Data submitted successfully")

label = Label(root, text="This isnt new you have been here multiple times", font=("Sans", 18))
entry = Entry(root, width=20)
button = Button(root,text= "Submit", command=data)

label.grid(row=0, column=0, padx=5, pady=3)
entry.grid(row=0, column=1, padx=5, pady=3)
button.grid(row=1, column=0, columnspan=2, padx=5, pady=3)

root.mainloop()