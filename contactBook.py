from tkinter import *
import datetime
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

date = datetime.datetime.now().date()
date = str(date)

"""  Home Page """

def start(root):
    root.title("Welcome to your contact book")
    temp(root)

def check1(root):
    root.geometry("650x550+350+60")
    root.title("Welcome to your contact book")
    
    #frams
    root.top = Frame(root, height=150, bg='white') 
    root.top.pack(fill=X) 
    root.bottom = Frame(root, height=500, bg='#34baeb')
    root.bottom.pack(fill=X)

    #top frame design
    root.top_image1 = PhotoImage(file='icons/contact-book.png')
    root.top_image1_label = Label(root.top, image=root.top_image1)
    root.top_image1_label.place(x=120, y=10) 
    
    root.heading = Label(root.top, text = "My Phonebook", font='Arial 15 bold', bg='white',fg='#ebb434')
    root.heading.place(x=210, y=30)
    
    root.date_lbl = Label(root.top, text="Date:"+date, font='arial 15 bold', fg='#ebb434',bg='white')
    root.date_lbl.place(x=450, y=100)
        
    #button1: view people
    root.viewButton = Button(root.bottom, text="My People", width=11, bg='white', fg='#42bcf5', font='arial 12 bold', command=lambda:my_people(root))
    root.viewButton.place(x=270,y=70)  
    #button2: add people
    root.addButton = Button(root.bottom, text="Add People", width=11, bg='white', fg='#42bcf5', font='arial 12 bold', command=lambda:addpeoplefunction(root))
    root.addButton.place(x=270,y=140)
    #button3: exit
    viewButton = Button(root.bottom, text="Log Out", width=11, bg='white', fg='#42bcf5', font='arial 12 bold',command=lambda: logout(root))
    viewButton.place(x=270,y=210)  

def exit(root):
    answer = messagebox.askquestion("Warning","Are you sure you want to Exit?")
    if answer == 'yes':
        messagebox.showinfo("Success", "Please Visit Again!")
        root.destroy()
    
def logout(root):
    answer = messagebox.askquestion("Warning","Are you sure you want to log out?")
    if answer == 'yes':
        root.destroy()
        main()    

""" My People Page """

def my_people(root):
    root.destroy()
    MyPeople()

def My_People(root):
    root.geometry("650x550+350+80")
    root.title("My People")
    root.resizable(False, False)

    #frams
    root.top = Frame(root, height=150, bg='white') 
    root.top.pack(fill=X) 
    root.bottom = Frame(root, height=500, bg='#b5f5b0')
    root.bottom.pack(fill=X)

    #top frame design
    root.top_image = PhotoImage(file='icons/teamwork.png')
    root.top_image_label = Label(root.top, image=root.top_image)
    root.top_image_label.place(x=120, y=10) 

    root.heading = Label(root.top, text = "My People", font='Arial 15 bold', bg='white',fg='#ebb434')
    root.heading.place(x=210, y=30)

    root.scroll = Scrollbar(root.bottom, orient=VERTICAL)
        
    root.listBox = Listbox(root.bottom, width=50, height=25, bg='#f2e785', font='arial 10 bold')
    root.listBox.grid(row=0, column=0, padx=(80,0))

    root.scroll.config(command=root.listBox.yview)
    root.listBox.config(yscrollcommand=root.scroll.set)

    persons = cur.execute("select * from 'phone_book'").fetchall()
    print(persons)
    count=0
    for person in persons:
        root.listBox.insert(count, str(person[0]) +  ". " + person[1] + " " + person[2] + " " + person[4])
        count += 1

    root.scroll.grid(row=0, column=1, sticky=N+S)
    
    #buttons
    btnadd = Button(root.bottom, text="Add", width=12, font='arial 12 bold', command=lambda: addpeoplefunction(root))
    btnadd.grid(row=0, column=2, padx=20, pady=10, sticky=N)

    btnupdate = Button(root.bottom, text="Update", width=12, font='arial 12 bold', command =lambda:  update_function(root))
    btnupdate.grid(row=0, column=2, padx=20, pady=50, sticky=N)

    btnDisplay = Button(root.bottom, text="Display", width=12, font='arial 12 bold', command=lambda: display_person(root))
    btnDisplay.grid(row=0, column=2, padx=20, pady=90, sticky=N)

    btnDelete = Button(root.bottom, text="Delete", width=12, font='arial 12 bold', command=lambda: delete_person(root))
    btnDelete.grid(row=0, column=2, padx=20, pady=130, sticky=N)

    viewButton = Button(root.bottom, text="Home", width=12, font='arial 12 bold',command=lambda: home(root))
    viewButton.grid(row=0, column=2, padx=20, pady=170, sticky=N)

def MyPeople():
    root = Tk() 
    My_People(root)
    root.mainloop() 
   
""" Update Page """

def update_function(root):
    selected_item = root.listBox.curselection()  
    person = root.listBox.get(selected_item)
    person_id = person.split(".")[0]
    root.destroy()    
    updatepage = Update(person_id)

def update(root,person_id):
    root.geometry("650x550+350+80")
    root.title("Update Person")
    root.resizable(False, False)

    print("person id : ", person_id)

    query = "select * from phone_book where person_id = '{}'" . format(person_id)
    result = cur.execute(query).fetchone()
    print(result)
    root.person_id = person_id

    person_name = result[1]
    person_surname = result[2]
    person_email = result[3]
    person_phone = result[4]
    person_address = result[5]

    print("Person Name :", person_name)

    #frams
    root.top = Frame(root, height=150, bg='white') 
    root.top.pack(fill=X) 
    root.bottom = Frame(root, height=500, bg='#fcfc7e')
    root.bottom.pack(fill=X)

    #top frame design
    root.top_image = PhotoImage(file='icons/user.png')
    root.top_image_label = Label(root.top, image=root.top_image)
    root.top_image_label.place(x=120, y=10) 

    root.heading = Label(root.top, text = "Update Person", font='Arial 15 bold', bg='white',fg='#ebb434')
    root.heading.place(x=210, y=30)

    #name
    root.label_name = Label(root.bottom, text="  Name  ", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_name.place(x=140, y=40)
    root.entry_name = Entry(root.bottom, width=30, bd=4)
    root.entry_name.insert(0,person_name)
    root.entry_name.place(x=270,y=40)

    #surname
    root.label_surname = Label(root.bottom, text="  Surname  ", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_surname.place(x=140, y=80)
    root.entry_surname = Entry(root.bottom, width=30, bd=4)
    root.entry_surname.insert(0,person_surname)
    root.entry_surname.place(x=270,y=80)

    #email
    root.label_email = Label(root.bottom, text="  Email  ", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_email.place(x=140, y=120)
    root.entry_email = Entry(root.bottom, width=30, bd=4)
    root.entry_email.insert(0,person_email)
    root.entry_email.place(x=270,y=120)

    #phone number
    root.label_phone = Label(root.bottom, text="Phone Number", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_phone.place(x=140, y=160)
    root.entry_phone = Entry(root.bottom, width=30, bd=4)
    root.entry_phone.insert(0,person_phone)
    root.entry_phone.place(x=270,y=160)

    #address
    root.label_address = Label(root.bottom, text="  Address  ", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_address.place(x=140, y=200)
    root.entry_address = Text(root.bottom, width=23, height=5)
    root.entry_address.insert(1.0,person_address)
    root.entry_address.place(x=270,y=200)

    #buttons
    button = Button(root.bottom, text="Update Person", font='arial 12 bold', fg='white', bg='#fcc324', command=lambda:update_people(root))
    button.place(x=215, y=300)

    viewButton = Button(root.bottom, text=" Home ", fg='white', bg='#fcc324', font='arial 12 bold',command=lambda: home(root))
    viewButton.place(x=360,y=300)  
        
def update_people(root):    
    id = root.person_id
    name = root.entry_name.get()
    surname = root.entry_surname.get()    
    email = root.entry_email.get()
    phone = root.entry_phone.get()
    address = root.entry_address.get(1.0, 'end-1c')

    query="update phone_book set person_name = '{}', person_surname='{}', person_email='{}', person_phone='{}', person_address='{}' where person_id = {}".format(name, surname, email, phone, address, id)

    try:
        cur.execute(query)
        con.commit()
        messagebox.showinfo("Success", "Contact Updated")
    except EXCEPTION as e:
        print(e)     

def Update(person_id):
    root = Tk() 
    update(root,person_id)
    root.mainloop()  


""" Display Page """

def display_person(root):   
    selected_item = root.listBox.curselection()  
    person = root.listBox.get(selected_item)
    person_id = person.split(".")[0]
    root.destroy()    
    displaypage = Display(person_id)

def display(root,person_id):
    root.geometry("650x550+350+80")
    root.title("Display Person")
    root.resizable(False, False)

    print("person id : ", person_id)

    query = "select * from phone_book where person_id = '{}'" . format(person_id)
    result = cur.execute(query).fetchone()
    print(result)
    root.person_id = person_id

    person_name = result[1]
    person_surname = result[2]
    person_email = result[3]
    person_phone = result[4]
    person_address = result[5]

    print("Person Name :", person_name)

    #frams
    root.top = Frame(root, height=150, bg='white') 
    root.top.pack(fill=X) 
    root.bottom = Frame(root, height=500, bg='#fcfc7e')
    root.bottom.pack(fill=X)

    #top frame design
    root.top_image = PhotoImage(file='icons/user.png')
    root.top_image_label = Label(root.top, image=root.top_image)
    root.top_image_label.place(x=120, y=10) 
    root.heading = Label(root.top, text = "Person Details", font='Arial 15 bold', bg='white',fg='#ebb434')
    root.heading.place(x=210, y=30)

    #name
    root.label_name = Label(root.bottom, text="  Name  ", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_name.place(x=140, y=40)
    root.entry_name = Entry(root.bottom, width=30, bd=4)
    root.entry_name.insert(0,person_name)
    root.entry_name.config(state='disabled')
    root.entry_name.place(x=270,y=40)

    #surname
    root.label_surname = Label(root.bottom, text="  Surname  ", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_surname.place(x=140, y=80)
    root.entry_surname = Entry(root.bottom, width=30, bd=4)
    root.entry_surname.insert(0,person_surname)
    root.entry_surname.config(state='disabled')
    root.entry_surname.place(x=270,y=80)

    #email
    root.label_email = Label(root.bottom, text="  Email  ", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_email.place(x=140, y=120)
    root.entry_email = Entry(root.bottom, width=30, bd=4)
    root.entry_email.insert(0,person_email)
    root.entry_email.config(state='disabled')
    root.entry_email.place(x=270,y=120)

    #phone number
    root.label_phone = Label(root.bottom, text="Phone Number", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_phone.place(x=140, y=160)
    root.entry_phone = Entry(root.bottom, width=30, bd=4)
    root.entry_phone.insert(0,person_phone)
    root.entry_phone.config(state='disabled')
    root.entry_phone.place(x=270,y=160)

    #address
    root.label_address = Label(root.bottom, text="  Address  ", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_address.place(x=140, y=200)
    root.entry_address = Text(root.bottom, width=23, height=5)
    root.entry_address.insert(1.0,person_address)
    root.entry_address.config(state='disabled')
    root.entry_address.place(x=270,y=200)

    #button
    viewButton = Button(root.bottom, text=" Home ", fg='white', bg='#fcc324', font='arial 12 bold',command=lambda: home(root))
    viewButton.place(x=300,y=300)  
        
def Display(person_id):
    root = Tk() 
    display(root,person_id)
    root.mainloop()

""" Delete Page """

def delete_person(root):
    selected_item = root.listBox.curselection()  
    person = root.listBox.get(selected_item)
    person_id = person.split(".")[0]
       
    query = "delete from phone_book where person_id = {};".format(person_id)
    answer = messagebox.askquestion("Warning","Are you sure you want to delete this contact?")
    if answer == 'yes':
        try:
            cur.execute(query)
            con.commit()
            messagebox.showinfo("Success", "Deleted")
            #root.destroy()
            home(root)
        except EXCEPTION as e:
            messagebox.showinfo("Info"), str(e)


""" Add New Person Page """

def addpeoplefunction(root):  
    root.destroy()
    AddPeople()

def Add_People(root):
    root.geometry("650x550+350+80")
    root.title("Add new Person")
    root.resizable(False, False)

    #frams
    root.top = Frame(root, height=150, bg='white') 
    root.top.pack(fill=X) 
    root.bottom = Frame(root, height=500, bg='#fcfc7e')
    root.bottom.pack(fill=X)

    #top frame design
    root.top_image = PhotoImage(file='icons/user.png')
    root.top_image_label = Label(root.top, image=root.top_image)
    root.top_image_label.place(x=120, y=10) 
    root.heading = Label(root.top, text = "Add new Person", font='Arial 15 bold', bg='white',fg='#ebb434')
    root.heading.place(x=210, y=30)

    #name
    root.label_name = Label(root.bottom, text="  Name  ", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_name.place(x=140, y=40)
    root.entry_name = Entry(root.bottom, width=30, bd=4)
    root.entry_name.insert(0,"")
    root.entry_name.place(x=270,y=40)

    #surname
    root.label_surname = Label(root.bottom, text="  Surname  ", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_surname.place(x=140, y=80)
    root.entry_surname = Entry(root.bottom, width=30, bd=4)
    root.entry_surname.insert(0,"")
    root.entry_surname.place(x=270,y=80)

    #email
    root.label_email = Label(root.bottom, text="  Email  ", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_email.place(x=140, y=120)
    root.entry_email = Entry(root.bottom, width=30, bd=4)
    root.entry_email.insert(0,"")
    root.entry_email.place(x=270,y=120)

    #phone number
    root.label_phone = Label(root.bottom, text="Phone Number", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_phone.place(x=140, y=160)
    root.entry_phone = Entry(root.bottom, width=30, bd=4)
    root.entry_phone.insert(0,"")
    root.entry_phone.place(x=270,y=160)

    #address
    root.label_address = Label(root.bottom, text="  Address  ", font='arial 12 bold', fg='white', bg='#fcc324')
    root.label_address.place(x=140, y=200)
    root.entry_address = Text(root.bottom, width=23, height=5)
    root.entry_address.place(x=270,y=200)

    #buttons
    button = Button(root.bottom, text="Add Person", font='arial 12 bold', fg='white', bg='#fcc324', command=lambda:add_people(root))
    button.place(x=225, y=300)

    viewButton = Button(root.bottom, text=" Home ", fg='white', bg='#fcc324', font='arial 12 bold',command=lambda: temp(root))
    viewButton.place(x=340,y=300)  

def add_people(root):
    name = root.entry_name.get()
    surname = root.entry_surname.get()    
    email = root.entry_email.get()
    phone = root.entry_phone.get()
    address = root.entry_address.get(1.0, 'end-1c')

    if name and surname and email and phone and address != "":
        try:
            #add to the database
            query="insert into 'phone_book' (person_name, person_surname, person_email, person_phone, person_address) values (?, ?, ?, ?, ?)"
            cur.execute(query, (name, surname, email, phone, address))
            con.commit()
            messagebox.showinfo("Success","Contact Added")
        except EXCEPTION as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Fill all the fields", icon='warning')

def AddPeople():
    root = Tk() 
    Add_People(root)
    root.mainloop() 

""" About Page """

def about_us(root):
    root.destroy()
    About()

def about(root):
    root.geometry("650x550+350+80")
    root.title("About")
    root.resizable(False, False)

    #frams
    root.top = Frame(root, height=550,width=550, bg='#ffa500') 
    root.top.pack(fill=BOTH) 

    root.text = Label(root.top, text="About \n\n @Auther: Fenil Patel \n@Date: 30-07-2021 \n@Technologies: Python and Sqlite \n\nIt is very nice application and \n very important to add any contact details.", font='arial 12 bold',bg='#ffa500',fg='white')
    root.text.place(x=170, y=50)

    root.viewButton = Button(root, text="Home", width=12, bg='white', fg='#42bcf5', font='arial 12 bold',command=lambda: home(root))
    root.viewButton.place(x=260,y=370)  
    
def About():
    root = Tk() 
    about(root)
    root.mainloop()

""" Home Page """

def start1(root):
    
    #frame
    root.top = Frame(root, height=150, bg='white') 
    root.top.pack(fill=X) 
    root.bottom = Frame(root, height=500, bg='#34baeb')
    root.bottom.pack(fill=X)
    
    #top frame design
    root.heading = Label(root.top, text = "My Phonebook", font='Arial 15 bold', bg='white',fg='#ebb434')
    root.heading.place(x=210, y=30)
    root.date_lbl = Label(root.top, text="Date:"+date, font='arial 15 bold', fg='#ebb434',bg='white')
    root.date_lbl.place(x=450, y=100)
    root.top_image = PhotoImage(file='icons/contact-book.png')
    root.top_image_label = Label(root.top, image=root.top_image)
    root.top_image_label.place(x=120, y=10) 
        
    #button1: login
    root.viewButton = Button(root.bottom, text="Login", width=11, bg='white', fg='#42bcf5', font='arial 12 bold',command=lambda: Login(root) )
    root.viewButton.place(x=270,y=70)  
    #button2: about us
    root.aboutButton = Button(root.bottom, text="About Us", width=11, bg='white', fg='#42bcf5', font='arial 12 bold', command=lambda:about_us(root))
    root.aboutButton.place(x=270,y=140)
    #button3: exit
    viewButton = Button(root.bottom, text="Exit", width=11, bg='white', fg='#42bcf5', font='arial 12 bold',command=lambda: exit(root))
    viewButton.place(x=270,y=210)  

def exit(root):
    answer = messagebox.askquestion("Warning","Are you sure you want to Exit?")
    if answer == 'yes':
        messagebox.showinfo("Success", "Please Visit Again!")
        root.destroy()

""" Login Page """

def Login(root):
    root.destroy()
    login()

def login_page(root):
    root.title("Login Page")
    root.geometry("650x550+350+60")
    root.resizable(0,0)
    root.configure(bg='#42bcf5')
    root.l1 = Label(root, text='Login Page', font='arial 20 bold',bg='#42bcf5')
    root.l1.place(x=250,y=100)
        
    root.L1 = Label(root, text="Username", font=("Arial Bold", 15),bg='#42bcf5')
    root.L1.place(x=150, y=180)
    root.T1 = Entry(root, width = 30, bd = 5)
    root.T1.place(x=260, y=180)
        
    root.L2 = Label(root, text="Password", font=("Arial Bold", 15),bg='#42bcf5')
    root.L2.place(x=150, y=230)
    root.T2 = Entry(root, width = 30, show='*', bd = 5)
    root.T2.place(x=260, y=230)
        
    def verify():
        try:
            with open("credential.txt", "r") as f:
                info = f.readlines()
                i  = 0
                for e in info:
                    u, p =e.split(",")
                    if u.strip() == root.T1.get() and p.strip() == root.T2.get():
                        start(root)    
                        i = 1
                        break
                if i==0:
                    messagebox.showinfo("Error", "Please provide correct username and password!!")
        except:
            messagebox.showinfo("Error", "Please provide correct username and password!!!")
     
    root.B1 = Button(root, text="Log In", bg = "dark orange", font='arial 12 bold', command=verify)
    root.B1.place(x=290, y=290)
    
    root.viewButton = Button(root, text="Home", width=12, bg='white', fg='#42bcf5', font='arial 12 bold',command=lambda: home(root))
    root.viewButton.place(x=260,y=360)     

def login():
    root = Tk() 
    login_page(root)
    root.mainloop() 

def temp(root):
    root.destroy()
    root = Tk() 
    check1(root)

def home(root):
    root.destroy()
    root = Tk() 
    start(root)

def main():
    root = Tk() 
    start1(root) 
    root.title("Phone Book")
    root.geometry("650x550+350+60")
    root.resizable(False, False)
    
    root.mainloop() 

if __name__=='__main__':
    main()    