from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# root = Tk()
# root.title("First window")
# root.geometry("200x200")

# def msg():
#     messagebox.showwarning("Alert!", "Malware present in device")

# button = Button(root, text="Scan for malware", command=msg)
# button.place(x=40, y=80)

# root.mainloop()

root = Tk()
root.title("Main window")
root.geometry("400x400")

def show_image():
    img_window = Toplevel(root)
    img_window.title("image window")

    img = Image.open("normal.png")
    img = img.resize((600, 400))
    img_tk = ImageTk.PhotoImage(img) 

    img_label = Label(img_window, image = img_tk)
    img_label.image = img_tk
    img_label.pack()

def show_message():
    messagebox.showinfo("This is a message from an old friend")
    messagebox.showwarning("Its from your crazy ex")

def open_top_window():
    top = Toplevel(root)
    top.title("Secondary window")
    top.geometry("250x150")
    label1 = Label(top, text="New label", font=("Arial",12 ))
    label1.place(x=40, y=60)

btn1 = Button(root,text="Show image window", command=show_image)
btn1.pack(pady=10)

btn2 = Button(root,text="Show message box", command=show_message)
btn2.pack(pady=10)

btn3 = Button(root,text="Show top window", command=open_top_window)
btn3.pack(pady=10)

root.mainloop()