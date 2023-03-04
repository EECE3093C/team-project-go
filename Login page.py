from tkinter import*

class Login:
   def __init__(self, root):
        self.root = root
        self.root.title("LoginEasy")
        self.root.geometry("1200x600")



        Frame_Login = Frame(self.root, bg="light blue")
        Frame_Login.place(x=350, y=150, width= 500, height= 300)

        title = Label(Frame_Login, text="Welcome", font=("Impact", 38), fg="black" ,bg="light blue").place(x=70, y=30)
        title2 = Label(Frame_Login, text="username", font=("Impact",15), fg="black",bg="light blue").place(x=70, y=125)
        title3 = Label(Frame_Login, text="password", font=("Impact",15), fg="black",bg="light blue").place(x=70, y=170)

root = Tk()
obj = Login(root)
root.mainloop()
