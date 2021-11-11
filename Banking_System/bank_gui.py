'''
'''
#imports
from tkinter import *
import os
from PIL import ImageTk, Image
from decimal import *

#Main Screen
master = Tk()
master.title("Banking Application")
#Centers the Main Screen
master.eval('tk::PlaceWindow . center')



#Functions
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if name == "" or age == "" or gender == "" or password == "":
        notif.config(fg="red", text="All Fields are Required * ")
        return
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red", text="Account already exists")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write('0')
            new_file.close()
            notif.config(fg="green", text="Account has been created!")


def register():
    #variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    #register screen
    register_screen = Toplevel(master)
    register_screen.title("Register")
    register_screen.geometry('300x250+600+500')


    #labels
    Label(register_screen, text="Please Enter Your Details Below", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", font=("Calibri",12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age", font=("Calibri",12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender", font=("Calibri",12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password", font=("Calibri",12)).grid(row=4,sticky=W)
    notif = Label(register_screen, font=("Calibri",12))
    notif.grid(row=6, sticky=N, pady=10)

    #entries
    Entry(register_screen, textvariable=temp_name).grid(row=1,padx=60)
    Entry(register_screen, textvariable=temp_age).grid(row=2,padx=60)
    Entry(register_screen, textvariable=temp_gender).grid(row=3,padx=60)
    Entry(register_screen, textvariable=temp_password, show="*").grid(row=4,padx=60)

    #buttons
    Button(register_screen, text="Register", command= finish_reg, font=("Calibri",12)).grid(row=5,sticky=N,pady=10)
#Functions
def login_session():
    global username
    all_accounts = os.listdir()
    username = temp_username.get()
    username_password = temp_username_password.get()
    for name in all_accounts:
        if name == username:
            file = open(name,'r')
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            #Account Dashboard
            if username_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Dashboard")
                account_dashboard.geometry('245x200+600+500')
                #Labels
                Label(account_dashboard, text="Account Dashboard",font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="Welcome "+ name,font=("Calibri",12)).grid(row=1,sticky=N,pady=5)
                #Buttons
                Button(account_dashboard, text="Personal Details",font=("Calibri",12),width=30,command=personal_details).grid(row=3,sticky=N,pady=5)
                Button(account_dashboard, text="Deposit",font=("Calibri",12),width=30,command=deposit).grid(row=4,sticky=N,pady=5)
                Button(account_dashboard, text="Withdraw",font=("Calibri",12),width=30,command=withdraw).grid(row=5,sticky=N,pady=5)


                return
            else:
                login_notif.config(fg="red", text="Password Incorrect!!")
                return
    login_notif.config(fg="red", text="No Account Found!!")



def deposit():
    #Vars
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()
    file = open(username,'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]

    #Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title("Deposit")
    deposit_screen.geometry('230x200+600+500')
    #Label
    Label(deposit_screen, text="Deposit Information",font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(deposit_screen, text="Current Balance: $"+str(Decimal(details_balance)),font=("Calibri",12))
    current_balance_label.grid(row=1, sticky=W)
    Label(deposit_screen, text="Amount: ",font=("Calibri",12)).grid(row=2,sticky=W)
    deposit_notif = Label(deposit_screen,font=("Calibri",12))
    deposit_notif.grid(row=4, sticky=N, pady=5)
    #Entry
    Entry(deposit_screen, textvariable=amount,width=10).grid(row=2,padx=60)
    #Button
    Button(deposit_screen, text="Finish", font=("Calibri",12),command=finish_deposit).grid(row=3,sticky=N,pady=5)


def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text="Amount is required", fg="red")
        return
    if Decimal(amount.get()) <= 0:
        deposit_notif.config(text="Negative currency is not accepted", fg="red")
    file = open(username, "r+")
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = current_balance
    updated_balance = Decimal(updated_balance) + Decimal(amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance: $"+str(Decimal(updated_balance)), fg="green")
    deposit_notif.config(text="Balance Updated", fg="green")

def withdraw():
    # Vars
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file = open(username, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]



    # Withdraw Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("Withdraw")
    withdraw_screen.geometry('230x200+600+500')
    # Label
    Label(withdraw_screen, text="Withdrawal Information", font=("Calibri", 12)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(withdraw_screen, text="Current Balance: $" +'{0:.2f}'.format(float(details_balance)), font=("Calibri", 12))
    current_balance_label.grid(row=1, sticky=W)
    Label(withdraw_screen, text="Amount: ", font=("Calibri", 12)).grid(row=2, sticky=W)
    withdraw_notif = Label(withdraw_screen, font=("Calibri", 12))
    withdraw_notif.grid(row=4, sticky=N, pady=5)
    # Entry
    Entry(withdraw_screen, textvariable=withdraw_amount, width=10).grid(row=2, padx=60)
    # Button
    Button(withdraw_screen, text="Finish", font=("Calibri", 12), command=finish_withdraw).grid(row=3, sticky=N, pady=5)

def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text="Amount is required", fg="red")
        return
    if Decimal(withdraw_amount.get()) <= 0:
        withdraw_notif.config(text="Negative currency is not accepted", fg="red")
        return
    file = open(username, "r+")
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]

    if Decimal(withdraw_amount.get()) > Decimal(current_balance):
        withdraw_notif.config(text="Insufficient Funds!", fg="red")
        return

    updated_balance = current_balance
    updated_balance = Decimal(updated_balance) - Decimal(withdraw_amount.get())
    file_data = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    current_balance_label.config(text="Current Balance: $"+str(Decimal(updated_balance)), fg="green")
    withdraw_notif.config(text="Balance Updated", fg="green")

def personal_details():
    #Vars
    file = open(username,'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[4]
    #personal details screen
    personal_details_screen=Toplevel(master)
    personal_details_screen.title("Account Information")
    personal_details_screen.geometry('212x150+600+500')

    #labels
    Label(personal_details_screen, text="Personal Details", font=("Calibri", 12),width=25).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text="Name: "+details_name, font=("Calibri", 12)).grid(row=1, sticky=N)
    Label(personal_details_screen, text="Age: "+details_age, font=("Calibri", 12)).grid(row=2, sticky=N)
    Label(personal_details_screen, text="Gender: "+details_gender, font=("Calibri", 12)).grid(row=3, sticky=N)
    Label(personal_details_screen, text="Balance: $"+details_balance, font=("Calibri", 12)).grid(row=4, sticky=N)


def login():
    #variables
    global temp_username
    global temp_username_password
    global login_notif
    global login_screen
    temp_username = StringVar()
    temp_username_password = StringVar()
    #login screen
    login_screen = Toplevel(master)
    login_screen.title("Login")
    login_screen.geometry('300x175+600+500')

    #labels
    Label(login_screen, text="Please Enter Your Login Details Below", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Username", font=("Calibri",12)).grid(row=1,sticky=W)
    Label(login_screen, text="Password", font=("Calibri",12)).grid(row=2,sticky=W)
    login_notif = Label(login_screen, font=("Calibri",12))
    login_notif.grid(row=4, sticky=N)

    #entries
    Entry(login_screen, textvariable=temp_username).grid(row=1, padx=70)
    Entry(login_screen, textvariable=temp_username_password, show="*").grid(row=2, padx=70)

    #buttons
    Button(login_screen, text="Login", command=login_session, font=("Calibri",12), width= 15).grid(row=3,sticky=N,pady=10)


#Image Import
img = Image.open('banking.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Labels
Label(master, text = "Custom Banking Beta", font=("Calibri",14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "The Most Secure Bank You Have Ever Used", font=("Calibri",12)).grid(row=1,sticky=N)
Label(master, image= img).grid(row=2, sticky=N,pady=15)

#Buttons
Button(master, text = "Register", font=("Calibri", 12), width=20,command= register).grid(row=3,sticky=N)
Button(master, text = "Login", font=("Calibri", 12), width=20, command=login).grid(row=4,sticky=N,pady=5)




master.mainloop()
