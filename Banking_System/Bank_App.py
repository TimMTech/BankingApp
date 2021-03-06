'''
1.  Implement PostgreSQL Database to User Information Backend
2.  RESIZE APPLICATION(MAKE IT MORE REALISTIC)
  a. Test 500x500 geometry, but also center windows.
'''
#Imports
from tkinter import *
import os
from PIL import ImageTk, Image
from decimal import *

#Master Main Screen
master = Tk()
master.title("Banking Application")
#Centers the Main Screen
master.eval('tk::PlaceWindow . center')



#Finish Registration Function
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    recovery_answer = temp_recovery_answer.get()
    question = choice_selected
    all_accounts = os.listdir()

    if name == "" or age == "" or gender == "" or password == "" or recovery_answer == "" or choice_selected == "Security Question":
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
            new_file.write('0'+'\n')
            new_file.write(recovery_answer+'\n')
            new_file.write(question)
            new_file.close()
            notif.config(fg="green", text="Account has been created!")

def register():
    #Variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global temp_recovery_answer
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    temp_recovery_answer = StringVar()

    #Register screen
    register_screen = Toplevel(master)
    register_screen.title("Register")
    register_screen.geometry('290x275+600+350')

    #Register Screen Labels
    Label(register_screen, text="Please Enter Your Details Below", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", font=("Calibri",12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age", font=("Calibri",12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender", font=("Calibri",12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password", font=("Calibri",12)).grid(row=4,sticky=W)
    Label(register_screen, text="Answer", font=("Calibri",12)).grid(row=6,sticky=W)

    notif = Label(register_screen, font=("Calibri",12))
    notif.grid(row=8, sticky=N, pady=5)

    #Register Screen Entries
    Entry(register_screen, textvariable=temp_name).grid(row=1,padx=60)
    Entry(register_screen, textvariable=temp_age).grid(row=2,padx=60)
    Entry(register_screen, textvariable=temp_gender).grid(row=3,padx=60)
    Entry(register_screen, textvariable=temp_password, show="*").grid(row=4,padx=60)
    Entry(register_screen, textvariable=temp_recovery_answer, show="*").grid(row=6,padx=60)
    options = [
        "Security Question",
        "What is your Mother's last name?",
        "Do you have a dog or a cat?",
        "What month was your dad born?",
        "What public school did you attend?",
        "What was your first car?",
        "Name of first pet?",
        "What city were you born?",
        "High school name?",
        "Best friend's name growing up?"
    ]
    choice = StringVar()
    choice.set(options[0])
    choice_selected = options[0]

    #Cursor For OptionMenu Selection
    def _get(cur):
        global choice_selected
        choice_selected = cur
        print(choice_selected)

    question = OptionMenu(register_screen, choice, command=_get, *options)
    question.grid(row=5, sticky=N)

    #Register Screen Buttons
    Button(register_screen, text="Register", command= finish_reg, font=("Calibri",12)).grid(row=7,sticky=N,pady=10)

#Finish Login Function
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
                account_dashboard.geometry('245x200+600+350')

                #Account Dashboard Labels
                Label(account_dashboard, text="Account Dashboard",font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="Welcome "+ name,font=("Calibri",12)).grid(row=1,sticky=N,pady=5)

                #Account Dashboard Buttons
                Button(account_dashboard, text="Personal Details",font=("Calibri",12),width=30,command=personal_details).grid(row=3,sticky=N,pady=5)
                Button(account_dashboard, text="Deposit",font=("Calibri",12),width=30,command=deposit).grid(row=4,sticky=N,pady=5)
                Button(account_dashboard, text="Withdraw",font=("Calibri",12),width=30,command=withdraw).grid(row=5,sticky=N,pady=5)
                Button(account_dashboard, text="Change Password",font=("Calibri",12),width=30,command=change_pass).grid(row=6,sticky=N,pady=5)
                return
            else:
                login_notif.config(fg="red", text="Password Incorrect!!")
                return
    login_notif.config(fg="red", text="No Account Found!!")

def deposit():
    #Variables
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
    deposit_screen.geometry('230x200+600+350')

    #Deposit Screen Labels
    Label(deposit_screen, text="Deposit Information",font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(deposit_screen, text="Current Balance: $"+str(Decimal(details_balance)),font=("Calibri",12))
    current_balance_label.grid(row=1, sticky=W)
    Label(deposit_screen, text="Amount: ",font=("Calibri",12)).grid(row=2,sticky=W)
    deposit_notif = Label(deposit_screen,font=("Calibri",12))
    deposit_notif.grid(row=4, sticky=N, pady=5)

    #Deposit Screen Entries
    Entry(deposit_screen, textvariable=amount,width=10).grid(row=2,padx=60)

    #Deposit Screen Buttons
    Button(deposit_screen, text="Finish", font=("Calibri",12),command=finish_deposit).grid(row=3,sticky=N,pady=5)

#Finish Deposit Function
def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text="Amount is required", fg="red")
        return
    if Decimal(amount.get()) <= 0:
        deposit_notif.config(text="Negative currency is not accepted", fg="red")
        return
    file = open(username, "r+")
    file_data = file.read()
    details = file_data.split('\n')
    current_name = details[0]
    current_password = details[1]
    current_age = details[2]
    current_gender = details[3]
    current_balance = details[4]
    current_recovery_answer = details[5]
    current_question = details[6]
    updated_balance = current_balance
    updated_balance = Decimal(updated_balance) + Decimal(amount.get())
    new_file = open(username, "w")
    new_file.write(current_name + '\n')
    new_file.write(current_password + '\n')
    new_file.write(current_age + '\n')
    new_file.write(current_gender + '\n')
    new_file.write(str(updated_balance) + '\n')
    new_file.write(current_recovery_answer + '\n')
    new_file.write(current_question)
    new_file.close()

    current_balance_label.config(text="Current Balance: $"+str(updated_balance), fg="green")
    deposit_notif.config(text="Balance Updated", fg="green")

def withdraw():
    #Variables
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    file = open(username, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]

    #Withdraw Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title("Withdraw")
    withdraw_screen.geometry('230x200+600+350')

    #Withdraw Screen Labels
    Label(withdraw_screen, text="Withdrawal Information", font=("Calibri", 12)).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(withdraw_screen, text="Current Balance: $"+str(Decimal(details_balance)), font=("Calibri", 12))
    current_balance_label.grid(row=1, sticky=W)
    Label(withdraw_screen, text="Amount: ", font=("Calibri", 12)).grid(row=2, sticky=W)
    withdraw_notif = Label(withdraw_screen, font=("Calibri", 12))
    withdraw_notif.grid(row=4, sticky=N, pady=5)

    #Withdraw Screen Entries
    Entry(withdraw_screen, textvariable=withdraw_amount, width=10).grid(row=2, padx=60)

    #Withdraw Screen Buttons
    Button(withdraw_screen, text="Finish", font=("Calibri", 12), command=finish_withdraw).grid(row=3, sticky=N, pady=5)

#Finish Withdraw Function
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
    current_name = details[0]
    current_password = details[1]
    current_age = details[2]
    current_gender = details[3]
    current_balance = details[4]
    current_recovery_answer = details[5]
    current_question = details[6]

    if Decimal(withdraw_amount.get()) > Decimal(current_balance):
        withdraw_notif.config(text="Insufficient Funds!", fg="red")
        return

    updated_balance = current_balance
    updated_balance = Decimal(updated_balance) - Decimal(withdraw_amount.get())
    new_file = open(username, "w")
    new_file.write(current_name + '\n')
    new_file.write(current_password + '\n')
    new_file.write(current_age + '\n')
    new_file.write(current_gender + '\n')
    new_file.write(str(updated_balance) + '\n')
    new_file.write(current_recovery_answer + '\n')
    new_file.write(current_question)
    new_file.close()

    current_balance_label.config(text="Current Balance: $"+str(updated_balance), fg="green")
    withdraw_notif.config(text="Balance Updated", fg="green")

def change_pass():
    global change_notif
    global updated_password
    global attempt_password
    global current_password
    attempt_password = StringVar()
    updated_password = StringVar()
    file = open(username, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    current_password = user_details[1]

    #Change Password Screen
    change_pass_screen = Toplevel(master)
    change_pass_screen.title("Change Your Password")
    change_pass_screen.geometry('270x200+600+350')

    #Change Password Screen Labels
    Label(change_pass_screen, text="Enter Your Password Below", font=("Calibri", 12)).grid(row=1, sticky=N)
    Label(change_pass_screen, text="Password", font=("Calibri", 12)).grid(row=3, sticky=W)
    change_notif = Label(change_pass_screen, font=("Calibri", 12))
    change_notif.grid(row=7, sticky=N, pady=5)
    Label(change_pass_screen, text="Enter Your New Password Below", font=("Calibri", 12)).grid(row=4, sticky=N)
    Label(change_pass_screen, text="New Password", font=("Calibri", 12)).grid(row=5, sticky=W)

    #Change Password Screen Entries
    Entry(change_pass_screen, textvariable=attempt_password, width=10,show='*').grid(row=3)
    Entry(change_pass_screen, textvariable=updated_password, width=10,show='*').grid(row=5, padx=90)

    #Change Password Screen Buttons
    Button(change_pass_screen, text="Finish", font=("Calibri",12),command=finish_change).grid(row=6,sticky=N)

#Finish Change Password Function
def finish_change():
    file = open(username, "r+")
    file_data = file.read()
    details = file_data.split('\n')
    current_name = details[0]
    current_password = details[1]
    if attempt_password.get() != current_password:
        change_notif.config(text="Invalid Current Password.", fg='red')
        return
    if updated_password.get() == '':
        change_notif.config(text="Please Enter a Password.", fg='red')
        return
    current_age = details[2]
    current_gender = details[3]
    current_balance = details[4]
    current_recovery_answer = details[5]
    current_question = details[6]
    new_file = open(username, "w")
    new_file.write(current_name + '\n')
    new_file.write(str(updated_password.get()) + '\n')
    new_file.write(current_age + '\n')
    new_file.write(current_gender + '\n')
    new_file.write(current_balance + '\n')
    new_file.write(current_recovery_answer + '\n')
    new_file.write(current_question)
    new_file.close()

    change_notif.config(text="Password Updated!", fg='green')

def personal_details():
    #Variables
    file = open(username,'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[4]

    #Personal Details Screen
    personal_details_screen=Toplevel(master)
    personal_details_screen.title("Account Information")
    personal_details_screen.geometry('212x150+600+350')

    #Personal Details Screen Labels
    Label(personal_details_screen, text="Personal Details", font=("Calibri", 12),width=25).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text="Name: "+details_name, font=("Calibri", 12)).grid(row=1, sticky=N)
    Label(personal_details_screen, text="Age: "+details_age, font=("Calibri", 12)).grid(row=2, sticky=N)
    Label(personal_details_screen, text="Gender: "+details_gender, font=("Calibri", 12)).grid(row=3, sticky=N)
    Label(personal_details_screen, text="Balance: $"+details_balance, font=("Calibri", 12)).grid(row=4, sticky=N)

def login():
    #Variables
    global temp_username
    global temp_username_password
    global login_notif
    global login_screen
    temp_username = StringVar()
    temp_username_password = StringVar()

    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title("Login")
    login_screen.geometry('300x200+600+350')

    #Login Screen Labels
    Label(login_screen, text="Please Enter Your Login Details Below", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Username", font=("Calibri",12)).grid(row=1,sticky=W)
    Label(login_screen, text="Password", font=("Calibri",12)).grid(row=2,sticky=W)
    login_notif = Label(login_screen, font=("Calibri",12))
    login_notif.grid(row=5, sticky=N)

    #Login Screen Entries
    Entry(login_screen, textvariable=temp_username).grid(row=1, padx=70)
    Entry(login_screen, textvariable=temp_username_password, show="*").grid(row=2, padx=70)

    #Login Screen Buttons
    Button(login_screen, text="Login", command=login_session, font=("Calibri",12), width= 15).grid(row=3,sticky=N,pady=10)
    Button(login_screen, text="Forgot Password", command=forgot_user_pass, font=("Calibri",12), width= 20).grid(row=4,sticky=N)

def forgot_user_pass():
    #Variables
    global temp_username
    global temp_username_password
    global temp_recovery_answer
    global recovery_screen
    global recovery_notif
    temp_username = StringVar()
    temp_username_password = StringVar()
    temp_recovery_answer = StringVar()

    #Recovery Screen
    recovery_screen = Toplevel(master)
    recovery_screen.title("Recovery")
    recovery_screen.geometry('300x260+600+350')

    #Recovery Screen Labels
    Label(recovery_screen, text="Please Enter Your Username Below", font=("Calibri",12)).grid(row=0,sticky=N,padx=50)
    Label(recovery_screen, text="Username", font=("Calibri",12)).grid(row=1,sticky=W,pady=20)
    options = [
        "Security Question",
        "What is your Mother's last name?",
        "Do you have a dog or a cat?",
        "What month was your dad born?",
        "What public school did you attend?",
        "What was your first car?",
        "Name of first pet?",
        "What city were you born?",
        "High school name?",
        "Best friend's name growing up?"
    ]
    choice = StringVar()
    choice.set(options[0])
    choice_selected = options[0]

    #Cursor For OptionMenu Selection
    def _get(cur):
        global choice_selected
        choice_selected = cur
        print(choice_selected)
    question = OptionMenu(recovery_screen, choice,command=_get, *options)
    question.grid(row=2, sticky=N)

    Label(recovery_screen, text="Please Enter Your Answer Below", font=("Calibri",12)).grid(row=3,sticky=N,padx=50)
    Label(recovery_screen, text="Answer", font=("Calibri",12)).grid(row=4,sticky=W)

    recovery_notif = Label(recovery_screen, font=("Calibri", 12))
    recovery_notif.grid(row=6, sticky=N)

    #Recovery Screen Entries
    Entry(recovery_screen, textvariable=temp_username).grid(row=1, padx=70)
    Entry(recovery_screen, textvariable=temp_recovery_answer).grid(row=4, padx=70)

    #Recovery Screen Buttons
    Button(recovery_screen, text="Get Password", command=recovery_session, font=("Calibri",12), width= 20).grid(row=5,sticky=N,pady=20)

#Finish Recovery Function
def recovery_session():
    global username
    global answer
    all_accounts = os.listdir()
    username = temp_username.get()
    username_answer = temp_recovery_answer.get()
    for name in all_accounts:
        if name == username:
            file = open(name, 'r')
            file_data = file.read()
            file_data = file_data.split('\n')
            answer = file_data[5]
            password = file_data[1]
            question = file_data[6]

            #Account Recovery Screen
            if username_answer == answer and choice_selected == question:
                login_screen.destroy()
                recovery_screen.destroy()
                recovery_answer = Toplevel(master)
                recovery_answer.title("Recovery")
                recovery_answer.geometry('245x150+600+350')
                Label(recovery_answer, text="Welcome " + name, font=("Calibri",12)).grid(row=1,sticky=N,pady=5,padx=50)
                Label(recovery_answer, text="Your Password Below", font=("Calibri", 12)).grid(row=2, sticky=N, pady=10,padx=50)
                Label(recovery_answer, text=password, font=("Calibri", 12)).grid(row=3, sticky=N, pady=10,padx=50)
                return
            else:
                recovery_notif.config(fg="red", text="Answer or Question is Incorrect!")
                return
    recovery_notif.config(fg="red", text="No Account Found!")



#Master Screen Image Import
img = Image.open('banking.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Master Screen Labels
Label(master, text = "Custom Banking Beta", font=("Calibri",14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "The Most Secure Bank You Have Ever Used", font=("Calibri",12)).grid(row=1,sticky=N)
Label(master, image= img).grid(row=2, sticky=N,pady=15)

#Master Screen Buttons
Button(master, text = "Register", font=("Calibri", 12), width=20,command= register).grid(row=3,sticky=N)
Button(master, text = "Login", font=("Calibri", 12), width=20, command=login).grid(row=4,sticky=N,pady=5)


master.mainloop()
