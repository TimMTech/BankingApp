# Banking GUI
+
-This is a Tkinter Library-based Banking Application.

-Modules used:
1. Tkinter 
2. PIL
3. OS
4. decimal(Currency)


When you run the application, it opens a centered 
GUI window that asks for the user to either
register or log in.

Register:
Once you click on the register button, it opens
a new screen that asks you to input you Name, Age,
Gender, your password(* hidden), select a recovery question and
provide the answer(* hidden)
Once you press register, it will save the user information
into its own separate txt file.  
Note:  If the account already exists, a message below
the register button will prompt "Account Exists"

Login:
Once you click on the login button, it opens a new screen
that asks you to input your login credentials.
Note:  If password or user is incorrect, invalid message
will prompt below the Login button.

Forgot Password - Opens a new window named "Recovery".  User
will have to input their username, select the appropriate 
recovery question that they have chosen during the registration
session and provide the correct answer to that security question.
If Username is incorrect, an error message will prompt below 
the Get Password button.  If security question or answer does
not match the user's records, an error message will prompt.

Once logged in successfully, you will be brought to your
respective account's dashboard.

Three options:

Personal Details - Shows the users' personal details, such as 
Name, Age, Gender and Balance.
(NEVER THE PASSWORD OR RECOVERY QUESTION/ANSWER)

Deposit - Opens a new window that allows User to deposit 
a specific amount in decimal form.  Will also show the User's
current balance.  If deposited amount is either a negative
or the integer 0, an error message will prompt below the finish
button.
If deposit is successful, a message will prompt that 
Account has been updated!

Withdraw - Opens a new window that allows User to withdraw
a specific amount in decimal form.  Will also show the User's
current balance.  If withdrawal amount is either a negative 
or the integer 0, an error message will prompt below the finish 
button.  An error wil ALSO show if the amount withdrawn
exceeds the current balance amount.
If withdrawal is successful, a message will prompt that
Account has been updated!

Change Password - Opens a new window named "Change Password".  User
will have to input their current password and a desired new
password.  If the current password does not match with user's
records, an error message will prompt.  If user inputs correct
current password but leaves the new password entry blank, an 
error message will prompt.  Once both entries are correctly
filled out, the user will then successfully have changed their
password.

All successful updates will be saved into the respective
User's text file.

Will continue to work on new updates...
Will also implement an SQL database for specific Users...
