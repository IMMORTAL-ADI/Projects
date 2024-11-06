from tkinter import* #pip install tkinter
from PIL import Image,ImageTk #pip install pillow
from tkcalendar import DateEntry  # pip install tkcalendar
#from win32api import GetSystemMetrics
#import win32gui, win32con
import sqlite3
import subprocess as sp

from tkinter import ttk,messagebox

#import pymysql


class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Database Mangement System | Developed By Aditya")
        self.root.geometry("13500x7000+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text=("Student Database Management System"),font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20,pady=10).place(x=0,y=0,relwidth=1,height=70)

        #==========all variables===============
        self.roll_no_var=StringVar()
        self.seat_var=StringVar()
        self.name_var=StringVar()
        self.gen_var=StringVar()
        self.email_var=StringVar()
        self.phone_var=StringVar()
        self.dob_var=StringVar()
        self.par_var=StringVar()
        self.par_cont_var=StringVar()
        self.address_var=StringVar()

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        #======top frame work=================
        btn_help=Button(self.root,command=self.help_window,text="Help",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=120)
        btn_logout=Button(self.root,command=self.root.destroy,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1300,y=10,height=50,width=150)
        self.lbl_clock=Label(self.root,text="Welcome to Student Database Management System",font=("times new roman",15),bg="gray",fg="white",justify="center")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        #======Manage Frame============
        Manage_Frame=Frame(self.root,bd=4,relief=GROOVE)
        Manage_Frame.place(x=20,y=110,width=550,height=660)
        
        #=======Student details==============
        m_title=Label(Manage_Frame,text="Student Details",font=("goudy old style",25,"bold"))
        m_title.grid(row=0,columnspan=4,padx=20)

        lbl_roll=Label(Manage_Frame,text="College Roll No:",font=("goudy old style",17,"bold"))
        lbl_roll.grid(row=1,column=0,padx=10,pady=10,sticky="w")

        txt_roll=Entry(Manage_Frame,textvariable=self.roll_no_var,font=("goudy old style",17,"bold"),bd=3,relief=SUNKEN,bg="white")
        txt_roll.grid(row=1,column=1,padx=10,pady=10)

        lbl_seat=Label(Manage_Frame,text="University Seat No:",font=("goudy old style",17,"bold"))
        lbl_seat.grid(row=2,column=0,padx=10,pady=10,sticky="w")

        txt_seat=Entry(Manage_Frame,textvariable=self.seat_var,font=("goudy old style",17,"bold"),bd=3,relief=SUNKEN,bg="white")
        txt_seat.grid(row=2,column=1,padx=10,pady=10)
        
        lbl_name=Label(Manage_Frame,text="Student's Full Name:",font=("goudy old style",17,"bold"))
        lbl_name.grid(row=3,column=0,padx=10,pady=10,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("goudy old style",17,"bold"),bd=3,relief=SUNKEN,bg="white")
        txt_name.grid(row=3,column=1,padx=10,pady=10)

        lbl_dob=Label(Manage_Frame,text="Date Of Birth:",font=("goudy old style",17,"bold"))
        lbl_dob.grid(row=4,column=0,padx=10,pady=10,sticky="w")

        txt_dob=DateEntry(Manage_Frame,textvariable=self.dob_var,font=("goudy old style",17,"bold"),width=19,bd=3,relief=SUNKEN,bg="white")
        txt_dob.grid(row=4,column=1,padx=10,pady=10)
        
        lbl_gen=Label(Manage_Frame,text="Gender:",font=("goudy old style",17,"bold"))
        lbl_gen.grid(row=5,column=0,padx=10,pady=10,sticky="w")

        txt_gen=ttk.Combobox(Manage_Frame,textvariable=self.gen_var,font=("goudy old style",17,"bold"),width=19,state="readonly")
        txt_gen["values"]=("Select","Male","Female","Other")
        txt_gen.grid(row=5,column=1,padx=10,pady=10)
        txt_gen.current(0)

        lbl_phone=Label(Manage_Frame,text="Mobile Number:",font=("goudy old style",17,"bold"))
        lbl_phone.grid(row=6,column=0,padx=10,pady=10,sticky="w")

        txt_phone=Entry(Manage_Frame,textvariable=self.phone_var,font=("goudy old style",17,"bold"),bd=3,relief=SUNKEN,bg="white")
        txt_phone.grid(row=6,column=1,padx=10,pady=10)

        lbl_mail=Label(Manage_Frame,text="E-mail Id:",font=("goudy old style",17,"bold"))
        lbl_mail.grid(row=7,column=0,padx=10,pady=10,sticky="w")

        txt_mail=Entry(Manage_Frame,textvariable=self.email_var,font=("goudy old style",17,"bold"),bd=3,relief=SUNKEN,bg="white")
        txt_mail.grid(row=7,column=1,padx=10,pady=10)
        
        lbl_pname=Label(Manage_Frame,text="Parent's Name:",font=("goudy old style",17,"bold"))
        lbl_pname.grid(row=8,column=0,padx=10,pady=10,sticky="w")

        txt_pname=Entry(Manage_Frame,textvariable=self.par_var,font=("goudy old style",17,"bold"),bd=3,relief=SUNKEN,bg="white")
        txt_pname.grid(row=8,column=1,padx=10,pady=10)

        lbl_pphone=Label(Manage_Frame,text="Parent's Contact:",font=("goudy old style",17,"bold"))
        lbl_pphone.grid(row=9,column=0,padx=10,pady=10,sticky="w")

        txt_pphone=Entry(Manage_Frame,textvariable=self.par_cont_var,font=("goudy old style",17,"bold"),bd=3,relief=SUNKEN,bg="white")
        txt_pphone.grid(row=9,column=1,padx=10,pady=10)

        lbl_add=Label(Manage_Frame,text="Home Address:",font=("goudy old style",17,"bold"))
        lbl_add.grid(row=10,column=0,padx=10,pady=10,sticky="w")

        txt_add=Entry(Manage_Frame,textvariable=self.address_var,font=("goudy old style",17,"bold"),bd=3,relief=SUNKEN,bg="white")
        txt_add.grid(row=10,column=1,padx=10,pady=10)

        #=========buttons frame student details============
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="white")
        btn_Frame.place(x=10,y=600,width=510)

        addbtn=Button(btn_Frame,text="ADD",width=10,command=self.add_students).grid(row=11,column=0,padx=10)
        updatebtn=Button(btn_Frame,text="UPDATE",width=10,command=self.update).grid(row=11,column=1,padx=10)
        viewbtn=Button(btn_Frame,text="VIEW",width=10,command=self.view).grid(row=11,column=2,padx=10)
        clearbtn=Button(btn_Frame,text="CLEAR",width=10,command=self.clear).grid(row=11,column=3,padx=10)
        deletebtn=Button(btn_Frame,text="DELETE",width=10,command=self.delete).grid(row=11,column=4,padx=10)

        #=======Detail Frame===========
        Detail_Frame=Frame(self.root,bd=4,relief=GROOVE)
        Detail_Frame.place(x=580,y=110,width=940,height=660)

        lbl_search=Label(Detail_Frame,text="Search By",font=("goudy old style",25,"bold"))
        lbl_search.grid(row=0,column=0,padx=10,pady=10,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.var_searchby,font=("goudy old style",15,"bold"),width=10,state="readonly")
        combo_search["values"]=("Select","College_roll_no","University_seat_no","Name","Phone_no","Email")
        combo_search.grid(row=0,column=1,padx=10,pady=10)
        combo_search.current(0)

        txt_search=Entry(Detail_Frame,textvariable=self.var_searchtxt,font=("goudy old style",15,"bold"),width=20,bd=3,relief=SUNKEN,bg="white")
        txt_search.grid(row=0,column=2,padx=10,pady=10)

        searchbtn=Button(Detail_Frame,text="Search",width=10,command=self.search).grid(row=0,column=3,padx=5)
        showallbtn=Button(Detail_Frame,text="Show all",width=10,command=self.show).grid(row=0,column=4,padx=5)

        #===========Table frame==============
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE)
        Table_Frame.place(x=10,y=60,width=900,height=570)

        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_Frame,columns=("College Roll No","University Seat no.","Student's Full Name","Date Of Birth","Gender","Mobile Number","E-mail ID","Parent's Name","Parent's Contact","Home Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("College Roll No",text="College Roll No")
        self.student_table.heading("University Seat no.",text="University Seat No")
        self.student_table.heading("Student's Full Name",text="Student's Full Name")
        self.student_table.heading("Date Of Birth",text="Date Of Birth")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Mobile Number",text="Mobile Number")
        self.student_table.heading("E-mail ID",text="E-mail ID")
        self.student_table.heading("Parent's Name",text="Parent's Name")
        self.student_table.heading("Parent's Contact",text="Parent's Contact")
        self.student_table.heading("Home Address",text="Home Address")

        self.student_table["show"]="headings"

        self.student_table.column("College Roll No",width=100)
        self.student_table.column("University Seat no.",width=120)
        self.student_table.column("Student's Full Name",width=200)
        self.student_table.column("Date Of Birth",width=100)
        self.student_table.column("Gender",width=50)
        self.student_table.column("Mobile Number",width=100)
        self.student_table.column("E-mail ID",width=200)
        self.student_table.column("Parent's Name",width=200)
        self.student_table.column("Parent's Contact",width=100)
        self.student_table.column("Home Address",width=200)

        self.student_table.pack(fill=BOTH,expand=1)

        self.show()
     #================all function and working===========================
    def help_window(self):
        program_name="Notepad.exe"
        file_name="Help.txt"
        sp.Popen([program_name,file_name])
    def login_window(self):
        self.root.destroy()
        import login
        
    def add_students(self):
        con=sqlite3.connect(database="sdms.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS student (College_roll_no varchar(20) PRIMARY KEY,University_seat_no varchar(100) NOT NULL,Name varchar(100) NOT NULL,DOB varchar(50) NOT NULL,gen varchar(50) NOT NULL,Phone_no varchar(15) DEFAULT NULL,Email varchar(200) DEFAULT NULL,parent_name varchar(200) DEFAULT NULL,parent_cont varchar(15) DEFAULT NULL,address varchar(200) DEFAULT NULL)")
        try:
            if self.roll_no_var.get()=="":
                messagebox.showerror("Error","College Roll no must be required",parent=self.root)
                
            else:
                cur.execute("Select * from student where College_roll_no=?",(self.roll_no_var.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This College roll already assigned",parent=self.root)
                else:
                    cur.execute("Insert into student (College_roll_no,University_seat_no,Name,DOB,gen,Phone_no,Email,parent_name,parent_cont,address)values(?,?,?,?,?,?,?,?,?,?)",(self.roll_no_var.get(),self.seat_var.get(),self.name_var.get(),self.dob_var.get(),self.gen_var.get(),self.phone_var.get(),self.email_var.get(),self.par_var.get(),self.par_cont_var.get(),self.address_var.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Student Detail Added Successfully",parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def show(self):
        con=sqlite3.connect(database="sdms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def view(self):
        f=self.student_table.focus()
        content=(self.student_table.item(f))
        row=content["values"]
        #====
        self.roll_no_var.set(row[0])
        self.seat_var.set(row[1])
        self.name_var.set(row[2])
        self.dob_var.set(row[3])
        self.gen_var.set(row[4])
        self.phone_var.set(row[5])
        self.email_var.set(row[6])
        self.par_var.set(row[7])
        self.par_cont_var.set(row[8])
        self.address_var.set(row[9])
        
    def update(self):
        con=sqlite3.connect(database="sdms.db")
        cur=con.cursor()
        try:
            if self.roll_no_var.get()=="":
                messagebox.showerror("Error","College Roll no must be required",parent=self.root)
                
            else:
                cur.execute("Select * from student where College_roll_no=?",(self.roll_no_var.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","This College Roll number does not exists.",parent=self.root)
                else:
                    cur.execute("update student set University_seat_no=?,Name=?,DOB=?,gen=?,Phone_no=?,Email=?,parent_name=?,parent_cont=?,address=? where College_roll_no=?",(self.seat_var.get(),self.name_var.get(),self.dob_var.get(),self.gen_var.get(),self.phone_var.get(),self.email_var.get(),self.par_var.get(),self.par_cont_var.get(),self.address_var.get(),self.roll_no_var.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Student Detail Updated Successfully",parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.roll_no_var.set("")
        self.seat_var.set("")
        self.name_var.set("")
        self.dob_var.set("")
        self.gen_var.set("Select")
        self.phone_var.set("")
        self.email_var.set("")
        self.par_var.set("")
        self.par_cont_var.set("")
        self.address_var.set("")
        

    def delete(self):
        con=sqlite3.connect(database="sdms.db")
        cur=con.cursor()
        try:
            if self.roll_no_var.get()=="":
                messagebox.showerror("Error","College Roll no must be required",parent=self.root)
                
            else:
                cur.execute("Select * from student where College_roll_no=?",(self.roll_no_var.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","This College Roll number does not exists.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where College_roll_no=?",(self.roll_no_var.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student Detail Deleted Successfully",parent=self.root)
                        self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def search(self):
        con=sqlite3.connect(database="sdms.db")
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select * from student where " + self.var_searchby.get() + " LIKE '%"+self.var_searchtxt.get() + "%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","NO Recoed found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)






#if __name__=="__main__":
root=Tk()
obj=Student(root)
root.mainloop()
