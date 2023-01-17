#open window
"""
import tkinter
win=tkinter.Tk()
wi=win.winfo_screenwidth()
he=win.winfo_screenheight()
print(wi)
print(he)
win.configure(width=wi,height=he,bg="red")
win.mainloop()
"""
#user name create box
"""
import tkinter
win=tkinter.Tk()
wi=win.winfo_screenwidth()
he=win.winfo_screenheight()
win.configure(width=wi,height=he,bg="gold")
def show():
    print("test")
l1=tkinter.Label(win,text="enter user name:")
l1.place(x=300,y=100)
t1=tkinter.Entry(win)
t1.place(x=450,y=100)
l2=tkinter.Label(win,text="enter passward:")
l2.place(x=300,y=200)
t2=tkinter.Entry(win,show="#")
t2.place(x=450,y=200)
b1=tkinter.Button(win,text="click me",command=show)
b1.place(x=450,y=300)
win.mainloop()
"""
#message box
"""
import tkinter
from tkinter import messagebox
win=tkinter.Tk()
wi=win.winfo_screenwidth()
he=win.winfo_screenheight()
win.configure(width=wi,height=he,bg="gold")
def show():
    #messagebox.showinfo("success","data saved")
    #messagebox.showerror("success","data saved")
    messagebox.showwarning("success","data saved")
l1=tkinter.Label(win,text="enter user name:")
l1.place(x=300,y=100)
t1=tkinter.Entry(win)
t1.place(x=450,y=100)
l2=tkinter.Label(win,text="enter passward:")
l2.place(x=300,y=200)
t2=tkinter.Entry(win,show="#")
t2.place(x=450,y=200)
b1=tkinter.Button(win,text="click me",command=show)
b1.place(x=450,y=300)
win.mainloop()
"""
# photo insert
"""
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
win=tkinter.Tk()
wi=win.winfo_screenwidth()
he=win.winfo_screenheight()
win.configure(width=wi,height=he,bg="gold")
def show():
    #messagebox.showinfo("success","data saved")
    #messagebox.showerror("failure","data saved")
    messagebox.showwarning("failure","data saved")
l1=tkinter.Label(win,text="enter user name:")
l1.place(x=300,y=100)
t1=tkinter.Entry(win)
t1.place(x=450,y=100)
l2=tkinter.Label(win,text="enter passward:")
l2.place(x=300,y=200)
t2=tkinter.Entry(win,show="#")
t2.place(x=450,y=200)
b1=tkinter.Button(win,text="click me",command=show)
b1.place(x=450,y=300)
path=Image.open("E:/imgae1/poo.jpg")
res=ImageTk.PhotoImage(path)
imglbl=tkinter.Label(win,image=res)
imglbl.place(x=700,y=200)
win.mainloop()
"""
#connector sql
"""
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
win=tkinter.Tk()
wi=win.winfo_screenwidth()
he=win.winfo_screenheight()
win.configure(width=wi,height=he,bg="gold")
def show():
    un=t1.get()
    pw=t2.get()
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="poo")
    print("connection success")
    cur=con.cursor()
    cur.execute("insert into login values('%s','%s')"%(un,pw))
    con.commit()
    messagebox.showinfo("success",un+" "+pw)
    #messagebox.showerror("failure","data saved")
    #messagebox.showwarning("failure","data saved")
    clearfun()
def clearfun():
    t1.delete(0,"end")
    t2.delete(0,"end")
    t1.focus()
l1=tkinter.Label(win,text="enter user name:")  
l1.place(x=300,y=100)
t1=tkinter.Entry(win)
t1.place(x=450,y=100)
l2=tkinter.Label(win,text="enter passward:")
l2.place(x=300,y=200)
t2=tkinter.Entry(win,show="#")
t2.place(x=450,y=200)
b1=tkinter.Button(win,text="click me",command=show)
b1.place(x=450,y=300)
path=Image.open("E:/imgae1/poo.jpg")
res=ImageTk.PhotoImage(path)
imglbl=tkinter.Label(win,image=res)
imglbl.place(x=700,y=200)
win.mainloop()
"""
# insert and search
"""
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
win=tkinter.Tk()
wi=win.winfo_screenwidth()
he=win.winfo_screenheight()
win.configure(width=wi,height=he,bg="gold")
testlist=[0]
def searchfun():
    un=t1.get()
    isvaliduser=False
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="Poo")
    print("connection success")
    cur=con.cursor()
    cur.execute("select * from login")
    alldata=cur.fetchall()    
    for ans in alldata:
        #print(ans[0],ans[1])
        if ans[0]==un:
            isvaliduser=True
            testlist[0]=True
            messagebox.showinfo("success","valid user")
            break
    if isvaliduser==False:
        testlist[0]=False
        messagebox.showerror("faliure","invalid user")

def insertfun():
    un=t1.get()
    pw=t2.get()

    
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="poo")
    print("connection success")
    cur=con.cursor()
    cur.execute("insert into login values('%s','%s')"%(un,pw))
    con.commit()    
    #print("test")
    messagebox.showinfo("success",un+"  "+pw)
    #messagebox.showerror("failure","data saved")
    #messagebox.showwarning("failure","data saved")
    clearfun()
def clearfun():
    t1.delete(0,"end")
    t2.delete(0,"end")
    t1.focus()
l1=tkinter.Label(win,text="enter user name:")  
l1.place(x=300,y=100)
t1=tkinter.Entry(win)
t1.place(x=450,y=100)
l2=tkinter.Label(win,text="enter passward:")
l2.place(x=300,y=200)
t2=tkinter.Entry(win,show="#")
t2.place(x=450,y=200)
b1=tkinter.Button(win,text="insert/save",command=insertfun)
b1.place(x=450,y=300)
b2=tkinter.Button(win,text="Search",command=searchfun)
b2.place(x=550,y=300)

path=Image.open("E:/imgae1/poo.jpg")
res=ImageTk.PhotoImage(path)
imglbl=tkinter.Label(win,image=res)
imglbl.place(x=1000,y=200)
win.mainloop()
"""
#delete botton
"""
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
win=tkinter.Tk()
wi=win.winfo_screenwidth()
he=win.winfo_screenheight()
win.configure(width=wi,height=he,bg="gold")
testlist=[0]
def deletefun():
    un=t1.get()
    searchfun()    
    #print(testlist[0])
    if testlist[0]==True:
        con=mysql.connector.connect(host="localhost",user="root",password="12345",database="Poo")
        print("connection success") 
        cur=con.cursor()
        cur.execute("delete from login where uname='%s'"%un)
        con.commit()
        messagebox.showinfo("succes","delete success")

def searchfun():
    un=t1.get()
    isvaliduser=False
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="Poo")
    print("connection success")
    cur=con.cursor()
    cur.execute("select * from login")
    alldata=cur.fetchall()    
    for ans in alldata:
        #print(ans[0],ans[1])
        if ans[0]==un:
            isvaliduser=True
            testlist[0]=True
            messagebox.showinfo("success","valid user")
            break
    if isvaliduser==False:
        testlist[0]=False
        messagebox.showerror("faliure","invalid user")

def insertfun():
    un=t1.get()
    pw=t2.get()

    
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="poo")
    print("connection success")
    cur=con.cursor()
    cur.execute("insert into login values('%s','%s')"%(un,pw))
    con.commit()    
    #print("test")
    messagebox.showinfo("success",un+"  "+pw)
    #messagebox.showerror("failure","data saved")
    #messagebox.showwarning("failure","data saved")
    clearfun()
def clearfun():
    t1.delete(0,"end")
    t2.delete(0,"end")
    t1.focus()
l1=tkinter.Label(win,text="enter user name:")  
l1.place(x=300,y=100)
t1=tkinter.Entry(win)
t1.place(x=450,y=100)
l2=tkinter.Label(win,text="enter passward:")
l2.place(x=300,y=200)
t2=tkinter.Entry(win,show="#")
t2.place(x=450,y=200)
b1=tkinter.Button(win,text="insert/save",command=insertfun)
b1.place(x=450,y=300)
b2=tkinter.Button(win,text="Search",command=searchfun)
b2.place(x=550,y=300)
b3=tkinter.Button(win,text="Delete",command=deletefun)
b3.place(x=650,y=300)
path=Image.open("E:/imgae1/poo.jpg")
res=ImageTk.PhotoImage(path)
imglbl=tkinter.Label(win,image=res)
imglbl.place(x=1000,y=200)
win.mainloop()
"""
# update

import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
win=tkinter.Tk()
wi=win.winfo_screenwidth()
he=win.winfo_screenheight()
win.configure(width=wi,height=he,bg="gold")
testlist=[False]
def updatefun():
    un=t1.get()
    pw=t2.get()
    if len(un)==0:
        messagebox.showwarning("fill","must fill username")
    else:
        searchfun()
        if testlist[0]==True:
            con=mysql.connector.connect(host="localhost",user="root",password="12345",database="Poo")
            print("connection success") 
            cur=con.cursor()
            cur.execute("update login set pword='%s' where uname='%s'"%(pw,un))
            con.commit()
            messagebox.showinfo("succes","update success")
            clearfun()
def deletefun():
    un=t1.get()
    searchfun()    
    #print(testlist[0])
    if testlist[0]==True:
        con=mysql.connector.connect(host="localhost",user="root",password="12345",database="Poo")
        print("connection success") 
        cur=con.cursor()
        cur.execute("delete from login where uname='%s'"%un)
        con.commit()
        messagebox.showinfo("succes","delete success")

def searchfun():
    un=t1.get()
    isvaliduser=False
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="Poo")
    print("connection success")
    cur=con.cursor()
    cur.execute("select * from login")
    alldata=cur.fetchall()    
    for ans in alldata:
        #print(ans[0],ans[1])
        if ans[0]==un:
            isvaliduser=True
            testlist[0]=True
            messagebox.showinfo("success","valid user")
            break
    if isvaliduser==False:
        testlist[0]=False
        messagebox.showerror("faliure","invalid user")

def insertfun():
    un=t1.get()
    pw=t2.get()

    
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="poo")
    print("connection success")
    cur=con.cursor()
    cur.execute("insert into login values('%s','%s')"%(un,pw))
    con.commit()    
    #print("test")
    messagebox.showinfo("success",un+"  "+pw)
    #messagebox.showerror("failure","data saved")
    #messagebox.showwarning("failure","data saved")
    clearfun()
def clearfun():
    t1.delete(0,"end")
    t2.delete(0,"end")
    t1.focus()
l1=tkinter.Label(win,text="enter user name:")  
l1.place(x=300,y=100)
t1=tkinter.Entry(win)
t1.place(x=450,y=100)
l2=tkinter.Label(win,text="enter passward:")
l2.place(x=300,y=200)
t2=tkinter.Entry(win,show="#")
t2.place(x=450,y=200)
b1=tkinter.Button(win,text="insert/save",command=insertfun)
b1.place(x=450,y=300)
b2=tkinter.Button(win,text="Search",command=searchfun)
b2.place(x=550,y=300)
b3=tkinter.Button(win,text="Delete",command=deletefun)
b3.place(x=650,y=300)
b4=tkinter.Button(win,text="Update",command=updatefun)
b4.place(x=750,y=300)

path=Image.open("E:/imgae1/poo.jpg")
res=ImageTk.PhotoImage(path)
imglbl=tkinter.Label(win,image=res)
imglbl.place(x=1000,y=200)
win.mainloop()
