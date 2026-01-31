from tkinter import *
from tkinter import messagebox

def login():
    user = entry_user.get()
    pwd = entry_pass.get()

    if user == "admin" and pwd == "1234":
        messagebox.showinfo("Login Success", "Welcome Admin")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

root = Tk()
root.title("Login Page")
root.geometry("350x250")

Label(root, text="Login", font=("Arial", 18, "bold")).pack(pady=10)

Label(root, text="Username").pack()
entry_user = Entry(root)
entry_user.pack()

Label(root, text="Password").pack()
entry_pass = Entry(root, show="*")
entry_pass.pack()

Button(root, text="Login", command=login, width=15).pack(pady=20)

root.mainloop()
