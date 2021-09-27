from logging import root
import Company
import sys
sys.path.append( ".")
import Database
from tkinter import *  
from tkinter import messagebox
from tkinter.ttk import Combobox, Style, Treeview


class AssignDriver:

    def __init__(self, root):
        root.state('zoomed')
        self.root = root
        self.con = Database
        print('working assign driver')
        self.root.title("Taxi Booking System - Assign Driver")
        self.root.resizable(False, False)  # This code helps to disable windows from resizing

        # adjusting window dimension based on the screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+0+0'%(screen_width, screen_height))
        
        # banner of the company on the top
        self.bannerFile = PhotoImage(file= "Pictures\\banner.png")
        Label(self.root, image= self.bannerFile).pack(side=TOP) 

        #********************************************    creating all the frame required   ******************************************
        # Creating frame to store elements 
        self.storeFrame = Frame(self.root, bg= 'cyan')
        self.storeFrame.place(x = 50 , y = 200, width= 510, height= 500)
        # frame to store data label and entry fields
        self.dataFrame = Frame(self.storeFrame, padx= 10) # padding between the internal elements and the frame
        self.dataFrame.pack( padx= 5) # padding from the outer main frame
        # frame to store all the buttons
        self.buttonFrame = Frame(self.storeFrame, bg= 'cyan')
        self.buttonFrame.place(x= 110, y= 429)
        # frame to store table
        self.TreeviewFrame = Frame(self.root, width= 850, height= 500, bg = 'skyblue')
        self.TreeviewFrame.place(x= 580 , y = 200, width=900, height= 500)

        #font and padding (fixed) values
        self.fnt = '20'
        self.paddingx = 10
        self.paddingy = 20

        #variables declaration
        self.tripNo = StringVar()
        self.paddress = StringVar()
        self.pdate = StringVar()
        self.ptime = StringVar()
        self.daddress = StringVar()
        self.driver = StringVar()
        self.cmb_driverName = StringVar()
        # variable to store search string 
 
        #********************************************    All the buttons frame   ******************************************
        # button padding space
        self.buttonPadding = 15
        # creating the basic buttons for the booking operations
        self.btn_cancel = Button(self.buttonFrame, text= 'Cancel', command= self.cancel, font= self.fnt).grid(row= 0, column= 0, padx= self.buttonPadding)
        self.btn_reset = Button(self.buttonFrame, text= 'Clear', command= self.clear, font = self.fnt).grid(row= 0 , column= 1, padx= self.buttonPadding)
        self.btn_assign = Button(self.buttonFrame, text= 'Assign', command= self.assign, font = self.fnt).grid(row= 0 , column= 2, padx= self.buttonPadding)


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
        self.tree = Treeview(self.TreeviewFrame, height= 20,columns=('num', 'customer', 'bdate', 'pdate', 'ptime', 'paddress', 'daddress', 'Bstatus', 'Dname', 'Dphone'), xscrollcommand= scroll_x.set, yscrollcommand= scroll_y.set, selectmode= 'extended')
        self.tree.column('#0', width = 0, stretch= NO)
        self.tree.column('num', anchor= CENTER, width= 50, minwidth= 30)
        self.tree.column('customer', anchor= CENTER, width= 100)
        self.tree.column('bdate', anchor= CENTER, width= 100)
        self.tree.column('pdate', anchor= E, width= 100)
        self.tree.column('ptime', anchor= CENTER, width= 100)
        self.tree.column('paddress', anchor= E, width= 120)
        self.tree.column('daddress', anchor= E, width= 120)
        self.tree.column('Bstatus', anchor= E, width= 100)
        self.tree.column('Dname', anchor= CENTER, width= 100)
        self.tree.column('Dphone', anchor= E, width= 100)
        
        # config scroll bar to scroll content
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview) 

        # heading of the columns
        self.tree.heading('#0', text= '')
        self.tree.heading('num', text= 'S.N', anchor= CENTER)
        self.tree.heading('customer', text= 'Booked By', anchor= CENTER)
        self.tree.heading('bdate', text= 'Booked Date', anchor= CENTER)
        self.tree.heading('pdate', text= 'Pick Up Date', anchor= CENTER)
        self.tree.heading('ptime', text= 'Pick Up Time', anchor= CENTER)
        self.tree.heading('paddress', text= 'Pick Up Address', anchor= CENTER)
        self.tree.heading('daddress', text= 'Drop Off Address', anchor= CENTER)
        self.tree.heading('Bstatus', text = 'Status', anchor= CENTER)
        self.tree.heading('Dname', text = 'Driver Name', anchor= CENTER)
        self.tree.heading('Dphone', text = 'Driver Phone',  anchor= CENTER)

        self.tree.pack()
        self.tree.bind("<ButtonRelease-1>",self.get_data) # added the button action to table ( call the button function to load data from table to entry fields))
        self.show()
        self.dataEntryFields()

        # adding back button to the frame
        self.backIcon = PhotoImage(file= "Pictures\\back2.png")
        self.btn_back = Button(root, image = self.backIcon , command = self.back).place(x = 20 , y = 20)

    # bring back the main page of administrator
    def back(self):
        self.root.destroy()
        root = Tk()  # Creating instance of Tk class
        obj = Company.CompanyClass(root)
        root.mainloop()
        
    
        #********************************************    Entry data    ******************************************
    def dataEntryFields(self):
        # labels and data entry fields respectively
        self.lbl_trip = Label(self.dataFrame, text= 'Trip No. :', font= self.fnt, padx= self.paddingx, pady= self.paddingy).grid(row= 0 , column= 0)
        self.txt_trip = Label(self.dataFrame , textvariable= self.tripNo, font= self.fnt).grid(sticky= W,row=0, column= 1)

        self.lbl_paddress = Label(self.dataFrame, text= 'Pick Up Address :', font= self.fnt, padx= self.paddingx, pady= self.paddingy).grid(row= 1, column= 0 )
        self.txt_paddress = Entry(self.dataFrame, textvariable= self.paddress, font= self.fnt ).grid(row=1, column= 1)

        self.lbl_pdate = Label(self.dataFrame, text= 'Pick Up Date :', font= self.fnt, padx= self.paddingx, pady= self.paddingy).grid(row=2, column= 0)
        self.txt_pdate = Entry(self.dataFrame, textvariable= self.pdate, font= self.fnt).grid(row=2, column= 1)

        self.lbl_ptime = Label(self.dataFrame, text= 'Pick Up Time :', font= self.fnt, padx= self.paddingx, pady= self.paddingy).grid(row=3, column= 0)
        self.txt_ptime = Entry(self.dataFrame, textvariable= self.ptime, font= self.fnt).grid(row=3, column= 1)

        self.lbl_daddress = Label(self.dataFrame, text= 'Drop Off Address :', font= self.fnt, padx= self.paddingx, pady= self.paddingy).grid(row=4, column= 0)
        self.txt_daddress = Entry(self.dataFrame, textvariable = self.daddress, font= self.fnt).grid(row=4, column= 1)

        self.listDriver = []
        self.availableDrivers()
        self.lbl_driver = Label(self.dataFrame, text = 'Driver :', font = self.fnt , padx= self.paddingx, pady= self.paddingy ).grid(row= 5, column= 0)
        self.cmb_driver = Combobox(self.dataFrame, state="readonly", font= self.fnt, values= self.listDriver, textvariable= self.cmb_driverName).grid(row=5, column= 1) #, values= self.listDriver
       

    # display the records from database to table 
    def show(self): #customerID
            Database.cursor.execute("SELECT trip_booking.BookingID, customer.Name, trip_booking.Booking_date, trip_booking.PickUp_date, trip_booking.PickUp_time, trip_booking.PickUp_address, trip_booking.DropOff_address, trip_booking.Booking_status, driver.D_name, driver.D_phone FROM trip_booking LEFT JOIN customer ON trip_booking.CustomerID = customer.CustomerID LEFT JOIN driver ON driver.DriverID = trip_booking.DriverID ORDER BY `trip_booking`.`BookingID` DESC") 
            rows=Database.cursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert('',END,values =(row[0],row[1], row[2], row[3], row[4],row[5],row[6],row[7],row[8], row[9]))
        

    # load the data to Entry fields on click action (((indexerror with sn)))
    def get_data(self,ev):
        rowdata=self.tree.focus()
        content=(self.tree.item(rowdata))
        row=content['values']
        # print(row)
        
        self.tripNo.set(row[0]),
        self.pdate.set(row[3]),
        self.ptime.set(row[4]),
        self.paddress.set(row[5]),
        self.daddress.set(row[6])
        

    def availableDrivers(self):
        Database.cursor.execute('Select * from driver where status = 1')
        rows = Database.cursor.fetchall()
        for row in rows:
            print(row)  
            self.listDriver.append(row[1])
    
    # cancel the booking made by the customer
    def cancel(self):
        # try:
            if self.tripNo.get()== "":
                messagebox.showerror("Error","Select a record to Cancel",parent=self.root)
            else:
                op=messagebox.askyesno("Confirm", "Do you want to Cancel?",parent=self.root)
                if op==True:
                    Database.cursor.execute("UPDATE `trip_booking` SET Booking_status = 'Cancelled' WHERE BookingID = %s"%(self.tripNo.get())) 
                    Database.con.commit()
                    messagebox.showinfo("Cancelled","Booking cancelled Successfully",parent=self.root)
                    self.clear()
                    self.show()
        
        
    def assign(self):
        # try:
            print(self.cmb_driverName.get(), 'line : 200')
            # fetching the driver ID whose name is in the combobox
            Database.cursor.execute("SELECT DriverID FROM `driver` WHERE D_name = '%s'"%(self.cmb_driverName.get()))
            DriverID = sum(Database.cursor.fetchone())  
            print('Driver iD assigned is ',DriverID) 
            
            # assign driver to the booking 
            Database.cursor.execute("UPDATE `trip_booking` SET Booking_status = 'Booked', DriverID = %s WHERE BookingID = %s",(DriverID, self.tripNo.get()))
            Database.con.commit()

            # update the choosen driver status to unavailable
            Database.cursor.execute("UPDATE driver SET status = 0 WHERE DriverID = %s"%(DriverID))
            Database.con.commit()
            
            
            self.show()
            self.dataEntryFields()
            self.clear()
            messagebox.showinfo('Success', 'Driver assigned', parent = self.root)
        
        
        

    def clear(self):
        self.paddress.set("")
        self.pdate.set("")
        self.ptime.set("")
        self.daddress.set("")
        self.tripNo.set('')

# root = Tk()
# obj = AssignDriver(root)
# root.mainloop()