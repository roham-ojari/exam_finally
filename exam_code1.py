from tkinter import *
from tkinter import messagebox
import exam_code2
win = Tk()
win.geometry("540x350+430+200")
win.resizable(0,0)
win.config(bg="light blue")
#====================================
win.geometry("500x400")
win.resizable(0,0)
win.title("Login Form")
#====================================
oj1 = exam_code2.Exam("D:/python3/Exam_1/data.db")
oj1.create_table()
#====================================
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_email.delete(0,END)
    ent_pass.delete(0,END)
def insert():
    oj1.insert(ent_fname.get(),ent_lname.get(),ent_email.get(),ent_pass.get())
def sign_up():
    if len(ent_email.get()) == 0 or len(ent_pass.get()) == 0:
        messagebox.showerror("NO!!","please fill the force field")
        return True
    s = oj1.read()
    for i in s:
        if ent_email.get() == i[3]:
            messagebox.showerror("NO!!","This email is already sign in")
            return True
    insert()
def sign_in():
    if len(ent_email.get()) == 0 or len(ent_pass.get()) == 0:
        messagebox.showerror("NO!!","please fill the force field")
        return True
    s = oj1.read()
    for i in s:
        if ent_email.get() == i[3] and ent_pass.get() == i[4]:
            messagebox.showinfo("YES","Wellcome!!")
            clear()
            return True
    messagebox.showerror("NO!!","This account isn't sign in")

#====================================
lbl_fname = Label(text="Name :",font=20,bg="light blue")
lbl_fname.place(x=80,y=20)

lbl_lname = Label(text="Family :",font=20,bg="light blue")
lbl_lname.place(x=80,y=100)

lbl_email = Label(text="* Email :",font=20,bg="light blue")
lbl_email.place(x=70,y=180)
 
lbl_pass = Label(text="* Password :",font=20,bg="light blue")
lbl_pass.place(x=70,y=240)



#================================================
ent_fname =Entry(win,font=20)
ent_fname.place(x=160,y=20)

ent_lname =Entry(win,font=20)
ent_lname.place(x=160,y=100)

ent_email =Entry(win,font=20)
ent_email.place(x=160,y=180)

ent_pass =Entry(win,show="*",font=20)
ent_pass.place(x=180,y=240)


# ent_pass2 =Entry(win)
# ent_pass2.place(x=70,y=320,width=250)

btn_up = Button(win,text="Sign Up",command=sign_up,font=20)
btn_up.place(x=100,y=300)
btn_in = Button(win,text="Sign In",command=sign_in,font=20)
btn_in.place(x=300,y=300)
win.mainloop()