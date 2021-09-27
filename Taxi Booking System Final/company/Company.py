import Administrator
import viewDrivers
import viewCustomer
from tkinter import *
import AssignDriver_Page
from datetime import *

class CompanyClass:
    def __init__(self, root):
        self.root = root
        root.state('zoomed')
        self.root.title("Taxi Booking System - Company Staff Interface")
        self.root.resizable(True, False)  # This code helps to disable windows from resizing

        # adjusting window dimension based on the screen size
        screen_width = self.root.winfo_screenwidth() # 1536  in this case
        screen_height = self.root.winfo_screenheight() # 864 in this case
        print(screen_width, screen_height)
        self.root.geometry('%dx%d'%(screen_width, screen_height))

        # banner of the company on the top
        self.bannerFile = PhotoImage(file= "Pictures\\banner.png")
        Label(self.root, image= self.bannerFile).pack(side=TOP)


        # frame to store all the button of homepage
        self.mainFrame = Frame(self.root, bg= 'red',width= 800, height= 400)
        self.mainFrame.place(x= 120 , y = 400, width= 1300, height= 370)

        # button image
        self.btn_logOut = PhotoImage(file='Pictures\\btn_logOut.png')
        self.btn_assignDriver = PhotoImage(file='Pictures\\btn_assigndriver.png')
        self.btn_viewCustomer = PhotoImage(file='Pictures\\btn_viewcustomer.png')
        self.btn_viewDrivers = PhotoImage(file='Pictures\\btn_viewdrivers.png')

        # button icon on main frame
        Button(self.mainFrame, image= self.btn_assignDriver, command= self.assignDrivers).pack(side = 'left', padx=120, pady= 80)
        Button(self.mainFrame, image= self.btn_viewCustomer, command= self.viewCustomer ).place(x = 500, y = 80)
        Button(self.mainFrame, image= self.btn_viewDrivers, command = self.viewDrivers).pack(side='right', padx=120, pady= 80)

        # button on self.root - logOut button
        Button(self.root, image= self.btn_logOut, command= self.logout).place(x = 1350, y = 50)

        # displaying the current date on the top
        currentDate = Label(root, text="Current date: " + datetime.now().strftime('%Y/%m/%d'), font= 25, bg='yellow')
        currentDate.place(x  = 10, y = 30)

    # close the current interface and open the assignDrivier interface.
    def assignDrivers(self):
        print('running assign driver interface')
        self.root.destroy()
        root = Tk()  # Creating instance of Tk class
        obj = AssignDriver_Page.AssignDriver(root)
        root.mainloop()

    # close the current interface and open the viewCustomer interface.
    def viewCustomer(self):
        print('running view customer interface')
        self.root.destroy()
        root = Tk()  # Creating instance of Tk class
        obj = viewCustomer.ViewCustomer(root)
        root.mainloop()

    # close the current interface and open the viewDriver interface.
    def viewDrivers(self):
        print('running view customer interface')
        self.root.destroy()
        root = Tk()  # Creating instance of Tk class
        obj = viewDrivers.ViewDrivers(root)
        root.mainloop()

    # to logout of the system
    def logout(self):
        self.root.destroy()
        root = Tk()  # Creating instance of Tk class
        obj = Administrator.Login(root)
