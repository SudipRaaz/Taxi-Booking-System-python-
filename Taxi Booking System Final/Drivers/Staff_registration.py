import sys
sys.path.append( ".")
import Database
from tkinter import *
from tkinter import messagebox
import re
from tkcalendar import *



#gui interface frameDetails
class Staff_registration:
    def __init__(self, root) -> None:
        self.root = root
        frame_width = 1000
        frame_height = 700
        # getting the window width and height information
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # placing the window based on window resolution
        x_cordinate = int((screen_width/2) - (frame_width/2))
        y_cordinate = int((screen_height/2) - (frame_height/2))

        root.geometry("{}x{}+{}+{}".format(frame_width, frame_height, x_cordinate, y_cordinate))
        root.title('Taxi Company Staff - Staff Registration')

    #adding a picture at the background
        self.backpic = PhotoImage(file="Pictures\\registration.png")
        self.backgroundImage = Label(root, image= self.backpic).place(x=0,y=0)

    # image back button
        self.backIcon = PhotoImage(file= "Pictures\\back.png")
        self.btn_back = Button(root, text = 'Back', image = self.backIcon, command= self.back ).place(x = 20 , y = 20)

    #font
        fnt = '20'
        paddingx = 10
        paddingy = 20

    # variables 
        self.name = StringVar()
        self.phone = StringVar()
        self.dateOfBrith = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.license = StringVar()
        self.var = IntVar()
        self.gender = StringVar()

    # main frame to hold the label and data entry fields
        mainFrame = Frame(root,  bg= '#5adad9',width= 450, height= 800)
        mainFrame.pack(anchor= 'ne', padx= 20 , pady= 20)

    # heading of the frame
        line = '_'*15
        Label(mainFrame, text= line, font= 'Trebuchet 20', bg= '#5adad9', borderwidth= 1).place(x = 70, y = 20)
        Label(mainFrame, text= 'Registration', font= 'Trebuchet 20', bg='#5adad9').place(x = 110, y = 14)

    # registration data entry frame
        frameDetails = Frame(mainFrame, bg= '#5adad9',width= 350, height= 700)
        frameDetails.pack(side='right', padx=10 , pady=80)

    # components of data entry frame
        lbl_name = Label(frameDetails, text= 'Name :' , font= fnt).grid(row=0, column=0, padx= paddingx , pady= paddingy)
        txt_name = Entry(frameDetails, font= fnt, textvariable = self.name).grid(row=0, column= 1)

        lbl_phone = Label(frameDetails, text= 'Phone :', font= fnt).grid(row=1, column= 0, padx= paddingx , pady= paddingy)
        txt_phone = Entry(frameDetails, font= fnt, textvariable = self.phone).grid(row=1, column=1)

        self.lbl_dateOfBirth = Label(frameDetails, text= 'Date of Birth :', font= fnt).grid(row=2, column=0, padx= paddingx , pady= paddingy)
        self.txt_dateOfBirth = DateEntry(frameDetails,state = "readonly", font= fnt, textvariable = self.dateOfBrith)
        self.txt_dateOfBirth.grid(row=2, column= 1)

        lbl_email = Label(frameDetails, text= 'Email :', font= fnt).grid(row=3, column=0, padx= paddingx , pady= paddingy)
        txt_email = Entry(frameDetails, font= fnt, textvariable = self.email).grid(row=3, column=1)

        lbl_password = Label(frameDetails, text= 'Password :', font= fnt).grid(row=4, column=0, padx= paddingx , pady= paddingy)
        txt_password = Entry(frameDetails, show = '*', font= fnt, textvariable = self.password).grid(row=4, column=1)
        
        lbl_license = Label(frameDetails, text= 'License Plate No :', font= fnt).grid(row=5, column=0, padx= paddingx , pady= paddingy)
        txt_license = Entry(frameDetails, font= fnt, textvariable = self.license).grid(row=5, column= 1)

        

        lbl_gender = Label(frameDetails, text='Gender', font=fnt).grid(row=6, column= 0, padx= paddingx , pady= paddingy)
        radio = Radiobutton(mainFrame, text = 'Male', value = 0, variable = self.var, font= fnt).place(x = 160, y =512)
        radio = Radiobutton(mainFrame, text = 'Female', value = 1, variable = self.var, font= fnt).place(x = 230, y = 512)

    # assigning the string value to the choosen radio button
        if self.var.get() == 0:
            self.gender.set("Male")
        else:
            self.gender.set("Female")


        btn_submit = Button(mainFrame, text = 'submit', command = self.register, font=fnt).place(x =  160, y =590)


    
    def back(self):
        self.root.destroy()

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

# abstracting the data from the GUI interface
    def register(self):
        if self.check():
            if self.check():
                if (self.name.get() == '') or (self.phone.get() == '') or (self.dateOfBrith.get() == '') or (self.email.get() == '') or (self.password.get() == '') or (self.license.get() == ''): 
                    messagebox.showerror("Error","Fields Can Not Be EMPTY",parent=self.root)
                
                else:
                    Database.cursor.execute("Select * from driver where D_phone=%s or D_licensePlate=%s or D_email =%s",(self.phone.get(), self.license.get(), self.email.get()))
                    row=Database.cursor.fetchone()
                    print('user with same phone or license number =',row)
                    if row == None:
                        print(self.txt_dateOfBirth, self.gender)
                        Database.cursor.execute(" Insert into driver (D_name, D_phone, D_birth, D_email, D_password, D_licensePlate, D_gender) values (%s,%s,%s,%s,%s,%s,%s)",(
                            self.name.get(),
                            self.phone.get(),
                            self.txt_dateOfBirth.get_date(),
                            self.email.get(),
                            self.password.get(),
                            self.license.get(),
                            self.gender.get()
                        ))
                        Database.con.commit()
                        messagebox.showinfo("Sucess"," Registered Sucessfully",parent=self.root)
                        
                    else:
                        messagebox.showerror("Unavailable","Phone Number OR License Plate OR Email Is Not Available At The Moment",parent=self.root)
            else:
                messagebox.showerror("Invalid","Please enter a valid Email address",parent=self.root)
        else:
            messagebox.showerror('Invalid','Please enter a valid Email address')

