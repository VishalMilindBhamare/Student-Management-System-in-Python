from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk
import pymysql
from tkcalendar import DateEntry
from datetime import date

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1450x835+0+0")

        title = Label(self.root, text="Student Management System | Login Area", bd=10, relief=GROOVE,
                      font=("Times new roman", 40, "bold"), bg="Teal", fg="White")
        title.pack(side=TOP, fill=X)

        # All images
        self.bg_icon = ImageTk.PhotoImage(file="bg1.jpg")
        self.logo_icon = ImageTk.PhotoImage(file="logo.png")

        # Variables
        self.uname = StringVar()
        self.pass_ = StringVar()

        # Background image
        bg_lbl = Label(self.root, image=self.bg_icon)
        bg_lbl.pack()

        # Login Frame
        Login_Frame = Frame(self.root, bg="white")
        Login_Frame.place(x=500, y=150, width=450)

        # Logo
        logolbl = Label(Login_Frame, image=self.logo_icon, bd=0)
        logolbl.grid(row=0, columnspan=2, pady=20)

        # Username label and entry
        lbluser = Label(Login_Frame, text="Username", font=("Times new roman", 20, "bold"), bg="white")
        lbluser.grid(row=1, column=0, padx=20, pady=10)
        txtuser = Entry(Login_Frame, bd=5, textvariable=self.uname, relief=GROOVE, font=("", 15))
        txtuser.grid(row=1, column=1, padx=20)

        # Password label and entry
        lblpass = Label(Login_Frame, text="Password", font=("Times new roman", 20, "bold"), bg="white")
        lblpass.grid(row=2, column=0, padx=20, pady=10)
        txtpass = Entry(Login_Frame, bd=5, textvariable=self.pass_, relief=GROOVE, font=("", 15), show='*')
        txtpass.grid(row=2, column=1, padx=20)

        # Login button
        btn_log = Button(Login_Frame, text="Login", width=15, command=self.login, font=("Times new roman", 14, "bold"),
                         bg="Teal", fg="white")
        btn_log.grid(row=3, column=1, pady=10)


         # News Ticker
        self.news_var = StringVar()
        news_label = ttk.Label(self.root, textvariable=self.news_var, anchor='w', font=('Helvetica', 12, 'bold'))
        news_label.place(x=0, y=785, width=1440,height=50)  # Adjust the position as needed

        # News update
        self.news_items = [ "Welcome to the Student Management System!",
    "With the new semester approaching next week, get ready for class allocation updates!",
    "To ensure accuracy, please review and update student records before the semester begins.",
    "Don't forget to submit grade reports by the end of this month.",
    "Check out the updated academic calendar on our website.",
    "Staff meeting scheduled for next Wednesday. Agenda: Curriculum updates.",
    "Congratulations to our students on their recent achievements!",
    "Feedback session scheduled for next Friday. Share your thoughts!",
    "Upcoming training sessions on using advanced features of the system.",
    "Reminder: Attendance reports due by the 15th of each month.",
    "Thank you for your dedication to student success!"]
        self.news_index = 0
        self.update_news()

    def update_news(self):
        if self.news_var:
            self.news_var.set(self.news_items[self.news_index])
            self.news_index = (self.news_index + 1) % len(self.news_items)
            self.root.after(3000, self.update_news)  # Schedule next update



    def login(self):
        if self.uname.get() == "" or self.pass_.get() == "":
            messagebox.showerror("Error", "All fields are required!!")
        elif self.uname.get() == "Vishal" and self.pass_.get() == "123456":
            messagebox.showinfo("Successful", f"Welcome {self.uname.get()}")
            self.root.destroy()  # Close login window
            self.open_student_management()
        else:
            messagebox.showerror("Error", "Invalid Username or Password!!")

    def open_student_management(self):
        root = Tk()
        ob = StudentManagement(root)
        root.mainloop()


class StudentManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1450x835+0+0")

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,font=("Times new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        # Initialize variables
        self.roll_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.doj_var = StringVar()
        self.Status_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        #===========Manage Frame===========#

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#8B0000")
        Manage_Frame.place(x=20,y=100,width=450,height=730)

        m_title=Label(Manage_Frame,text="Manage Students",bg="#8B0000",fg="#FFE4E1",font=("Times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="ID.",bg="#8B0000",fg="white",font=("Times new roman",20))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_Frame,textvariable=self.roll_var,font=("Times new roman",15),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        lbl_name=Label(Manage_Frame,text="Name.",bg="#8B0000",fg="white",font=("Times new roman",20,""))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("Times new roman",15,""),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")


        lbl_email=Label(Manage_Frame,text="Email.",bg="#8B0000",fg="white",font=("Times new roman",20,""))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("Times new roman",15,""),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")


        lbl_gender=Label(Manage_Frame,text="Gender.",bg="#8B0000",fg="white",font=("Times new roman",20,""))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,""),state='readonly')
        combo_gender['values']=("Male","Female","other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_contact=Label(Manage_Frame,text="Contact No.",bg="#8B0000",fg="white",font=("Times new roman",20,""))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("Times new roman",15,""),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_DOB = Label(Manage_Frame, text="D.O.B", bg="#8B0000", fg="white", font=("Times new roman", 20, ""))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.txt_DOB = DateEntry(Manage_Frame,textvariable=self.dob_var, font=("Times new roman", 15, ""), bd=5, relief=GROOVE,date_pattern='dd/mm/yyyy',state='readonly')
        self.txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_DOJ = Label(Manage_Frame, text="D.O.J", bg="#8B0000", fg="white", font=("Times new roman", 20, ""))
        lbl_DOJ.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_DOJ = DateEntry(Manage_Frame,textvariable=self.doj_var,font=("Times new roman", 15, ""), bd=5, relief=GROOVE, date_pattern='dd/mm/yyyy',state='readonly')
        self.txt_DOJ.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        lbl_Status=Label(Manage_Frame,text="Status",bg="#8B0000",fg="white",font=("Times new roman",20,""))
        lbl_Status.grid(row=8,column=0,pady=10,padx=20,sticky="w")

        combo_Status=ttk.Combobox(Manage_Frame,textvariable=self.Status_var,font=("times new roman",13,""),state='readonly')
        combo_Status['values']=("Ongoing","Discontinue","Paused","Course Completed")
        combo_Status.grid(row=8,column=1,padx=20,pady=10)

        lbl_Address=Label(Manage_Frame,text="Address",bg="#8B0000",fg="white",font=("Times new roman",20,""))
        lbl_Address.grid(row=9,column=0,pady=10,padx=20,sticky="w")

        self.txt_Address=Text(Manage_Frame,width=35,height=5,font=("Times New Roman",10))
        self.txt_Address.grid(row=9,column=1,pady=10,padx=20,sticky="w")



        #===========Button Frame============#

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#DDDDDD")
        btn_Frame.place(x=15,y=645,width=400)

        Addbtn=Button(btn_Frame,text="Save",bg="Teal",fg="white",font=("Times new roman",16,"bold"),command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",bg="Teal",fg="white",font=("Times new roman",16,"bold"),command=self.Update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",bg="Teal",fg="white",font=("Times new roman",16,"bold"),command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",bg="Teal",fg="white",font=("Times new roman",16,"bold"),command=self.clear).grid(row=0,column=3,padx=10,pady=10)



        #===========Detail Frame===========#

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#8B0000")
        Detail_Frame.place(x=500,y=100,width=900,height=730)

        
        lbl_Search=Label(Detail_Frame,text="Search By",bg="#8B0000",fg="white",font=("Times new roman",20,"bold"))
        lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_Search['values']=("ID","Name","Contact")
        combo_Search.grid(row=0,column=1,padx=20,pady=10)

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("Times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",bg="Teal",fg="white",font=("Times new roman",14,"bold"),pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showeallbtn=Button(Detail_Frame,text="Show All",bg="Teal",fg="white",font=("Times new roman",14,"bold"),pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)


         # Login button
        btn_logout = Button(Detail_Frame, text="Logout", command=self.logout, font=("Times new roman", 14, "bold"),
                            bg="Teal", fg="white")
        btn_logout.place(x=800, y=20)

        #============Dev Frame================#       
        Dev_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#8B0000")
        Dev_Frame.place(x=10,y=680,width=870,height=32)

        lbl_deve=Label(Dev_Frame,text="Devloped by :- Vishal Bhamare ",bg="#8B0000",fg="white",font=("Times new roman",13,"bold"))
        lbl_deve.grid(row=0,column=0,pady=0,padx=335,sticky="w")

        #==================Table Frame============================#
        
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#8B0000")
        Table_Frame.place(x=10,y=70,width=870,height=600)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("ID","Name","Email","Gender","Contact","D.O.B","D.O.J","Status","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("ID", text="ID.")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Contact", text="Contact")
        self.Student_table.heading("D.O.B", text="D.O.B")
        self.Student_table.heading("D.O.J", text="D.O.J")
        self.Student_table.heading("Status", text="Status")
        self.Student_table.heading("Address", text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("ID",width=100)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Email",width=100)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("D.O.B",width=100)
        self.Student_table.column("D.O.J",width=100)
        self.Student_table.column("Status",width=100)
        self.Student_table.column("Address",width=100)
        self.fetch_data()
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_students(self):
        if self.roll_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.roll_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.doj_var.get(),
                                                                            self.Status_var.get(),
                                                                            self.txt_Address.get('1.0',END)
                                                                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="sms")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
    # Check if all fields are already clear
        if (self.roll_var.get() == "" and
            self.name_var.get() == "" and
            self.email_var.get() == "" and
            self.gender_var.get() == "" and
            self.contact_var.get() == "" and
            self.dob_var.get() == "" and
            self.doj_var.get() == "" and
            self.Status_var.get() == "" and
            self.txt_Address.get("1.0", END) == "\n"):
            
            messagebox.showwarning("Already Cleared", "Fields are already clear.")
        else:
            self.roll_var.set("")
            self.name_var.set("")
            self.email_var.set("")
            self.gender_var.set("")
            self.contact_var.set("")
            self.dob_var.set("")
            self.doj_var.set("")
            self.Status_var.set("")
            self.txt_Address.delete("1.0", END)


    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        
        if row:  # Check if row is not empty
            if len(row) >= 9:  # Ensure row has at least 9 elements
                self.roll_var.set(row[0])
                self.name_var.set(row[1])
                self.email_var.set(row[2])
                self.gender_var.set(row[3])
                self.contact_var.set(row[4])
                self.dob_var.set(row[5])
                self.doj_var.set(row[6])
                self.Status_var.set(row[7])
                self.txt_Address.delete("1.0", END)
                self.txt_Address.insert(END, row[8])
            else:
                print("Row does not have enough elements to unpack")
        else:
            print("Row is empty or None")

        
    def Update_data(self):
        if not self.roll_var.get():
            messagebox.showerror("Error", "ID field cannot be empty")
            return

        if (not self.name_var.get() or not self.email_var.get() or not self.gender_var.get() or 
            not self.contact_var.get() or not self.dob_var.get() or not self.doj_var.get() or 
            not self.Status_var.get() or not self.txt_Address.get("1.0", END).strip()):
            messagebox.showerror("Error", "All fields are required")
            return

        confirmation = messagebox.askyesno("Confirm Update", "Are you sure you want to update this record?")
        if confirmation:
            con = pymysql.connect(host="localhost", user="root", password="", database="sms")
            cur = con.cursor()
            cur.execute("UPDATE students SET name=%s, email=%s, gender=%s, contact=%s, dob=%s, doj=%s, Status=%s, Address=%s WHERE id=%s", (
                                                                                                                    self.name_var.get(),
                                                                                                                    self.email_var.get(),
                                                                                                                    self.gender_var.get(),
                                                                                                                    self.contact_var.get(),
                                                                                                                    self.dob_var.get(),
                                                                                                                    self.doj_var.get(),
                                                                                                                    self.Status_var.get(),
                                                                                                                    self.txt_Address.get("1.0", END),
                                                                                                                    self.roll_var.get()
                                                                                                                    ))  
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()


    def delete_data(self):
        if not self.roll_var.get():
            messagebox.showerror("Error", "ID field cannot be empty")
            return

        confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
        if confirmation:
            con = pymysql.connect(host="localhost", user="root", password="", database="sms")
            cur = con.cursor()
            cur.execute("DELETE FROM students WHERE id=%s", self.roll_var.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()


    def search_data(self):
        if self.search_by.get()=="" or self.search_txt.get()=="":
            messagebox.showerror("Error", "The Search fields are empty") 
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()

    # Check if search_by is selected and search_txt is not empty
        if self.search_by.get() and self.search_txt.get():
            # Construct the query with proper formatting
            query = f"SELECT * FROM students WHERE {self.search_by.get()} LIKE '%{self.search_txt.get()}%'"
            cur.execute(query)
            rows = cur.fetchall()

            if len(rows) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert("", END, values=row)
                con.commit()
        else:
            # If search criteria are not selected or search text is empty, fetch all data
            self.fetch_data()

        con.close()



    def logout(self):
        self.root.destroy()
        LoginSystem(Tk())

# Main program
root = Tk()
obj = LoginSystem(root)
root.mainloop()
