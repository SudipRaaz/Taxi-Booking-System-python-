import Customer_login
import sys
sys.path.append( ".")
import Database
from tkinter import *
from tkinter import messagebox
import re


class Customer_register:
    def __init__(self, root):
        self.root = root # creating the instance of Tk()   
        frame_width = 1000
        frame_height = 700

        # getting the formation about the window width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # finding the cordinate to place the window
        x_cordinate = int((screen_width/2) - (frame_width/2))
        y_cordinate = int((screen_height/2) - (frame_height/2))
        
        #  placing the window in the screen
        self.root.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate, y_cordinate))
        self.root.title('Customer - Registration')

        #adding a picture at the background
        self.backpic = PhotoImage(file="Pictures\\registration.png")
        self.backgroundImage = Label(self.root, image= self.backpic).place(x=0,y=0)

        # image back button
        self.backIcon = PhotoImage(file= "Pictures\\back.png")

        #font
        fnt = '20'
        paddingx = 10
        paddingy = 20

        # variables declaration
        self.name = StringVar()
        self.address = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.credit = StringVar()
        self.gender = StringVar()
        self.var = IntVar()          # stores gender integer

        # creating main frame to store sub-frames
        mainFrame = Frame(self.root,  bg= '#5adad9',width= 450, height= 800)
        mainFrame.pack(anchor= 'e')
        
        # title of the frame - Registration
        line = '_'*15
        Label(mainFrame, text= line, font= 'Trebuchet 20', bg= '#5adad9', borderwidth= 1).place(x = 70, y = 20)
        Label(mainFrame, text= 'Registration', font= 'Trebuchet 20', bg='#5adad9').place(x = 110, y = 14)

        # registration data entry frame - subframe of mainframe
        frameDetails = Frame(mainFrame, bg= '#5adad9',width= 350, height= 700)
        frameDetails.pack(side='right', padx=10 , pady=80)

        # grid layout - label and entry fields in the sequence
        lbl_name = Label(frameDetails, text= 'Name :' , font= fnt).grid(row=0, column=0, padx= paddingx , pady= paddingy)
        txt_name = Entry(frameDetails, font= fnt, textvariable= self.name).grid(row=0, column= 1)

        lbl_address = Label(frameDetails, text= 'Address :', font= fnt).grid(row=1, column=0, padx= paddingx , pady= paddingy)
        txt_address = Entry(frameDetails, font= fnt, textvariable= self.address).grid(row=1, column= 1)

        lbl_phone = Label(frameDetails, text= 'Phone :', font= fnt).grid(row=2, column= 0, padx= paddingx , pady= paddingy)
        txt_phone = Entry(frameDetails, font= fnt, textvariable= self.phone).grid(row=2, column=1)

        lbl_email = Label(frameDetails, text= 'Email :', font= fnt).grid(row=3, column=0, padx= paddingx , pady= paddingy)
        txt_email = Entry(frameDetails, font= fnt, textvariable= self.email).grid(row=3, column=1)

        lbl_password = Label(frameDetails, text= 'Password :', font= fnt).grid(row=4, column=0, padx= paddingx , pady= paddingy)
        txt_password = Entry(frameDetails, show = '*', font= fnt, textvariable= self.password).grid(row=4, column=1)
        
        lbl_credit = Label(frameDetails, text= 'Credit Card :', font= fnt).grid(row=5, column=0, padx= paddingx , pady= paddingy)
        txt_credit = Entry(frameDetails, font= fnt, textvariable= self.credit).grid(row=5, column= 1, columnspan=2)

        lbl_gender = Label(frameDetails, text='Gender', font=fnt).grid(row=6, column= 0, padx= paddingx , pady= paddingy)
        radio = Radiobutton(mainFrame, text = 'Male', value = 0, variable = self.var, font= fnt).place(x = 160, y =512)
        radio = Radiobutton(mainFrame, text = 'Female', value = 1, variable = self.var, font= fnt).place(x = 230, y = 512)

        # Buttons used in the window
        btn_submit = Button(mainFrame, text = 'submit', command = self.registering, font=fnt).place(x =  160, y =590)
        self.btn_back = Button(self.root, text = 'Back', image = self.backIcon , command = self.back).place(x = 20 , y = 20)

        # setting the variable based on the customer choice 
        if self.var.get() == 0:
            self.gender.set("Male") # setting male for 0
        else:
            self.gender.set("Female") # setting female for 1

    # bring back the main page of administrator
    def back(self):
        self.root.destroy()
        root = Tk()  # Creating instance of Tk class
        obj = Customer_login.Login(root)
        root.mainloop()

    # check for valid email address
    def check(self):
        # pass the regular expression
        # and the string into the fullmatch() method
        # regex pattern to validate email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, self.email.get())):
            print("Valid Email")
            return True
 
        else:
            print("Invalid Email")
            return False


    # register customer to database
    def registering(self):
        if self.check():
        # try:
            if (self.name.get() == "") or (self.address.get() == "") or (self.phone.get() == "") or (self.email.get() == "") or (self.password.get() == "") or (self.credit.get() == ""):
                messagebox.showerror("Error","Fields Can Not Be EMPTY",parent=self.root)              
            else:
                Database.cursor.execute("Select * from customer where Phone=%s or CreditInfo=%s or Email = '%s'"%(self.phone.get(), self.credit.get(), self.email.get()))
                row=Database.cursor.fetchone()
                print(Database.cursor, row)
                if row == None:
                    Database.cursor.execute("INSERT INTO customer (Name, Address, Phone, Email, Password,CreditInfo, Gender) VALUES (%s,%s,%s,%s,%s,%s,%s)",(
                                  
                                    self.name.get(),
                                    self.address.get(),
                                    self.phone.get(),
                                    self.email.get(),
                                    self.password.get(),
                                    self.credit.get(),
                                    self.gender.get()
                                
                    ))
                    Database.con.commit()
                    messagebox.showinfo("Sucess"," Registered Sucessfully",parent=self.root)
                    
                else:
                    messagebox.showerror("Error","Phone Number OR Credit Card OR Email \nIs Already Registered",parent=self.root)
        else:
            messagebox.showerror("Invalid","Please Enter a valid Email address",parent=self.root)
