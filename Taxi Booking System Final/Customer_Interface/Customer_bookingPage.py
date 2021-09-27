import Customer_login
import sys
sys.path.append( ".")
import Database
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Style, Treeview
from tkcalendar import *
from datetime import * 




class booking:

    def __init__(self, root , customerID):  # take the customerID from login page 
        print('booking page working ')
        self.root = root
        root.state('zoomed')
        root.title("Taxi Booking System - Customer Interface")
        root.resizable(False, False)  # This code helps to disable windows from resizing

        # adjusting window dimension based on the screen size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(screen_width, screen_height))

        # banner of the company on the top
        self.bannerFile = PhotoImage(file= "Pictures\\banner.png")
        Label(root, image= self.bannerFile).pack(side=TOP)

        # customer logout
        # button image
        self.btn_logOut = PhotoImage(file='Pictures\\btn_logOut.png')
        Button(self.root, image= self.btn_logOut, command= self.logout).place(x = 1350, y = 50)

        #creating all the frame required
        # Creating frame to store elements 
        self.storeFrame = Frame(root, bg= 'cyan')
        self.storeFrame.place(x = 70 , y = 200, width= 410, height= 500)
        # frame to store data label and entry fields
        self.dataFrame = Frame(self.storeFrame, padx= 10) # padding between the internal elements and the frame
        self.dataFrame.pack( padx= 5, pady= (40, 130)) # padding from the outer main frame
        # frame to store all the buttons
        self.buttonFrame = Frame(self.storeFrame, bg= 'cyan')
        self.buttonFrame.place(x= 0, y= 400)
        # search frame 
        self.searchFrame = Frame(root, bg = 'yellow')
        self.searchFrame.place(x = 680, y = 150, width= 380, height= 40)
        # frame to store table
        self.TreeviewFrame = Frame(root, width= 850, height= 500, bg = 'skyblue')
        self.TreeviewFrame.place(x= 550 , y = 200, width=850, height= 500)

        #font and padding (fixed) values
        self.fnt = '20'
        self.paddingx = 10
        self.paddingy = 20

        #variables declaration
        self.sn = StringVar()
        self.paddress = StringVar()
        self.pdate = StringVar()
        self.ptime = StringVar()
        self.daddress = StringVar()
        self.search = StringVar() # variable to store search string
        self.customerID = customerID

        # display the current date on the top
        currentDate = Label(root, text="Current date: " + datetime.now().strftime('%Y/%m/%d'), font= 25, bg='yellow')
        currentDate.place(x  = 10, y = 30)
        

        #search elements    
        # elements of search frame
        self.lbl_search = Label(self.searchFrame, text= 'Booking ID :', font= self.fnt).grid(row= 0, column= 0)
        # creating the entry field
        self.searchFrom = Entry(self.searchFrame, textvariable= self.search ,font= self.fnt, width= 16).grid(row= 0, column= 1)
        # search button 
        self.btn_search = Button(self.searchFrame, text= 'Search', font= self.fnt, command= self.search_show).grid(row= 0 , column= 2)

        #Entry data 
        # labels and data entry fields respectively
        self.serialnum  = Label(self.dataFrame, text= 'Serial Number :', font= self.fnt, padx= self.paddingx, pady= self.paddingy).grid(row= 0, column= 0 )
        self.serialnum = Label(self.dataFrame, textvariable =  self.sn, font= self.fnt ).grid(sticky=W,row=0, column= 1)

        self.lbl_paddress = Label(self.dataFrame, text= 'Pick Up Address :', font= self.fnt, padx= self.paddingx, pady= self.paddingy).grid(row= 1, column= 0 )
        self.txt_paddress = Entry(self.dataFrame, textvariable = self.paddress, font= self.fnt ).grid(row=1, column= 1)

        self.lbl_pdate = Label(self.dataFrame, text= 'Pick Up Date :', font= self.fnt, padx= self.paddingx, pady= self.paddingy).grid(row=2, column= 0)
        self.txt_pdate = DateEntry(self.dataFrame,state = "readonly", textvariable= self.pdate, font= self.fnt)
        self.txt_pdate.grid(row=2, column= 1)

        self.lbl_ptime = Label(self.dataFrame, text= 'Pick Up Time :', font= self.fnt, padx= self.paddingx, pady= self.paddingy).grid(row=3, column= 0)
        self.txt_ptime = Entry(self.dataFrame, textvariable= self.ptime, font= self.fnt).grid(row=3, column= 1)

        self.lbl_daddress = Label(self.dataFrame, text= 'Drop Off Address :', font= self.fnt, padx= self.paddingx, pady= self.paddingy).grid(row=4, column= 0)
        self.txt_daddress = Entry(self.dataFrame, textvariable = self.daddress, font= self.fnt).grid(row=4, column= 1)

        #All the buttons frame
        # button padding space
        self.buttonPadding = 15
        # creating the basic buttons for the booking operations
        self.btn_book = Button(self.buttonFrame, text= 'Book', font= self.fnt, command= self.book).grid(row= 0, column= 0, padx= self.buttonPadding)
        self.btn_update = Button(self.buttonFrame, text= 'Update', font= self.fnt, command= self.update).grid(row= 0, column= 1, padx= self.buttonPadding)
        self.btn_cancel = Button(self.buttonFrame, text= 'Cancel', font= self.fnt, command= self.cancel).grid(row= 0, column= 2, padx= self.buttonPadding)
        self.btn_reset = Button(self.buttonFrame, text= 'Clear', font = self.fnt, command= self.clear).grid(row= 0 , column= 3, padx= self.buttonPadding)


        #table and its elements
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
        self.tree = Treeview(self.TreeviewFrame, height= 20,columns=('num', 'pdate', 'ptime', 'paddress', 'daddress', 'Dname', 'Dphone', 'Bstatus'), xscrollcommand= scroll_x.set, yscrollcommand= scroll_y.set, selectmode= 'extended')
        self.tree.column('#0', width = 0, stretch= NO)
        self.tree.column('num', anchor= CENTER, width= 100, minwidth= 30)
        self.tree.column('pdate', anchor= E, width= 100)
        self.tree.column('ptime', anchor= CENTER, width= 100)
        self.tree.column('paddress', anchor= E, width= 120)
        self.tree.column('daddress', anchor= E, width= 120)
        self.tree.column('Dname', anchor= E, width= 100)
        self.tree.column('Dphone', anchor= E, width= 100)
        self.tree.column('Bstatus', anchor= CENTER, width= 100)
        
        # config scroll bar to scroll content
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview) 

        # heading of the columns
        self.tree.heading('#0', text= '')
        self.tree.heading('num', text= 'Booking ID', anchor= CENTER)
        self.tree.heading('pdate', text= 'Pick Up Date', anchor= CENTER)
        self.tree.heading('ptime', text= 'Pick Up Time', anchor= CENTER)
        self.tree.heading('paddress', text= 'Pick Up Address', anchor= CENTER)
        self.tree.heading('daddress', text= 'Drop Off Address', anchor= CENTER)
        self.tree.heading('Dname', text = 'Driver Name', anchor= CENTER)
        self.tree.heading('Dphone', text = 'Driver Phone',  anchor= CENTER)
        self.tree.heading('Bstatus', text = 'Status', anchor= CENTER)

        self.tree.pack()
        # fetching the data from focused row in the table
        self.tree.bind("<ButtonRelease-1>",self.get_data)
        # inserting the content into the table
        self.show()


    # to logout of the system
    def logout(self):
        self.root.destroy()
        root = Tk()  # Creating instance of Tk class
        obj = Customer_login.Login(root)
        root.mainloop()
    
    # find the number of gap day against the selected date
    def gap(self):
        Start=date.today()
        End=self.txt_pdate.get_date()
        Gap=(End-Start).days
        print("Days gap:",Gap)
        return Gap

    # display the records from database to table 
    def show(self): #customerID
    
        # try:
            Database.cursor.execute("select * from trip_booking where not Booking_status = 'Cancelled' and CustomerID = %s ORDER BY `trip_booking`.`BookingID` DESC"%(self.customerID))
            rows=Database.cursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert('',END,values=(row[0],row[1], row[2], row[3], row[4],'','',row[6]))


    # search the bookings with booking ID
    def search_show(self):
    
        # try:
            if self.search.get() == '':
                self.show()
            else:
                Database.cursor.execute("select * from trip_booking where BookingID = %s"%(self.search.get()))
                rows=Database.cursor.fetchall()
                self.tree.delete(*self.tree.get_children())
                for row in rows:
                    self.tree.insert('',END,values=(row[0],row[1], row[2], row[3], row[4],'','',row[6]))


    # load the data to Entry fields on click action (((indexerror with sn)))
    def get_data(self,ev):
        # try:

            rowdata=self.tree.focus()
            content=(self.tree.item(rowdata))
            row=content['values']
            print(row)
           
            self.sn.set(row[0]),
            self.pdate.set(row[1]),
            self.ptime.set(row[2]),
            self.paddress.set(row[3]),
            self.daddress.set(row[4])
        
      
    # update the previous booking made by the customer (((checked))) -- Not dynamic
    def update(self):
        
        # try:
            if self.sn.get()== "" :
                messagebox.showerror("Error"," Select a record to Update",parent=self.root)
            else: 
                Database.cursor.execute("DELETE FROM `trip_booking` WHERE BookingID = %s"%(self.sn.get()))
                Database.con.commit()
                

                Database.cursor.execute("INSERT INTO `trip_booking`(PickUp_address, PickUp_date, PickUp_time, DropOff_address, CustomerID) VALUES (%s,%s,%s,%s,%s)",(
                            self.paddress.get(),
                            self.txt_pdate.get_date(),
                            self.ptime.get(),
                            self.daddress.get(),
                            self.customerID
                            ))
                            
                Database.con.commit()
                

                messagebox.showinfo("Sucess","Booking Updated Sucessfully",parent=self.root)
                self.clear()
                self.show()

    
    # cancel the booking made by the customer
    def cancel(self):
        # try:
            if self.sn.get()== "":
                messagebox.showerror("Error","Select a record to Cancel",parent=self.root)
            else:
                op=messagebox.askyesno("Confirm", "Do you want to delete?",parent=self.root)
                if op==True:
                    print(self.customerID)
                    Database.cursor.execute("UPDATE `trip_booking` SET Booking_status = 'Cancelled' WHERE BookingID = %s"%(self.sn.get())) 
                    Database.con.commit()
                    messagebox.showinfo("Cancelled","Booking cancelled Successfully",parent=self.root)
                    self.clear()
                    self.show()
        

    def book(self):
        if self.gap() >= 0:
            try:
                if (self.paddress.get()=="") or (self.ptime.get()=="") or (self.daddress.get()==""):
                    messagebox.showerror("Error","All the Fields are Mandatory",parent=self.root)
                else:
                    
                    Database.cursor.execute("INSERT INTO `trip_booking`(PickUp_address, PickUp_date, PickUp_time, DropOff_address, CustomerID) VALUES (%s,%s,%s,%s,%s)",(
                        self.paddress.get(),
                        self.txt_pdate.get_date(),
                        self.ptime.get(),
                        self.daddress.get(),
                        self.customerID
                        ))
                    Database.con.commit()
                    messagebox.showinfo("Sucess","Booking Added Sucessfully ",parent=self.root)
                    self.clear()
                    self.show()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        else:
            messagebox.showwarning('Invalid', 'Only upcoming Dates are acceptable')



    # clear out all the fields 
    def clear(self):
        self.paddress.set("")
        self.pdate.set("")
        self.ptime.set("")
        self.daddress.set("")
        self.sn.set('')
