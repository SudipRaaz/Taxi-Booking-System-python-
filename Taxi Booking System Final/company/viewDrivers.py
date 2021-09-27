import Company
import sys
sys.path.append( ".")
import Database
from tkinter import *  
from tkinter.ttk import Combobox, Style, Treeview


class ViewDrivers:
    def __init__(self, root):
        print('working')
        self.root = root
        # to open the window in the maximized size
        root.state('zoomed')
        root.title("Taxi Booking System - Drivers") # to set the title of the window
        root.resizable(False, False)  # This code helps to disable windows from resizing

        # adjusting window dimension based on the screen size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(screen_width, screen_height))
        
        
        # banner of the company on the top
        self.bannerFile = PhotoImage(file= "Pictures\\banner.png")
        Label(root, image= self.bannerFile).pack(side=TOP) 

        #creating all the frame required
        # search frame 
        self.searchFrame = Frame(root, bg = 'red')
        self.searchFrame.place(x = 480, y = 150, width= 400, height= 40)
        
        # frame to store table
        self.TreeviewFrame = Frame(root, width= 850, height= 500, bg = 'skyblue')
        self.TreeviewFrame.place(x= 270 , y = 220, width=1000, height= 550)

        #font and padding (fixed) values
        self.fnt = '20'
        self.paddingx = 10
        self.paddingy = 20

        # variable to store search string 
        self.search = StringVar()
        

         #********************************************    search elements   ******************************************    
        # elements of search frame
        self.lbl_name = Label(self.searchFrame, text= 'Name :', font= self.fnt, padx= 5).grid(row= 0, column= 0)
        # creating the entry field
        self.searchFrom = Entry(self.searchFrame, textvariable= self.search ,font= self.fnt).grid(row= 0, column= 1, padx= (5, 8))
        # search button 
        self.btn_search = Button(self.searchFrame, text= 'Search', font= self.fnt, command= self.search_shows).grid(row= 0 , column= 2)
        
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
        self.tree = Treeview(self.TreeviewFrame, height= 20,columns=('num', 'name', 'phone', 'dob','license', 'trip'), xscrollcommand= scroll_x.set, yscrollcommand= scroll_y.set, selectmode= 'extended')
        self.tree.column('#0', width = 0, stretch= NO)
        self.tree.column('num', anchor= CENTER, width= 50, minwidth= 30)
        self.tree.column('name', anchor= CENTER, width= 140)
        self.tree.column('phone', anchor= CENTER, width= 140)
        self.tree.column('dob', anchor= CENTER, width= 140)
        self.tree.column('license', anchor= CENTER, width= 140)
        self.tree.column('trip', anchor= CENTER, width= 140)
        
        
        # config scroll bar to scroll content
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview) 

        # heading of the columns
        self.tree.heading('#0', text= '')
        self.tree.heading('num', text= 'S.N', anchor= CENTER)
        self.tree.heading('name', text= 'Name', anchor= CENTER)
        self.tree.heading('phone', text= 'Phone', anchor= CENTER)
        self.tree.heading('dob', text= 'Date of Birth', anchor= CENTER)
        self.tree.heading('license', text= 'License Plate No.', anchor= CENTER)
        self.tree.heading('trip', text= 'Total Trip Assigned', anchor= CENTER)
    
        self.tree.pack()
        self.show()

        # adding back button to the frame
        self.backIcon = PhotoImage(file= "Pictures\\back2.png")
        self.btn_back = Button(root, image = self.backIcon , command = self.back).place(x = 20 , y = 20)

    # bring back the main page of administrator
    def back(self):
        self.root.destroy()
        root = Tk()  # Creating instance of Tk class
        obj = Company.CompanyClass(root)
        root.mainloop()

    # display the records from database to table 
    def show(self): #customerID
    
        # try:
            Database.cursor.execute("select * from driver")
            rows=Database.cursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert('',END,values=(row[0],row[1], row[2], row[3], row[4],row[5],row[6]))

      

        
    # search the bookings with customer name on key 'enter' pressed
    def search_shows(self):
        # try:
            if self.search.get() == '':
                self.show()
            else:
                print('line 160',self.search.get())
                Database.cursor.execute("SELECT * from driver WHERE D_name = '%s'"%(self.search.get()))
                rows=Database.cursor.fetchall()
                self.tree.delete(*self.tree.get_children())
                for row in rows:
                    self.tree.insert('',END,values=(row[0],row[1], row[2], row[3], row[4],row[5],row[6]))

     
