import Company
from tkinter import *
from tkinter import messagebox
import sys
sys.path.append( ".")
import Database

# default username or email = admin
# default password          = admin


class Login:
    def __init__(self, root):
                
        #gui interface window
        self.root = root
        self.root.title('Administrator')
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
        self.username = StringVar()
        self.password = StringVar()
        self.customerID = StringVar()

        # stores label and entry fields
        frame = Frame(self.root)
        frame.pack(padx= 10, pady= 10)
        # store buttons
       

        # username address 
        lbl_username = Label(frame, text = 'username ID' )
        lbl_username.grid(row = 0, column = 0,  padx = 20, pady = 20)
        txt_username = Entry(frame, textvariable= self.username)
        txt_username.grid(row = 0, column = 1)

        #password
        lbl_password = Label(frame, text = 'Password')
        lbl_password.grid(row=1, column=0)

        password = Entry(frame,  show = '*' , textvariable= self.password)
        password.grid(row=1, column=1)

        btn_login = Button(self.root, text = 'Login',  height = 1, bg = 'green', fg= 'white', command= self.log)
        btn_login.place(x= 140, y = 200 )
     

    # calling new window form another class
    def log(self):

        Database.cursor.execute("select * from Administrator where username = %s and Password = %s ",(self.username.get(), self.password.get()))
        row = Database.cursor.fetchone()
        print(row)      

        if row != None:
            
            self.root.destroy()
            homePage = Tk()
            obj = Company.CompanyClass(homePage)
            homePage.mainloop()
            # self.new_window = Toplevel(root)
            # self.new_obj = Company.CompanyClass(self.new_window)
            
        else:
            messagebox.showerror('Error', 'User Not Found',parent=self.root)

    
# main method
if __name__ == '__main__':
    root = Tk()
    Login(root)
    root.mainloop()

