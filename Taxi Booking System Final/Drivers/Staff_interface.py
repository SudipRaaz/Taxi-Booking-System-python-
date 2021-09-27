import Staff_login
from datetime import *
from tkinter import *
from tkinter import messagebox   
from tkinter.ttk import Style, Treeview

from tkcalendar import *
import sys
sys.path.append( ".")
import Database

class Staff_interface:

    def __init__(self, root, driverID , name, status ):
        print('working')
        self.root = root
        # opening the window in maximize 
        self.root.state('zoomed')
        self.root.title("Taxi Booking System - Drivers")
        self.root.resizable(False, False)  # This code helps to disable windows from resizing

        # adjusting window dimension based on the screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+0+0'%(screen_width, screen_height))
        
        
        # banner of the company on the top
        self.bannerFile = PhotoImage(file= "Pictures\\banner.png")
        self.banner =  Label(self.root, image= self.bannerFile)
        self.banner.pack(side=TOP) 

        #********************************************    creating all the frame required   ******************************************
        # search frame 
        self.searchFrame = Frame(self.root, bg = 'yellow')
        self.searchFrame.place(x = 480, y = 150, width= 400, height= 40)
        
        # frame to store table
        self.TreeviewFrame = Frame(self.root, width= 850, height= 500, bg = 'skyblue')
        self.TreeviewFrame.place(x= 200 , y = 220, width=1200, height= 550)

        #font and padding (fixed) values
        self.fnt = '20'
        self.paddingx = 10
        self.paddingy = 20

        # variable to store values
        self.driverID = driverID
        self.driverStatus = status
        self.d_name = name
        self.search = StringVar()
        self.bookingID = StringVar()
        self.pdate = StringVar()
        
        # greeting the user
        Label(self.root, text= ("Wel-Come " + str(self.d_name)), font= self.fnt, bg = 'yellow' ).place(x = 20 , y = 60)

        # customer logout
        # button image
        self.btn_logOut = PhotoImage(file='Pictures\\btn_logOut.png')
        Button(self.root, image= self.btn_logOut, command= self.logout).place(x = 1350, y = 50)

        # display the current date on the top
        currentDate = Label(self.root, text="Current date: " + datetime.now().strftime('%Y/%m/%d'), font= 25, bg='yellow')
        currentDate.place(x  = 10, y = 10)

        #********************************************    search elements   ******************************************    
        # elements of search frame
        self.lbl_name = Label(self.searchFrame, text= 'Name :', font= self.fnt, padx= 5).grid(row= 0, column= 0)
        # creating the entry field
        self.searchbar = Entry(self.searchFrame, textvariable= self.search ,font= self.fnt)
        self.searchbar.grid(row= 0, column= 1, padx= (5, 8))
        self.searchbar.bind('<Return>', self.search_shows)
        # search button 
        self.btn_search = Button(self.searchFrame, text= 'Search', font= self.fnt, command= self.search_show).grid(row= 0 , column= 2)
        
        #********************************************    table and its elements   ******************************************
        # creating scroll bar
        scroll_y = Scrollbar(self.TreeviewFrame, orient= VERTICAL)
        scroll_y.pack(side='right', fill= Y)
        scroll_x = Scrollbar(self.TreeviewFrame, orient= HORIZONTAL)
        scroll_x.pack(side='bottom', fill= X)
        
        # adding some styles to treeview method

        # Add Some Style
        style = Style()
        # Pick A Theme
        style.theme_use('default')
        # Configure the Treeview Colors
        style.configure("Treeview",
        background="#D3D3D3",  
        foreground="black",
        rowheight=30,
        fieldbackground="#D3D3D3")

        # table frame defining columns
        self.tree = Treeview(self.TreeviewFrame, height= 20,columns=('bookingID', 'customerName', 'pdate', 'ptime','paddress', 'daddress', 'bstatus'), xscrollcommand= scroll_x.set, yscrollcommand= scroll_y.set, selectmode= 'extended')
        self.tree.column('#0', width = 0, stretch= NO)
        self.tree.column('bookingID', anchor= CENTER, width= 50, minwidth= 30)
        self.tree.column('customerName', anchor= CENTER, width= 140)
        self.tree.column('pdate', anchor= CENTER, width= 140)
        self.tree.column('ptime', anchor= CENTER, width= 140)
        self.tree.column('paddress', anchor= CENTER, width= 140)
        self.tree.column('daddress', anchor= CENTER, width= 140)
        self.tree.column('bstatus', anchor= CENTER, width= 140)
        
        # config scroll bar to scroll content
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview) 

        # heading of the columns
        self.tree.heading('#0', text= '')
        self.tree.heading('bookingID', text= 'Booking ID', anchor= CENTER)
        self.tree.heading('customerName', text= 'Customer Name', anchor= CENTER)
        self.tree.heading('pdate', text= 'Date of booking', anchor= CENTER)
        self.tree.heading('ptime', text= 'Pick up time', anchor= CENTER)
        self.tree.heading('paddress', text= 'Pick up Address', anchor= CENTER)
        self.tree.heading('daddress', text= 'Drop off Address', anchor= CENTER)
        self.tree.heading('bstatus', text= 'Booking Status', anchor= CENTER)
        
        self.tree.pack()
        # fetching the data from focused row
        self.tree.bind("<ButtonRelease-1>",self.get_data)
        # inseting data into table
        self.show()

        # button to switch the active and unactive driver status
        self.btn_available = Button(self.TreeviewFrame,text='Available', command= self.available, bg= 'lightgreen').place(x = 20 , y = 40)
        self.btn_unavailable = Button(self.TreeviewFrame,text='Unavailable', command= self.unavailable, bg= 'lightblue').place(x = 20 , y = 80)

        # button to mark the trips as completed
        self.btn_complete = Button(self.TreeviewFrame, text= 'Completed',command= self.completeBooking, bg= 'lightgreen').place( x= 1080, y = 40)

        # driver active or inactive indicator in canvas
        Label(self.root, text= 'Driver status', font= self.fnt).place(x = 180, y = 158)
        if self.driverStatus == 1:
            color = 'green'
        else: # setting red color if unactive
            color = 'red'
        can = Canvas(self.root, bg=color, width=40, height= 40)
        can.place(x= 120, y = 150)
        
        # setting the values from database and using the DateEntry format for other purpose
        self.txt_pdate = DateEntry(self.root,state = "readonly", textvariable= self.pdate, font= self.fnt)
        
        
    
    # find the number of gap day against the selected date
    def gap(self):
        Start=date.today()
        End=self.txt_pdate.get_date()
        Gap=(End-Start).days
        print("Days gap:",Gap)
        return Gap

    # load the data to Entry fields on click action (((indexerror with sn)))
    def get_data(self,ev):
            rowdata=self.tree.focus()
            content=(self.tree.item(rowdata))
            row=content['values']
            print(row)

            self.pdate.set(row[2])
            self.bookingID.set(row[0])
            print('booking ID',self.bookingID.get(), 'date :', self.pdate.get())
    
    # mark the bookings completed if they are completed
    def completeBooking(self):
        if self.gap() > 0:
            Database.cursor.execute("UPDATE trip_booking SET Booking_status = 'Completed' WHERE BookingID = %s"%(self.bookingID.get()))
            Database.con.commit()
            messagebox.showinfo('Success', 'Trip marked "Completed"', parent = self.root)
            self.show()
        # else unsuccessful
        else:
            messagebox.showerror('Unsuccessfull', 'Can not mark upcoming trips as "Completed"', parent = self.root)

    # update the status of the driver
    def status(self, color):
        # canvas to show the indication of driver status
        can = Canvas(self.root, bg= color, width=40, height= 40)
        can.place(x= 120, y = 150)

    # change the driver status to available = green
    def available(self):
        # try:
            Database.cursor.execute("UPDATE `driver` SET `status`= 1 WHERE DriverID = %s"%(self.driverID))
            messagebox.showinfo('Status','Driver status updated successfully', parent = self.root )
            active = 'green'
            self.status(active)
     

    # change the driver status to unavailable = red
    def unavailable(self):
            Database.cursor.execute("UPDATE `driver` SET `status`= 0 WHERE DriverID = %s"%(self.driverID))
            messagebox.showinfo('Status','Driver status updated successfully', parent = self.root )
            unactive = 'red'
            self.status(unactive)

    # display the records from database to table 
    def show(self): #customerID
            Database.cursor.execute("SELECT b.BookingID, c.Name, b.PickUp_date, b.PickUp_time, b.PickUp_address, b.DropOff_address, b.Booking_status FROM trip_booking b LEFT JOIN customer c ON c.CustomerID = b.CustomerID WHERE b.DriverID = %s ORDER BY `b`.`BookingID` DESC"%(self.driverID))
            rows=Database.cursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert('',END,values=(row[0],row[1], row[2], row[3], row[4],row[5],row[6]))
                print(row)


    # search the bookings with customer name on key 'enter' pressed
    def search_shows(self,e):
            if self.search.get() == '':
                self.show()
            else:
                print('line 160',self.search.get())
                Database.cursor.execute("SELECT b.BookingID, c.Name, b.PickUp_date, b.PickUp_time, b.PickUp_address, b.DropOff_address, b.Booking_status FROM trip_booking b LEFT JOIN customer c ON c.CustomerID = b.CustomerID WHERE c.Name = '%s'"%(self.search.get()))
                rows=Database.cursor.fetchall()
                self.tree.delete(*self.tree.get_children())
                for row in rows:
                    self.tree.insert('',END,values=(row[0],row[1], row[2], row[3], row[4],row[5],row[6]))


    # search the bookings with customer name in button press
    def search_show(self):
            if self.search.get() == '':
                self.show()
            else:
                print('line 160',self.search.get())
                Database.cursor.execute("SELECT b.BookingID, c.Name, b.PickUp_date, b.PickUp_time, b.PickUp_address, b.DropOff_address, b.Booking_status FROM trip_booking b LEFT JOIN customer c ON c.CustomerID = b.CustomerID WHERE c.Name = '%s'"%(self.search.get()))
                rows=Database.cursor.fetchall()
                self.tree.delete(*self.tree.get_children())
                for row in rows:
                    self.tree.insert('',END,values=(row[0],row[1], row[2], row[3], row[4],row[5],row[6]))


    # to logout of the system
    def logout(self):
        self.root.destroy()
        root = Tk()  # Creating instance of Tk class
        obj = Staff_login.Staff_login(root)
        root.mainloop()

# root = Tk()
# driverID = int
# d_name = str
# status = str
# obj = Staff_interface(root,driverID, d_name, status)
# root.mainloop()
