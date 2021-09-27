import Company
from tkinter import *  
from tkinter.ttk import Style, Treeview
import sys
sys.path.append( ".")
import Database

class ViewCustomer:

    def __init__(self, root):
        print('working')
        self.root = root
        root.state('zoomed')
        root.title("Taxi Booking System - View Customer")
        root.resizable(False, False)  # This code helps to disable windows from resizing

        # adjusting window dimension based on the screen size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(screen_width, screen_height))
        
        
        # banner of the company on the top
        self.bannerFile = PhotoImage(file= "Pictures\\banner.png")
        Label(root, image= self.bannerFile).pack(side=TOP) 

        #********************************************    creating all the frame required   ******************************************
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
        # variable to store search string 

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
        self.tree = Treeview(self.TreeviewFrame, height= 20,columns=('num', 'name', 'address', 'phone', 'email', 'password', 'credit'), xscrollcommand= scroll_x.set, yscrollcommand= scroll_y.set, selectmode= 'extended')
        self.tree.column('#0', width = 0, stretch= NO)
        self.tree.column('num', anchor= CENTER, width= 50, minwidth= 30)
        self.tree.column('name', anchor= CENTER, width= 140)
        self.tree.column('address', anchor= E, width= 100)
        self.tree.column('phone', anchor= CENTER, width= 100)
        self.tree.column('email', anchor= E, width= 130)
        self.tree.column('password', anchor= E, width= 130)
        self.tree.column('credit', anchor= E, width= 130, minwidth= 100)
        
        # config scroll bar to scroll content
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview) 

        # heading of the columns
        self.tree.heading('#0', text= '')
        self.tree.heading('num', text= 'S.N', anchor= CENTER)
        self.tree.heading('name', text= 'Name', anchor= CENTER)
        self.tree.heading('address', text= 'Address', anchor= CENTER)
        self.tree.heading('phone', text= 'Phone Number', anchor= CENTER)
        self.tree.heading('email', text= 'Email Address', anchor= CENTER)
        self.tree.heading('password', text= 'Password', anchor= CENTER)
        self.tree.heading('credit', text= 'Credit Card No', anchor= CENTER)
        
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
            Database.cursor.execute("select * from customer")
            rows=Database.cursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert('',END,values=(row[0],row[1], row[2], row[3], row[4],row[5],row[6]))

        # except Exception as ex:
        #     messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

        
    # search the bookings with customer name on key 'enter' pressed
    def search_shows(self):
        # try:
            if self.search.get() == '':
                self.show()
            else:
                print('line 160',self.search.get())
                Database.cursor.execute("SELECT * from customer WHERE Name = '%s'"%(self.search.get()))
                rows=Database.cursor.fetchall()
                self.tree.delete(*self.tree.get_children())
                for row in rows:
                    self.tree.insert('',END,values=(row[0],row[1], row[2], row[3], row[4],row[5],row[6]))


