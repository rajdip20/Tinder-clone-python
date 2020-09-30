from tkinter import *

def check_login():
    # print(email.get())
    # print(password.get())

    if email.get() == 'dasrajdip78754282@gmail.com' and password.get() == '9932894715':
        result.config(text="Welcome", font=("Arial", 30))
    else:
        result.config(text="Incorrect", font=("Arial", 30))


root = Tk()

root.title("Tinder Login")

root.minsize(400, 600)

heading = Label(root, text="Login Here")
heading.config(font=("Times", 20))
heading.pack(pady=(30, 30))

email_label = Label(root, text="Enter Email:")
email_label.config(font=("Arial", 16))
email_label.pack(pady=(10, 10))

email = Entry(root)
email.pack(pady=(5, 20))

password_label = Label(root, text="Enter Password:")
password_label.config(font=("Arial", 16))
password_label.pack(pady=(5, 10))

password = Entry(root)
password.pack(pady=(5, 20))

login = Button(root, text="Login", command=lambda: check_login())
login.pack(pady=(5, 30))

result = Label(root)
result.pack()

root.mainloop()