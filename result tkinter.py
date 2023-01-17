import tkinter
from tkinter import messagebox
import mysql.connector
win=tkinter.Tk()
wi=win.winfo_screenwidth()
he=win.winfo_screenheight()
print(wi)
print(he)
win.configure(width=wi,height=he,bg="pink")
testlist=[0]
def searchfun():
    rno=t1.get()
    dob=t2.get()
    isvaliduser=False
    con=mysql.connector.connect(host="localhost",user="root",password="12345",database="flower")
    print("connection success")
    cur=con.cursor()
    cur.execute("select * from result")
    alldata=cur.fetchall()
    for ans in alldata:
        if str(ans[0])==rno and str(ans[2])==dob:
            isvaliduser=True
            testlist[0]=True
            messagebox.showinfo("success","valid user")
            break
    if isvaliduser==False:
        messagebox.showerror("faliure","invalid user")
    clearfun()
        
def clearfun():
    t1.delete(0,"end")
    t2.delete(0,"end")
    t1.focus()


l1=tkinter.Label(win,text="SSLC Examination Results May 2022",bg="gold")
l1.place(x=300,y=50)
a1=tkinter.Label(win,text="Rigester No :",bg="red")
a1.place(x=100,y=100)
t1=tkinter.Entry (win)
t1.place(x=350,y=100)
a2=tkinter.Label(win,text="Date of Birth(dd/mm/yyyy) :",bg="red")
a2.place(x=100,y=150)
t2=tkinter.Entry(win)
t2.place(x=350,y=150)
b1=tkinter.Button(win,text="Get marks",command=searchfun)
b1.place(x=350,y=200)

win.mainloop()

"""
    """
