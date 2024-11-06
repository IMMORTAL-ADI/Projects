from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
import sqlite3


#from register import Register

class login_window:

    def __init__(self, root):
        self.root = root
        self.root.title("Log In Window")
        self.root.geometry("13500x7000+0+0")

        #=======bg image=====
        self.bg = ImageTk.PhotoImage(file="C:/Aditya/only pbl/FE PBL/back2.jpg")
        bg = Label(self.root, image=self.bg).place(x=450, y=0, relwidth=1, relheight=1)

        #=======left image=====
        self.left = ImageTk.PhotoImage(file="C:/Aditya/only pbl/FE PBL/t2.png")
        left = Label(self.root, image=self.left).place(x=100, y=150, width=350, height=480)

        #=======login  frame=========
        login_frame = Frame(self.root, bg='white')
        login_frame.place(x=450, y=150, width=800, height=480)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 28, "bold"), bg="white", fg="dark cyan")
        title.place(x=50, y=40)

        #======row1
        email = Label(login_frame, text="E-mail ID", font=("times new roman", 18, "bold"), bg="white", fg="gray")
        email.place(x=50, y=130)

        self.txt_email = Entry(login_frame, font=("time new roman", 18), bg="lightgray")
        self.txt_email.place(x=50, y=180, width=350)

        pass1 = Label(login_frame, text="Password", font=("times new roman", 18, "bold"), bg="white", fg="gray")
        pass1.place(x=50, y=230)

        self.txt_pass1 = Entry(login_frame, font=("time new roman", 18), bg="lightgray", show="*")
        self.txt_pass1.place(x=50, y=280, width=350)

        btn_reg = Button(login_frame, command=self.register_window, text="New Registration?",
                         font=("times new roman", 14), bd=0, bg="white", fg="black", cursor="hand2")
        btn_reg.place(x=50, y=320)

        btn_login = Button(login_frame, text="LOGIN", command=self.login, font=("times new roman", 18), bd=2, bg="turquoise", fg="white", cursor="hand2")
        btn_login.place(x=50, y=370, width=150, height=40)

    #self.new_win=Toplevel(self.root)
    #self.new_obj=Register(self.new_win)
    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get() == "" or self.txt_pass1.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="sdms.db")
                cur = con.cursor()
                cur.execute("select * from employee1 where email=? and password=?",
                            (self.txt_email.get(), self.txt_pass1.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Username and Password", parent=self.root)
                else:
                    messagebox.showinfo("Succes", "Welcome to Student Database Management System")
                    self.root.destroy()
                    import sdms

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


#if __name__=="__main__":
root = Tk()
obj = login_window(root)
root.mainloop()
