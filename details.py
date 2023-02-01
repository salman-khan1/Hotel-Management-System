from multiprocessing import parent_process
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1150x490+220+220")


################Title################
        lbl_title=Label(self.root,text="ROOM  DETAILS",font=("times new roman",18,"bold"),background="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

      ###########logo#######  
        img2=Image.open("images\logohotel.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoImg2=ImageTk.PhotoImage(img2) 

        lblimg=Label(self.root,image=self.photoImg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

##############LABEl Frame###########
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=1)
        labelframeleft.place(x=5,y=50,width=480,height=350)


            ###Floor
        lbl_floor=Label(labelframeleft,text="Floor :",font=("arial",11,"bold"),padx=1,pady=4)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=18,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

            ###Room no
        lbl_RoomNo=Label(labelframeleft,text="Room No :",font=("arial",11,"bold"),padx=1,pady=4)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_RoomNo=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=18,font=("arial",13,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

            ###Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type :",font=("arial",11,"bold"),padx=1,pady=4)
        lbl_RoomType.grid(row=2,column=0,sticky=W)
        self.var_RoomType=StringVar()

        entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=18,font=("arial",13,"bold"))
        entry_RoomType.grid(row=2,column=1,sticky=W)


                #############BTN################3
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=30,y=150,width=340,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnAdd.grid(row=0,column=0,padx=2)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnUpdate.grid(row=0,column=1,padx=2)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnDelete.grid(row=0,column=2,padx=2)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnReset.grid(row=0,column=3,padx=2)

   ###############Table Frame search system#######################
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=1)
        Table_Frame.place(x=500,y=50,width=550,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,columns=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)



        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomType",text="Room Type")


        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)


        self.fetch_data()

##########ADD DATA
    def add_data(self):

        if self.var_floor.get()=="" or self.var_RoomType.get()=="":

                messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
                try:
                
                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                        self.var_floor.get(),
                                                                                        self.var_RoomNo.get(),
                                                                                        self.var_RoomType.get(),
                                                                               
                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","New Room Added Succesfully", parent=self.root)
                except Exception as es:
                        messagebox.showwarning("Warning",f"Some thing went wrong {str(es)}",parent=self.root)

                  ###FETCH DATA#####      
    def fetch_data(self):
        

        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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


        self.var_floor.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2])

#####Update data
    def update(self):
        if self.var_floor.get()=="":
                messagebox.showerror("Error","Please Enter Correct Room No",parent=self.root)

        else:
                try:
                        
                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update details set Floor=%s, RoomType=%s where RoomNo=%s",(
                                                                                                                                                                        self.var_floor.get(),
                                                                                                                                                                        self.var_RoomType.get(),
                                                                                                                                                                        self.var_RoomNo.get()
                                                                                                                                                                                                        ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Updated","Room details has been updated successfully",parent=self.root)
                except Exception as es:

                        messagebox.showwarning("Warning",f"Some thing went wrong {str(es)}",parent=self.root)

##DELETE
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Managment System","Do You Want to Delete this Room",parent=self.root)
        if mDelete>0:
                try:

                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="managment")
                        my_cursor=conn.cursor()
                        query="delete from details where RoomNo=%s"
                        value=(self.var_RoomNo.get(),)
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
        self.var_floor.set("")
        self.var_RoomNo.set("")
        self.var_RoomType.set("")   

if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()
