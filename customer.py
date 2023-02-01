from multiprocessing import parent_process
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1150x490+220+220")


        ################Variables################
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_father=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()

################Title################
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),background="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

      ###########logo#######  
        img2=Image.open("images\logohotel.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoImg2=ImageTk.PhotoImage(img2) 

        lblimg=Label(self.root,image=self.photoImg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        
##############LABEl Frame###########
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=1)
        labelframeleft.place(x=5,y=50,width=390,height=420)

##############LABEl and Entries###########

            ###cust Ref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref:",font=("arial",12,"bold"),padx=1,pady=4)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=25,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #Customer Name
        cname=Label(labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=1,pady=4)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=25,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)

        ###FAther name
        lblfname=Label(labelframeleft,text="Father Name:",font=("arial",12,"bold"),padx=1,pady=4)
        lblfname.grid(row=2,column=0,sticky=W)
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_father,width=25,font=("arial",13,"bold"))
        entry_ref.grid(row=2,column=1)

        ###Gender Combobox
        label_gender=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=1,pady=4)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=23,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)



        #postcode
        lblpostcode=Label(labelframeleft,text="PostCode:",font=("arial",12,"bold"),padx=1,pady=4)
        lblpostcode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=25,font=("arial",13,"bold"))
        txtPostCode.grid(row=4,column=1)

        #mobiel number
        lblMobile=Label(labelframeleft,text="Mobile:",font=("arial",12,"bold"),padx=1,pady=4)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=25,font=("arial",13,"bold"))
        txtMobile.grid(row=5,column=1)


        #email
        lblEmail=Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=1,pady=4)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=25,font=("arial",13,"bold"))
        txtEmail.grid(row=6,column=1)

        #nationality
        lblNationality=Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=1,pady=4)
        lblNationality.grid(row=7,column=0,sticky=W) 

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=23,state="readonly")
        combo_Nationality["value"]=("Pakistani","Foreign")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        #idproof type combobox
        lblIdProof=Label(labelframeleft,text="ID Proof Type:",font=("arial",12,"bold"),padx=1,pady=4)
        lblIdProof.grid(row=8,column=0,sticky=W)
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=23,state="readonly")
        combo_id["value"]=("CNIC","Student Card","Driving License","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)


        #id Number
        lbIdNumber=Label(labelframeleft,text="ID Number:",font=("arial",12,"bold"),padx=1,pady=4)
        lbIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=25,font=("arial",13,"bold"))
        txtIdNumber.grid(row=9,column=1)

         #Address
        lblAddress=Label(labelframeleft,text="Address:",font=("arial",12,"bold"),padx=1,pady=4)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=25,font=("arial",13,"bold"))
        txtAddress.grid(row=10,column=1)

        #############BTN################3
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=30,y=350,width=340,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data ,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnAdd.grid(row=0,column=0,padx=2)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnUpdate.grid(row=0,column=1,padx=2)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnDelete.grid(row=0,column=2,padx=2)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnReset.grid(row=0,column=3,padx=2)


    ###############Table Frame search system#######################
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",12,"bold"),padx=1)
        Table_Frame.place(x=400,y=50,width=860,height=490)
        # Table_Frame.place(x=435,y=50,width=650,height=490)

        lblSearchBy=Label(Table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=1)
        # lblSearchBy.grid(row=0,column=0,sticky=W,padx=1)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=15,state="readonly")
        combo_Search["value"]=("Mobile","Ref","postCode")
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


#####################Show Data Table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=760,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","father","gender","post","mobile","email","nationality",
                                                                    "idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("father",text="Father Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=70)
        self.Cust_Details_Table.column("name",width=70)
        self.Cust_Details_Table.column("father",width=70)
        self.Cust_Details_Table.column("gender",width=70)
        self.Cust_Details_Table.column("post",width=70)
        self.Cust_Details_Table.column("mobile",width=70)
        self.Cust_Details_Table.column("email",width=70)
        self.Cust_Details_Table.column("nationality",width=70)
        self.Cust_Details_Table.column("idproof",width=70)
        self.Cust_Details_Table.column("idnumber",width=70)
        self.Cust_Details_Table.column("address",width=70)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_data(self):

        if self.var_mobile.get()=="" or self.var_cust_name.get()=="" or self.var_id_number.get()=="":

                messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
                try:
                
                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_ref.get(),
                                                                                        self.var_cust_name.get(),
                                                                                        self.var_father.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_post.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_nationality.get(),
                                                                                        self.var_id_proof.get(),
                                                                                        self.var_id_number.get(),
                                                                                        self.var_address.get()
                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","customer has been added", parent=self.root)
                except Exception as es:
                        messagebox.showwarning("Warning",f"Some thing went wrong {str(es)}",parent=self.root)
                
    def fetch_data(self):

        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from Customer")
        row=my_cursor.fetchall()
        if len(row)!=0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in row:
                        self.Cust_Details_Table.insert("",END,values=i)
                conn.commit()
                conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]


        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_father.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
                messagebox.showerror("Error","Please Enter Mobile number",parent=self.root)
        else:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                my_cursor=conn.cursor()
                my_cursor.execute("update customer set Name=%s,Father=%s,Gender=%s,postCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                                                                                self.var_cust_name.get(),
                                                                                                                                                                self.var_father.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_post.get(),
                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_nationality.get(),
                                                                                                                                                                self.var_id_proof.get(),
                                                                                                                                                                self.var_id_number.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_ref.get()
                                                                                                                                                                                                       ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Updated","Customer details has been updated successfully",parent=self.root)


    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Managment System","Do You Want to Delete this Customer",parent=self.root)
        if mDelete>0:

                conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                my_cursor=conn.cursor()
                query="delete from customer where Ref=%s"
                value=(self.var_ref.get(),)
                my_cursor.execute(query,value)
        else:
                if not mDelete:
                        return
        conn.commit()
        self.fetch_data()
        conn.close()

 
    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_father.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
      
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM customer WHERE "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                        self.Cust_Details_Table.insert("",END,values=i)
                conn.commit()
        conn.close()




               
if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()

