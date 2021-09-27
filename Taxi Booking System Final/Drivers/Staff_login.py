import sys
import tkinter
sys.path.append( ".")
import Database
import Staff_interface
import Staff_registration
from tkinter import *
from tkinter import messagebox

class Staff_login:
    def __init__(self, root) -> None:
                
        #gui interface window
        self.root = root
        self.root.title('Taxi Booking System - Staff_login')
        window_width = 300
        window_height = 300
        # getting the window width and height information
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # placing the window based on window resolution
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        

        #Staff_login heading   TITLE
        heading = Label(self.root, text = 'Staff_login' , fg= 'green', font=' Times 24')
        heading.pack()

        # stores label and entry fields
        frame = Frame(self.root)
        frame.pack(padx= 10, pady= 10)
        # store buttons
        buttonFrame = Frame(self.root)
        buttonFrame.place( x = 100, y = 180)

        # variables declaration
        self.email = StringVar()
        self.password = StringVar()
        
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

        btn_Staff_login = Button(buttonFrame, text = 'Staff_login',  height = 1, bg = 'green', fg= 'white', command= self.log)
        btn_Staff_login.grid(row= 0, column= 0)

        btn_register = Button(buttonFrame, text= ' Register', width= -1, height= 1, bg = 'lightblue', fg= 'black', command= self.registrationForm).grid(row= 0, column= 1, padx= 10)
    
    # login system checked
    def log(self):
        try:
            Database.cursor.execute("select * from driver where D_email = %s and D_password = %s",(self.email.get(), self.password.get()))
            row = Database.cursor.fetchone()
            print(row)
            self.driverID = row[0]
            self.d_name = row[1]
            self.status = row[8]
            print('Driver ID = ',self.driverID,'driver name :', self.d_name, 'driver status :', self.status)
            try:
                if row != None: 
                    self.root.destroy()
                    root = Tk()  # Creating instance of Tk class
                    obj = Staff_interface.Staff_interface(root,self.driverID, self.d_name, self.status)
                    root.mainloop()
                    
                elif row == None:
                    messagebox.showerror("Error", "User Not found !!!", parent = self.root)
            except tkinter.TclError:
                pass
        except:
            messagebox.showerror('Error', 'Unable to login',parent=self.root)
 
    # calling new window form another class
    def registrationForm(self):
        self.root.destroy()
        root = Tk()  # Creating instance of Tk class
        obj = Staff_registration.Staff_registration(root)
        root.mainloop()
       

# main method
if __name__ == '__main__':
    root = Tk()
    Staff_login(root)
    root.mainloop()

