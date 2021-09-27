import Customer_Register
import Customer_bookingPage # import booking
from tkinter import *
from tkinter import messagebox
import sys
sys.path.append( ".")
import Database



class Login:
    def __init__(self, root):
                
        #gui interface window
        self.root = root
        self.root.title('Taxi Booking System - Login')
        window_width = 300
        window_height = 300

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        #login heading   TITLE
        heading = Label(self.root, text = 'Login' , fg= 'green', font=' Times 24')
        heading.pack()

        # variables declaration
        self.email = StringVar()
        self.password = StringVar()
        self.customerID = StringVar()

        # stores label and entry fields
        frame = Frame(self.root)
        frame.pack(padx= 10, pady= 10)
        # store buttons
        buttonFrame = Frame(self.root)
        buttonFrame.place( x = 100, y = 180)

        # email address 
        lbl_email = Label(frame, text = 'Email ID' )
        lbl_email.grid(row = 0, column = 0,  padx = 20, pady = 20)
        txt_email = Entry(frame, textvariable= self.email)
        txt_email.grid(row = 0, column = 1)

        #password
        lbl_password = Label(frame, text = 'Password')
        lbl_password.grid(row=1, column=0)

        password = Entry(frame,  show = '*' , textvariable= self.password)
        password.grid(row=1, column=1)

        btn_login = Button(buttonFrame, text = 'Login',  height = 1, bg = 'green', fg= 'white', command= self.login)
        btn_login.grid(row= 0, column= 0)

        btn_register = Button(buttonFrame, text= ' Register', width= -1, height= 1, bg = 'lightblue', fg= 'black', command= self.registrationForm).grid(row= 0, column= 1, padx= 10)
        

    # calling new window form another class
    def login(self):

        try:
            Database.cursor.execute("select * from customer where Email = %s and Password = %s ",(self.email.get(), self.password.get()))
            row = Database.cursor.fetchone()
            print(row)
            
            self.customerID.set(row[0])
            print('customer ID :', self.customerID.get())
        
            if row != None:
                self.root.destroy()
                root = Tk()  # Creating instance of Tk class
                obj = Customer_bookingPage.booking(root, self.customerID.get())
                root.mainloop()
                
            else:
                messagebox.showerror('Error', 'User Not Found',parent=self.root)
        except TypeError:
            messagebox.showerror("Error", "User not Found !!!")


    # calling new window form another class
    def registrationForm(self):
        self.root.destroy()
        root = Tk()  # Creating instance of Tk class
        obj = Customer_Register.Customer_register(root)
        root.mainloop()
        
    
# main method
if __name__ == '__main__':
    root = Tk()
    Login(root)
    root.mainloop()

