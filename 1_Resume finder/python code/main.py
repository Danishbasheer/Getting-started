from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import importlib
 
def reset():
    #reset user enrty
    s=entry_usr.get()
    ln=len(s)
    entry_usr.delete(0,ln)
    #reset password entry
    p=entry_pass.get()
    ln2=len(p)
    entry_pass.delete(0,ln2)

def login():
    u=entry_usr.get()
    p=entry_pass.get()
    if(u.lower()=='admin' and p.lower()=='admin'):
        root.destroy()
        import gui_2
        importlib.reload(gui_2)
    else:
        messagebox.showinfo("Login Failed","Invalid Username or Password")
root=Tk()
root.geometry('475x400')
#root.state('zoomed')
#root.configure(bg='light grey')
root.resizable(width=False,height=False)
root.title("My Project")
img1=ImageTk.PhotoImage(image=Image.open('bg.jpg').resize((475,400)))
bg=Label(root,image=img1)
bg.place(x=1,y=1)
img2=ImageTk.PhotoImage(image=Image.open('logo.png').resize((475,75)))
logo=Label(root,image=img2)
logo.place(x=0,y=325)


lbl_title=Label(root,text='Resume Finder',font=('algerian',24,'bold italic'))
lbl_title.place(x=130,y=20)

lbl_usr=Label(root,text="username:",font=('arial',16))
lbl_usr.place(x=50,y=150)

lbl_pass=Label(root,text="password:",font=('arial',16))
lbl_pass.place(x=50,y=200)

entry_usr=Entry(root,font=('',16),bd=3)
entry_usr.place(x=165,y=150)

entry_pass=Entry(root,font=('',16),bd=3,show='*')
entry_pass.place(x=165,y=200)

btn_lgn=Button(root,command=login,text=" Log In ",font=('',14),bd=3)
btn_lgn.place(x=200,y=250)
btn_rst=Button(root,text=" Reset ",command=reset,font=('',14),bd=3)
btn_rst.place(x=300,y=250)




root.mainloop()

    
