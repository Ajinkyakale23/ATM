#Importing the required modules
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

def checkAuth():
    accno = accNo.get()
    otp = otp.get()
    action = action.get()
    if accno & otp & action:
        if action == 'withdraw':
            withDraw()
            print("hi")
    else:
        return False

# Function to heckauthentication for Atm 
def authenticationPage():
    global accNo, otp,  Canvas2,  wn
    print("hi1")
    #Creating the window
    wn = tkinter.Tk() 
    wn.title("Atm Machine")
    wn.configure(bg='mint cream')
    wn.minsize(width=400,height=400)
    wn.geometry("500x600")

    Canvas2 = Canvas(wn)
    Canvas2.config(bg='LightBlue1')
    Canvas2.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(wn,bg='LightBlue1',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="** Welcome To ATM **", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # Account Number
    lable1 = Label(labelFrame,text="Account Number : ", fg='black')
    lable1.place(relx=0.05,rely=0.45, relheight=0.08)
        
    accNo = Entry(labelFrame)
    accNo.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)

    # Enter OTP
    lable2 = Label(labelFrame,text="Enter Otp : ", fg='black')
    lable2.place(relx=0.05,rely=0.6, relheight=0.08)
        
    otp = Entry(labelFrame)
    otp.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

   #Submit Button
    Btn = Button(wn,text="Submit",bg='#d1ccc0', fg='black',command=checkAuth)
    Btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    #Back Button
    btn2 = Button(wn,text="Back",bg='#f7f1e3', fg='black',)
    btn2.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)

    wn.mainloop()
    

# Function to Withdraw Amount from Atm 
def withDraw():
    action = 'withdraw'
    print(action)
    authenticationPage()
    global accNo, withdraw,  Canvas1,  wn 
    
    
    # #Creating the window
    # wn = tkinter.Tk() 
    # wn.title("Atm Machine")
    # wn.configure(bg='mint cream')
    # wn.minsize(width=400,height=400)
    # wn.geometry("500x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg='LightBlue1')
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(wn,bg='LightBlue1',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="** Welcome To ATM **", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # Account Number
    lable1 = Label(labelFrame,text="Account Number : ", fg='black')
    lable1.place(relx=0.05,rely=0.45, relheight=0.08)
        
    accNo = Entry(labelFrame)
    accNo.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)

    # Enter Amount For Withdraw
    lable2 = Label(labelFrame,text=" Withdraw Amount : ", fg='black')
    lable2.place(relx=0.05,rely=0.6, relheight=0.08)
        
    withdraw = Entry(labelFrame)
    withdraw.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

   #Submit Button
    Btn = Button(wn,text="Submit",bg='#d1ccc0', fg='black',)
    Btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    #Back Button
    btn2 = Button(wn,text="Back",bg='#f7f1e3', fg='black',)
    btn2.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)

    wn.mainloop()

# Function to Deposit Amount
def depositAmt():
    authenticationPage()
    global accNo, amt,  Canvas1,  wn
    
    # #Creating the window
    # wn = tkinter.Tk() 
    # wn.title("Atm Machine")
    # wn.configure(bg='mint cream')
    # wn.minsize(width=400,height=400)
    # wn.geometry("500x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg='misty rose')
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(wn,bg='misty rose',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="** Welcome To ATM **", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.0,relheight=0.4)

    # Account Number
    lable1 = Label(labelFrame,text="Account Number : ", fg='black')
    lable1.place(relx=0.05,rely=0.45, relheight=0.08)
        
    accNo = Entry(labelFrame)
    accNo.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)

    # Enter Amount
    lable2 = Label(labelFrame,text="Deposit Amount : ", fg='black')
    lable2.place(relx=0.05,rely=0.6, relheight=0.08)
        
    amt = Entry(labelFrame)
    amt.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

   #Submit Button
    Btn = Button(wn,text="Submit",bg='#d1ccc0', fg='black',)
    Btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    #Back Button
    btn = Button(wn,text="back",bg='#f7f1e3', fg='black',)
    btn.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)

    wn.mainloop()


# Function to Check Balances
def checkBal():
    authenticationPage()
    global accNo, checkbal,  Canvas1,  wn
    
    #Creating the window
    # wn = tkinter.Tk() 
    # wn.title("Atm Machine")
    # wn.configure(bg='mint cream')
    # wn.minsize(width=400,height=400)
    # wn.geometry("500x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg='old lace')
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(wn,bg='old lace',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="** Welcome To ATM **", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # Account Number
    lable1 = Label(labelFrame,text="Account Number : ", fg='black')
    lable1.place(relx=0.05,rely=0.45, relheight=0.08)
        
    accNo = Entry(labelFrame)
    accNo.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)

    # To Check Balances
    lable2 = Label(labelFrame,text="Balance : ", fg='black')
    lable2.place(relx=0.05,rely=0.6, relheight=0.08)
        
    checkbal = Entry(labelFrame)
    checkbal.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

   #Submit Button
    Btn = Button(wn,text="Submit",bg='#d1ccc0', fg='black',)
    Btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    #Back Button
    btn2 = Button(wn,text="Back",bg='#f7f1e3', fg='black',)
    btn2.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)

    wn.mainloop()


# Function to Change Pin
def changePin():
    authenticationPage()
    global accNo, pin, pinn, Canvas1,  wn
    
    #Creating the window
    # wn = tkinter.Tk() 
    # wn.title("Atm Machine")
    # wn.configure(bg='mint cream')
    # wn.minsize(width=400,height=400)
    # wn.geometry("500x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg='lavender blush2')
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(wn,bg='lavender blush2',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="** Welcome To ATM **", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # Account Number
    lable1 = Label(labelFrame,text="Account Number : ", fg='black')
    lable1.place(relx=0.05,rely=0.45, relheight=0.08)
        
    accNo = Entry(labelFrame)
    accNo.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)

    # Old Pin
    lable2 = Label(labelFrame,text=" Old Pin : ", fg='black')
    lable2.place(relx=0.05,rely=0.6, relheight=0.08)
        
    pin = Entry(labelFrame)
    pin.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

    # New Pin
    lable3 = Label(labelFrame,text=" New Pin : ", fg='black')
    lable3.place(relx=0.05,rely=0.45, relheight=0.08)
        
    pinn = Entry(labelFrame)
    pinn.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

   #Submit Button
    Btn = Button(wn,text="Submit",bg='#d1ccc0', fg='black',)
    Btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)

    #Back Button
    btn2 = Button(wn,text="Back",bg='#f7f1e3', fg='black',)
    btn2.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)

    wn.mainloop()
        
def showHomePage():

    #Button to Withdraw
    btn1 = Button(wn,text="Withdraw Amount",bg='LightBlue1', fg='black', width=20,height=2,command=withDraw )
    btn1['font'] = font.Font( size=12)
    btn1.place(x=270,y=175)

    #Button to Deposit
    btn2 = Button(wn,text="Deposit Amount",bg='misty rose', fg='black', width=20,height=2,command=depositAmt)
    btn2['font'] = font.Font( size=12)
    btn2.place(x=270,y=255)

    #Button to Balance
    btn3 = Button(wn,text="Balance Amount",bg='old lace', fg='black', width=20,height=2,command=checkBal)
    btn3['font'] = font.Font( size=12)
    btn3.place(x=270,y=335)

    #Button to Pin Change
    btn4 = Button(wn,text="Pin Change",bg='lavender blush2', fg='black', width=20,height=2,command=changePin)
    btn4['font'] = font.Font( size=12)
    btn4.place(x=270,y=415)



#Creating the mail window
wn = tkinter.Tk() 
wn.title("Atm Machine")
wn.configure(bg='honeydew2')
wn.minsize(width=500,height=500)
wn.geometry("700x600")

headingFrame1 = Frame(wn,bg="snow3",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to Python Prjoect \n Atm Machine", fg='grey19', font=('Courier',15,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
showHomePage()

wn.mainloop() 