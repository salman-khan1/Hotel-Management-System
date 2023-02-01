from multiprocessing import parent_process
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Managment System")
        self.root.geometry("1150x490+220+220")

        ###########VAriables#########
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.roomavalaible=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


################Title################
        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",18,"bold"),background="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

      ###########logo#######  
        img2=Image.open("images\logohotel.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoImg2=ImageTk.PhotoImage(img2) 

        lblimg=Label(self.root,image=self.photoImg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

##############LABEl Frame###########
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman",12,"bold"),padx=1)
        labelframeleft.place(x=5,y=50,width=390,height=420)

##############LABEl and Entries###########

            ###cust Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("arial",11,"bold"),padx=1,pady=4)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=18,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        ######Fetch Data button
        btnFetchData=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data" ,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=310,y=2)

        #Check in Data
        check_in_date=Label(labelframeleft,text="Check_in Date:",font=("arial",12,"bold"),padx=1,pady=4)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=25,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

         ###Check out data
        lbl_Check_out=Label(labelframeleft,text="Check_out Date:",font=("arial",12,"bold"),padx=1,pady=4)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=25,font=("arial",13,"bold"))
        txt_Check_out_date.grid(row=2,column=1)

        ###Room Type
        label_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=1,pady=4)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
        my_cursor=conn.cursor()
        my_cursor.execute("select Roomtype from details")
        rmType=my_cursor.fetchall()   

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=23,state="readonly")
        combo_RoomType["value"]=rmType
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Room Available
        lblRoomAvailable=Label(labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=1,pady=4)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        # txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.roomavalaible,width=25,font=("arial",13,"bold"))
        # txtRoomAvailable.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()    

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.roomavalaible,font=("arial",12,"bold"),width=23,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)


        #Meal
        lblMeal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=1,pady=4)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=25,font=("arial",13,"bold"))
        txtMeal.grid(row=5,column=1)

         #No of Days
        lblNoOfDays=Label(labelframeleft,text="No of Days:",font=("arial",12,"bold"),padx=1,pady=4)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=25,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=6,column=1)
       
         #Paid tax
        lblNoOfDays=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=1,pady=4)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=25,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=7,column=1)

        #Subtotal
        lblSubTotal=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=1,pady=4)
        lblSubTotal.grid(row=8,column=0,sticky=W)
        txtSubTotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=25,font=("arial",13,"bold"))
        txtSubTotal.grid(row=8,column=1)

        #total cost
        lblIdNumber=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=1,pady=4)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,width=25,font=("arial",13,"bold"))
        txtIdNumber.grid(row=9,column=1)

###########BILL Button###########
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnBill.grid(row=10,column=0,padx=2,sticky=W)

                #############BTN################3
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=30,y=350,width=340,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnAdd.grid(row=0,column=0,padx=2)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnUpdate.grid(row=0,column=1,padx=2)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnDelete.grid(row=0,column=2,padx=2)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnReset.grid(row=0,column=3,padx=2)

        #########Right side Image#######
        img3=Image.open(r"images\bed.jpg")
        img3=img3.resize((400,300),Image.ANTIALIAS)
        self.photoImg3=ImageTk.PhotoImage(img3) 

        lblimg3=Label(self.root,image=self.photoImg3,bd=0,relief=RIDGE)
        lblimg3.place(x=750,y=55,width=385,height=200)      

   ###############Table Frame search system#######################
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",12,"bold"),padx=1)
        Table_Frame.place(x=400,y=250,width=735,height=220)
        # Table_Frame.place(x=435,y=50,width=650,height=490)

        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=1)
        # lblSearchBy.grid(row=0,column=0,sticky=W,padx=1)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=15,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=1)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=15,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=1)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowall=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        # btnShowall=Button(Table_Frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnShowall.grid(row=0,column=4,padx=1)

####################Show Data Table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=760,height=250)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomsavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomsavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfDays")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=70)
        self.room_table.column("checkin",width=70)
        self.room_table.column("checkout",width=70)
        self.room_table.column("roomtype",width=70)
        self.room_table.column("roomsavailable",width=70)
        self.room_table.column("meal",width=70)
        self.room_table.column("noOfdays",width=70)
        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
##########ADD DATA
    def add_data(self):

        if self.var_contact.get()=="":

                messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
                try:
                
                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_contact.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.roomavalaible.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_noofdays.get()
                                                                                        
                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","Room Booked Succesfully", parent=self.root)
                except Exception as es:
                        messagebox.showwarning("Warning",f"Some thing went wrong {str(es)}",parent=self.root)

                  ###FETCH DATA#####      
    def fetch_data(self):

        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        row=my_cursor.fetchall()
        if len(row)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in row:
                        self.room_table.insert("",END,values=i)
                conn.commit()
                conn.close()
#########Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]


        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.roomavalaible.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

#####Update data
    def update(self):
        if self.var_contact.get()=="":
                messagebox.showerror("Error","Please Enter Mobile number",parent=self.root)

        else:
                try:
                        
                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                                                                                                                        self.var_checkin.get(),
                                                                                                                                                                        self.var_checkout.get(),
                                                                                                                                                                        self.var_roomtype.get(),
                                                                                                                                                                        self.roomavalaible.get(),
                                                                                                                                                                        self.var_meal.get(),
                                                                                                                                                                        self.var_noofdays.get(),
                                                                                                                                                                        self.var_contact.get()
                                                                                                                                                                                                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Updated","Room details has been updated successfully",parent=self.root)
                except Exception as es:

                        messagebox.showwarning("Warning",f"Some thing went wrong {str(es)}",parent=self.root)
###DELETE
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do You Want to Delete this Room",parent=self.root)
        if mDelete>0:
                try:

                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                        my_cursor=conn.cursor()
                        query="delete from room where Contact=%s"
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                except Exception as es:

                        messagebox.showwarning("Warning",f"Some thing went wrong {str(es)}",parent=self.root)

        else:
                if not mDelete:
                        return
        conn.commit()
        self.fetch_data()
        conn.close()

####RESET
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.roomavalaible.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")   
 
###########FEtch all data#############
    def fetch_contact(self):
        if self.var_contact.get()=="":
                messagebox.showerror("Error","Please Enter Contact number ",parent=self.root)
        else:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                my_cursor=conn.cursor()
                query=("select Name from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                if row==None:
                        messagebox.showerror("Error","This number not found",parent=self.root)
                else:
                        conn.commit()
                        conn.close()

                        showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                        showDataframe.place(x=420,y=55,width=300,height=180)
                        
        #########################NAME################
                        lblname=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                        lblname.place(x=0,y=0)

                        lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lbl.place(x=90,y=0)

        #########################Gender################

                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                        my_cursor=conn.cursor()
                        query=("select Gender from customer where mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()


                        lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                        lblGender.place(x=0,y=30)

                        lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lbl2.place(x=90,y=30)

        #########################Gender################

                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                        my_cursor=conn.cursor()
                        query=("select email from customer where mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()


                        lblGender=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                        lblGender.place(x=0,y=60)

                        lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lbl2.place(x=90,y=60)

        #########################Nationality################

                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                        my_cursor=conn.cursor()
                        query=("select nationality from customer where mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()


                        lblGender=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                        lblGender.place(x=0,y=90)

                        lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lbl2.place(x=90,y=90)

        ######################### id number################

                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                        my_cursor=conn.cursor()
                        query=("select idnumber from customer where mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()


                        lblGender=Label(showDataframe,text="CNIC:",font=("arial",12,"bold"))
                        lblGender.place(x=0,y=120)

                        lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lbl2.place(x=90,y=120)
        #########################Address################

                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                        my_cursor=conn.cursor()
                        query=("select address from customer where mobile=%s")
                        value=(self.var_contact.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()


                        lblGender=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                        lblGender.place(x=0,y=150)

                        lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                        lbl2.place(x=90,y=150)


############SEarch System
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM room WHERE "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                        self.room_table.insert("",END,values=i)
                conn.commit()
        conn.close()




###########BILL BUTTON Function
    def total(self):
        ######DAYS CALCULATION
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate - inDate).days)


        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Single"):
                q1=float(300)
                q2=float(700)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3+q4)
                Tax = "Rs. "+str("%.2f" % ((q5) * 0.09))
                sT= "Rs. "+str("%.2f" % ((q5)))
                TT= "Rs. "+str("%.2f" % (q5+ ((q5) * 0.09)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(sT)
                self.var_total.set(TT)


        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Double"):
                q1=float(500)
                q2=float(1000)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3+q4)
                Tax = "Rs. "+str("%.2f" % ((q5) * 0.09))
                sT= "Rs. "+str("%.2f" % ((q5)))
                TT= "Rs. "+str("%.2f" % (q5+ ((q5) * 0.09)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(sT)
                self.var_total.set(TT)


        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Luxury"):
                q1=float(700)
                q2=float(1500)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3+q4)
                Tax = "Rs. "+str("%.2f" % ((q5) * 0.09))
                sT= "Rs. "+str("%.2f" % ((q5)))
                TT= "Rs. "+str("%.2f" % (q5+ ((q5) * 0.09)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(sT)
                self.var_total.set(TT)


        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
                q1=float(500)
                q2=float(900)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3+q4)
                Tax = "Rs. "+str("%.2f" % ((q5) * 0.09))
                sT= "Rs. "+str("%.2f" % ((q5)))
                TT= "Rs. "+str("%.2f" % (q5+ ((q5) * 0.09)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(sT)
                self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
                q1=float(800)
                q2=float(1200)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3+q4)
                Tax = "Rs. "+str("%.2f" % ((q5) * 0.09))
                sT= "Rs. "+str("%.2f" % ((q5)))
                TT= "Rs. "+str("%.2f" % (q5+ ((q5) * 0.09)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(sT)
                self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
                q1=float(1000)
                q2=float(1500)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3+q4)
                Tax = "Rs. "+str("%.2f" % ((q5) * 0.09))
                sT= "Rs. "+str("%.2f" % ((q5)))
                TT= "Rs. "+str("%.2f" % (q5+ ((q5) * 0.09)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(sT)
                self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
                q1=float(500)
                q2=float(800)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3+q4)
                Tax = "Rs. "+str("%.2f" % ((q5) * 0.09))
                sT= "Rs. "+str("%.2f" % ((q5)))
                TT= "Rs. "+str("%.2f" % (q5+ ((q5) * 0.09)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(sT)
                self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
                q1=float(800)
                q2=float(1000)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3+q4)
                Tax = "Rs. "+str("%.2f" % ((q5) * 0.09))
                sT= "Rs. "+str("%.2f" % ((q5)))
                TT= "Rs. "+str("%.2f" % (q5+ ((q5) * 0.09)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(sT)
                self.var_total.set(TT)


        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
                q1=float(1000)
                q2=float(1500)
                q3=float(self.var_noofdays.get())
                q4=float(q1+q2)
                q5=float(q3+q4)
                Tax = "Rs. "+str("%.2f" % ((q5) * 0.09))
                sT= "Rs. "+str("%.2f" % ((q5)))
                TT= "Rs. "+str("%.2f" % (q5+ ((q5) * 0.09)))
                self.var_paidtax.set(Tax)
                self.var_actualtotal.set(sT)
                self.var_total.set(TT)




if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
