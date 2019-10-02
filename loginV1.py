import tkinter
window = tkinter.Tk()
window.title("Login")

window.geometry("300x200")

lbUsername = tkinter.Label(window, text = "Username")
lbUsername.place(x=0, y=0)
txtUsername = tkinter.Entry(window)
txtUsername.place(x=60, y=0)

lbPassword = tkinter.Label(window, text = "Password") 
lbPassword.place(x=0, y=25)
txtPassword = tkinter.Entry(window, show="*")
txtPassword.place(x=60, y=25) 


btLogin = tkinter.Button(window, text = "LogIn")
btLogin.place(x= 60, y=50)

def GoToCreateAccount():
    window.title("Create Account")
    lbCUsername = tkinter.Label(window, text = "Create Username")
    lbCUsername.place(x=0, y=0)
    txtCUsername = tkinter.Entry(window)
    txtCUsername.place(x=100, y=0)

    lbCPassword = tkinter.Label(window, text = "Create Password") 
    lbCPassword.place(x=0, y=25)
    txtCPassword = tkinter.Entry(window, show="*")
    txtCPassword.place(x=100, y=25)
    
    lbRPassword = tkinter.Label(window, text = "Repeat Password") 
    lbRPassword.place(x=0, y=50)
    txtRPassword = tkinter.Entry(window, show="*")
    txtRPassword.place(x=100, y=50)

    btCreateAccount2 = tkinter.Button(window, text="Create Account")
    btCreateAccount2.place(x=60, y=75)

    btIHaveAnAccount = tkinter.Button(window, text="I Have An Account")
    btIHaveAnAccount.place(x=60, y=100)
    
    lbUsername.destroy()
    lbPassword.destroy()
    txtPassword.destroy()
    txtUsername.destroy()
    btLogin.destroy()
    btCreateAccount.destroy()
    
btCreateAccount = tkinter.Button(window, text = "Create Account", command=GoToCreateAccount)
btCreateAccount.place(x=60, y=75) 

window.mainloop()
