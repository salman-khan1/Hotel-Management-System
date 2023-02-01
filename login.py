from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from hotel import HotelManagmentSystem


def main():
 win=Tk()
 app=login_Window(win)
 win.mainloop() 


class login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"E:\hotelManagnment\images\taj.jpg")

        self.lbl_bg = Label(self.root, image=self.bg)
        self.lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)


        frame=Frame(self.root,bg="black")
        frame.place(x=530,y=170,width=330,height=440)

        img1=Image.open("images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=640,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

    ######labels########
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

    ############Icon Images###########
        img2=Image.open("E:\hotelManagnment\images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg2.place(x=570,y=323,width=25,height=25)    


        img3=Image.open("E:\hotelManagnment\images\lock-512.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg3.place(x=570,y=395,width=25,height=25)    

    ############Login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

    ############Registration Button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activebackground="black",activeforeground="white")
        registerbtn.place(x=16,y=350,width=160)


    #############Forgot Password
        forgotbtn=Button(frame,text="Forgot Password",command=self.forgot_pass_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activebackground="black",activeforeground="white")
        forgotbtn.place(x=10,y=370,width=160)
    ######### New REgister window on new user regiratration button
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
     if self.txtuser.get()=="" or self.txtpass.get()=="":
        messagebox.showerror("error","All field are required")

    #  elif self.txtuser.get()=="salman" and self.txtpass.get()=="pakhtoon":
    #     messagebox.showinfo("Success","Well Come to Hotel Mangment System")
     else:
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from register where email=%s and password=%s",(
                                                                                self.txtuser.get(),
                                                                                self.txtpass.get()
        ))
        row=my_cursor.fetchone()
        if row ==None:
            messagebox.showerror("Error","Invalid username or password")
        else:
            open_main=messagebox.askyesno("YesNo","Access Only Admin")
            # messagebox.showinfo(open_main)
            if open_main>0:
            # if open_main<1:
                self.new_window=Toplevel(self.new_window)
                self.app=HotelManagmentSystem(self.new_window)
            else:
                if not open_main:
                    return
        conn.commit()
        conn.close()
############ Reset Password
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please Enter new Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s and SecurityQ=%s and SecurityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your Password has been reset, Please login with new password",parent=self.root2)
                self.root2.destroy()
######### Forgot Password Window
    def forgot_pass_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the email address to reset the password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                #Security Combo boxes and label
                Security_Q=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white")
                Security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your nick name","Your favourite place")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                ## Security Answer
                Security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                Security_A.place(x=50,y=150)
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)
                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="White",bg="Green")
                btn.place(x=130,y=290)




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        ################Variables################
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
                ########Background Image
        self.bg=ImageTk.PhotoImage(file=r"E:\hotelManagnment\images\taj.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
                ########Left Image
        self.bg1=ImageTk.PhotoImage(file=r"E:\hotelManagnment\images\computer-keyboard-headphone-with-text-listen-your-customers_698447-1205.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)
        #######main Frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",25,"bold"),fg="dark green",bg="white" )
        # register_lbl.place(x=20,y=20)

      ##########  Label and Entries
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        ######Row1
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        #####Last name
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)
        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=370,y=130,width=250)

       
                                          ######Row2
         #####contact 
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
                        ######Email
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        #Security Combo boxes and label
        Security_Q=Label(frame,text="Security Question",font=("times new roman",15,"bold"),bg="white")
        Security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,text="Select Security Question",font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your nick name","Your favourite place")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        ## Security Answer
        Security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        Security_A.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        ## Password
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
        ## Confirm Password
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #########Check out button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        ###########Buttons
        img=Image.open(r"E:\hotelManagnment\images\register-now-button1.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)


        imgL=Image.open(r"E:\hotelManagnment\images\loginpng.png")
        imgL=imgL.resize((200,50),Image.ANTIALIAS)
        self.photoimageL=ImageTk.PhotoImage(imgL)
        b2=Button(frame,image=self.photoimageL,command=self.return_login,borderwidth=0,cursor="hand2")
        b2.place(x=330,y=420,width=200)


        ########Function Declaration##########
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All Fields are required")
        elif self.var_pass.get()!= self.var_confpass.get():
                messagebox.showerror("Error","Password & Confirm Password must be Same")
        elif self.var_check.get()==0:
                messagebox.showerror("Error","You must Agree to the terms & Condtions")
        else:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                my_cursor=conn.cursor()
                query=("Select * from register where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row !=None:
                        messagebox.showinfo("Error","User already Exist ,Please try another email")
                else:
                        my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                        ))
                
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()



if __name__=="__main__":
    main()