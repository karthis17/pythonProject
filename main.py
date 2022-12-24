from tkinter import *
from tkinter import Tk
from DatabaseCon import DatabaseNew
from tkinter import messagebox

main = Tk()
main.title("IOB ATM")
main.geometry("920x720")
main.config(bg="#5f27cd")
main.state("zoomed")
main.resizable(False, False)

db = DatabaseNew("pack.db")
font = ("Poppins sans-serif", 48, "bold")
fg = "#ffffff"
bg = "#5f27cd"
mainframe = Frame(main, bg=bg)
mainframe.pack(fill=BOTH, expand=True)
Label(mainframe, text="I O B  B A N K", font=font, bg=bg, fg=fg).place(x=550, y=10)
Label(mainframe, text="W E L C O M E !", font=font, bg=bg, fg=fg).place(x=530, y=150)

Button(mainframe, text=">  New User", command=lambda *args: new_userspace(),
       activebackground=bg, activeforeground="#000000", bd=0,
       font=("Poppins san-serif", 28), bg="#5f27cd", fg=fg).place(x=10, y=500)
Button(mainframe, text="Existing User  <", command=lambda *args: exist_userspace(),
       activebackground=bg, activeforeground="#000000", font=("Poppins san-serif", 28),
       bd=0, bg=bg, fg=fg).place(x=1250, y=500)


def close(a, b):
    a.destroy()
    b.pack(fill=BOTH, expand=True)


def new_userspace():
    page = mainframe
    page.pack(fill="none", expand=False)
    newUSer = Frame(main, bg=bg)
    newUSer.pack(fill=BOTH, expand=True)
    Label(newUSer, text="I O B  B A N K", font=("Poppins", 38, "bold"), bg=bg, fg=fg).place(
        x=600, y=10)
    Label(newUSer, text="Fell Your Account Details", font=("Poppins", 28, "bold"), bg=bg,
          fg=fg).place(x=550, y=110)
    Label(newUSer, text="Credit/Debit Card.NO : ", bg=bg, font=("Poppins", 20)).place(x=50, y=220)
    ac_txt = Entry(newUSer, bg=bg, font=("Poppins", 22), width=22, borderwidth=2)
    ac_txt.place(x=330, y=225)
    ac_txt.insert(0, "XXXX-XXXX-XXXX-")
    Label(newUSer, text="Name : ", bg=bg, font=("Poppins", 26)).place(x=760, y=220)
    name_txt = Entry(newUSer, bg=bg, font=("Poppins", 22), width=22, borderwidth=2)
    name_txt.place(x=880, y=225)
    Label(newUSer, justify=RIGHT, text="Contact  :", bg=bg, font=("Poppins", 26)).place(x=50, y=380)
    contact_txt = Entry(newUSer, bg=bg, font=("Poppins", 22), width=22, borderwidth=2)
    contact_txt.place(x=330, y=385)
    Label(newUSer, text="Email :", bg=bg, font=("Poppins", 26)).place(x=760, y=380)
    email_txt = Entry(newUSer, bg=bg, font=("Poppins", 22), width=22, borderwidth=2)
    email_txt.place(x=880, y=385)
    Label(newUSer, text="Password : ", bg=bg, font=("Poppins", 26)).place(x=350, y=550)
    pass_txt = Entry(newUSer, bg=bg, font=("Poppins", 22), width=22, borderwidth=2)
    pass_txt.place(x=570, y=555)
    Button(newUSer, bg="#afafdd", font=("Poppins", 22, "bold"), width=10, command=lambda *args: add_db(),
           text="ADD").place(x=1250, y=700)
    Button(newUSer, bg="#afafdd", font=("Poppins", 22, "bold"), width=10,
           command=lambda *args: close(newUSer, mainframe), text="Back").place(x=1050, y=700)

    def add_db():
        try:
            if ac_txt.get() == "" or name_txt.get() == "" or contact_txt.get() == "" or email_txt.get() == "" or \
                    pass_txt.get() == "":
                messagebox.showerror("Error", "Please Fill all fields")
            else:
                db.insert(ac_txt.get(), name_txt.get(), contact_txt.get(), email_txt.get(), pass_txt.get())
                messagebox.showinfo("Success!", "Success now you consider as a existing account holder")
                newUSer.destroy()
                page.pack(fill=BOTH, expand=True)
        except E:
            messagebox.showwarning("Error!", "The user is already existing")


def exist_userspace():
    mainframe.pack_forget()
    login_frame = Frame(main, bg=bg)
    login_frame.pack(fill=BOTH, expand=True)
    Label(login_frame, text="I O B  B A N K", font=("Poppins", 38, "bold"), bg=bg,
          fg=fg).place(x=600, y=10)
    Label(login_frame, text="Credit/Debit Card.NO : ", bg=bg, font=("Poppins", 20)).place(x=200, y=220)
    eac_txt = Entry(login_frame, bg=bg, font=("Poppins", 22), width=22, borderwidth=2)
    eac_txt.place(x=480, y=225)
    eac_txt.insert(0, "XXXX-XXXX-XXXX-")
    Label(login_frame, text="Enter Your Password", bg="#5f27cd", font=("poppins", 28, "bold")).place(x=550, y=400)
    entry_text = StringVar()  # the text in  your entry
    entry_widget = Entry(login_frame, show='X', font=("poppins", 68), width=5, bg="#5f27cd",
                         textvariable=entry_text)  # the entry
    entry_widget.place(x=590, y=500)  #
    entry_text.trace("w", lambda *args: character_limit(entry_text))
    Button(login_frame, bg="#afafdd", font=("Poppins", 22, "bold"), width=10, text="Enter",
           command=lambda *args: enter()).place(x=1250, y=700)
    Button(login_frame, bg="#afafdd", font=("Poppins", 22, "bold"), width=10, text="Back",
           command=lambda *args: close(login_frame, mainframe)).place(x=1050, y=700)

    def character_limit(entry):
        if len(entry.get()) > 4:
            entry.set(entry.get()[4:])

    def enter():
        account = eac_txt.get()
        password = entry_widget.get()
        rows = db.fetchonee(eac_txt.get(), entry_widget.get())
        if rows is None:
            messagebox.showerror("error", "Card Number or Password incorrect So please enter valid information")
        else:
            login_frame.destroy()
            function_page(account, password)


def function_page(account, password):
    function_frame = Frame(main, bg=bg)
    function_frame.pack(fill=BOTH, expand=True)
    Label(function_frame, text="I O B  B A N K", font=("Poppins", 38, "bold"), bg=bg,
          fg=fg).place(x=600, y=10)
    Button(function_frame, text=">  Holder Detail", command=lambda *args: userdata(function_frame, account, password),
           activebackground=bg, activeforeground="#000000", bd=0, font=("Poppins san-serif", 28),
           bg="#5f27cd", fg=fg).place(x=10, y=500)
    Button(function_frame, text="Withdraw  <", command=lambda *args: withdraw(function_frame, account, password),
           activebackground=bg, activeforeground="#000000", font=("Poppins san-serif", 28), bd=0,
           bg=bg, fg=fg).place(x=1300, y=510)
    Button(function_frame, text=">  Deposit", command=lambda *args: deposit(function_frame, account, password),
           activebackground=bg, activeforeground="#000000", bd=0, font=("Poppins san-serif", 28),
           bg="#5f27cd", fg=fg).place(x=10, y=590)
    Button(function_frame, text="Quic Balance Check  <",
           command=lambda *args: balance_check(function_frame, account, password), activebackground=bg,
           activeforeground="#000000", font=("Poppins san-serif", 28), bd=0, bg=bg,
           fg=fg).place(x=1100, y=600)
    Button(function_frame, bg="#afafdd", font=("Poppins", 22, "bold"), width=10,
           command=lambda *args: close(function_frame, mainframe), text="Back").place(
        x=1250, y=740)


def userdata(function_frame, account, password):
    function_frame.pack_forget()
    userdata_frame = Frame(main, bg=bg)
    userdata_frame.pack(fill=BOTH, expand=True)
    Label(userdata_frame, text="Account Holder", font=("Poppins", 28, "bold"), bg=bg,
          fg=fg).place(x=600, y=10)
    Label(userdata_frame, font=("Poppins", 28, "bold"), bg=bg, text="Card NO :").place(x=50, y=180)
    Label(userdata_frame, bg=bg, text="Name  :", font=("Poppins", 28, "bold")).place(x=50, y=280)
    Label(userdata_frame, bg=bg, text="Mobile.No :", font=("Poppins", 28, "bold")).place(x=50, y=380)
    Label(userdata_frame, bg=bg, text="Email ID :", font=("Poppins", 28, "bold")).place(x=50, y=480)
    acct = Label(userdata_frame, font=("Poppins", 28, "bold"), bg=bg)
    acct.place(x=240, y=180)
    names = Label(userdata_frame, bg=bg, font=("Poppins", 28, "bold"))
    names.place(x=240, y=280)
    MobX = Label(userdata_frame, bg=bg, font=("Poppins", 28, "bold"))
    MobX.place(x=290, y=380)
    emil = Label(userdata_frame, bg=bg, font=("Poppins", 28, "bold"))
    emil.place(x=240, y=480)
    for row in db.fetch(account, password):
        acct.config(text=row[0])
        names.config(text=row[1])
        MobX.config(text=row[2])
        emil.config(text=row[3])
    Button(userdata_frame, bg="#afafdd", font=("Poppins", 22, "bold"), width=10,
           command=lambda *args: close(userdata_frame, function_frame), text="Back").place(x=1250, y=720)


def deposit(function_frame, account, password):
    function_frame.pack_forget()
    deposit_frame = Frame(main, bg=bg)
    deposit_frame.pack(fill=BOTH, expand=True)
    Label(deposit_frame, text="DEPOSIT", font=("Poppins", 38, "bold"), bg=bg, fg=fg).place(x=640, y=10)
    Label(deposit_frame, text="Type Your Deposit Amount Here ", font=("Poppins", 28, "bold"), bg=bg, fg=fg) \
        .place(x=450, y=410)
    amount_txt = Entry(deposit_frame, bg=bg, font=("Poppins", 30), width=22, borderwidth=2)
    amount_txt.place(x=500, y=500)
    Button(deposit_frame, bg="#afafdd", font=("Poppins", 22, "bold"), width=10,
           command=lambda *args: close(deposit_frame, function_frame), text="Back").place(x=1050, y=700)
    Button(deposit_frame, bg="#afafdd", font=("Poppins", 22, "bold"), width=10, command=lambda *args: add(),
           text="ADD").place(x=1250, y=700)

    def add():
        for row in db.fetch(account, password):
            balance = int(row[5]) + int(amount_txt.get())
            try:
                db.updateData(balance, account)
                messagebox.showinfo("Success!", "The account has been Deposited to your account")
                deposit_frame.destroy()
                function_frame.pack(fill=BOTH, expand=True)
            except E:
                messagebox.showerror("Error", "Something went wrong")


def balance_check(function_frame, account, password):
    function_frame.pack_forget()
    balance_frame = Frame(main, bg=bg)
    balance_frame.pack(fill=BOTH, expand=True)
    Label(balance_frame, text="BALANCE", font=("Poppins", 38, "bold"), bg=bg, fg=fg).place(x=640, y=10)
    Label(balance_frame, text="Your Account Balance  :", bg=bg,
          font=('opines', 28, 'bold')).place(x=250, y=400)
    balance_txt = Entry(balance_frame, bg=bg, font=("Poppins", 40), width=15, borderwidth=2)
    balance_txt.place(x=500, y=500)
    for row in db.fetch(account, password):
        balance_txt.insert(0, row[5])
    Button(balance_frame, bg="#afafdd", font=("Poppins", 22, "bold"), width=10,
           command=lambda *args: close(balance_frame, function_frame), text="Back").place(x=1050, y=700)


def withdraw(function_frame, account, password):
    function_frame.pack_forget()
    withdraw_frame = Frame(main, bg=bg)
    withdraw_frame.pack(fill=BOTH, expand=True)
    Label(withdraw_frame, text="WITHDRAW", font=("Poppins", 38, "bold"), bg=bg, fg=fg).place(
        x=640, y=10)
    Label(withdraw_frame, text="Enter Amount Here  :", font=('opines', 28, 'bold'),
          bg=bg).place(x=250, y=400)
    withdraw_txt = Entry(withdraw_frame, bg=bg, font=("Poppins", 40), width=15, borderwidth=2)
    withdraw_txt.place(x=500, y=500)
    Button(withdraw_frame, bg="#afafdd", font=("Poppins", 22, "bold"), width=10,
           command=lambda *args: close(withdraw_frame, function_frame), text="Back").place(x=1050, y=700)
    Button(withdraw_frame, bg="#afafdd", font=("Poppins", 22, "bold"), width=10, command=lambda *args: add_data(),
           text="Correct").place(x=1250, y=700)

    def add_data():
        for row in db.fetch(account, password):
            balance = int(row[5]) - int(withdraw_txt.get())
            try:
                db.updateData(balance, account)
                messagebox.showinfo("Success!", "The account has been withdraw from your account")
                withdraw_frame.destroy()
                function_frame.pack(fill=BOTH, expand=True)
            except E:
                messagebox.showerror("Error", "Something went wrong")


main.mainloop()
