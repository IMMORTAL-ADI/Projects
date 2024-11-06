from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("13500x7000+0+0")
        #=======bg image=====
        #file="C:/Aditya Codes/back2.jpeg"
        self.bg=ImageTk.PhotoImage(file="C:/Aditya Codes/FE PBL/back2.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)


        #=======left image=====
        self.left=ImageTk.PhotoImage(file="C:/Aditya Codes/FE PBL/a1.png")
        left=Label(self.root,image=self.left).place(x=100,y=150,width=350,height=480)


        #=======Registration  frame=========
        frame1=Frame(self.root,bg='white')
        frame1.place(x=450,y=150,width=800,height=480)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="dark cyan")
        title.place(x=50,y=20)

        #==========row1
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray")
        f_name.place(x=50,y=70)
        self.txt_fname=Entry(frame1,font=("time new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=100,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray")
        l_name.place(x=370,y=70)
        self.txt_lname=Entry(frame1,font=("time new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=100,width=250)

        #==========row2
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray")
        contact.place(x=50,y=140)
        self.txt_contact=Entry(frame1,font=("time new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=170,width=250)

        email=Label(frame1,text="E-mail ID",font=("times new roman",15,"bold"),bg="white",fg="gray")
        email.place(x=370,y=140)
        self.txt_email=Entry(frame1,font=("time new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=170,width=250)

        #=========row3
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray")
        question.place(x=50,y=210)
        self.cmb_quest=ttk.Combobox(frame1,font=("time new roman",13),state='readonly')
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.current(0)
        self.cmb_quest.place(x=50,y=240,width=250)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray")
        answer.place(x=370,y=210)
        self.txt_answer=Entry(frame1,font=("time new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=240,width=250)

        #========row4
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray")
        password.place(x=50,y=280)
        self.txt_password=Entry(frame1,font=("time new roman",15),bg="lightgray",show="*")
        self.txt_password.place(x=50,y=310,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray")
        cpassword.place(x=370,y=280)
        self.txt_cpassword=Entry(frame1,font=("time new roman",15),bg="lightgray",show="*")
        self.txt_cpassword.place(x=370,y=310,width=250)

        #==========ROW5
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12),bg="white").place(x=50,y=350)

        self.btn_img=ImageTk.PhotoImage(file="C:/Aditya Codes/FE PBL/register1.jpeg")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420,width=200,height=40)


        #==========sign in
        btn_login=Button(self.root,command=self.login_window,text="Sign In",font=("times new roman",20),bg="dark cyan",fg="white",bd=0,cursor="hand2").place(x=180,y=550,width=180)

    def login_window(self):
        self.root.destroy()
        import login
        
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All fields Are Required",parent=self.root)

        elif self.txt_password.get() != self.txt_cpassword.get() :
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)

        elif self.var_chk.get()==0 :
            messagebox.showerror("Error","Please Agree our Terms & Conditions.",parent=self.root)

        else:
            try:
                con=sqlite3.connect(database="sdms.db")
                cur=con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS employee1 (eid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,f_name VARCHAR(200) NULL,l_name VARCHAR(200) NULL,contact VARCHAR(15) NULL,email VARCHAR(200) NULL,question VARCHAR(200) NULL,answer VARCHAR(200) NULL,password VARCHAR(200) NULL)")
                cur.execute("select * from employee1 where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exists,Please try with another Email Id",parent=self.root)
                else:
                    cur.execute("insert into employee1(f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",
                                (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.cmb_quest.get(),
                                self.txt_answer.get(),
                                self.txt_password.get(),
                                ))
                    con.commit()
                    messagebox.showinfo("Success","Registered Successful",parent=self.root)
                    self.clear()


            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
                
            
              #self.txt_lname.get(),
              #self.txt_contact.get(),
              #self.txt_email.get(),
              #self.cmb_quest.get(),
              #self.txt_answer.get(),
              #self.txt_password.get(),
              #self.txt_cpassword.get())
            
        
        
        

root=Tk()
obj=Register(root)
root.mainloop()
