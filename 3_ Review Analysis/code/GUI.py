from tkinter import *
from tkinter import filedialog
import os
import docxpy as dx
from tkinter import messagebox
from review_analysis import Review
from PIL import ImageTk,Image
import importlib

def reset():
    #reset keyword
    p=entry_key.get()
    ln2=len(p)
    entry_key.delete(0,ln2)
    pred.config(text='Prediction:')

def predict():
    msg=entry_key.get()
    if(msg):
        res=Review(msg)
        pred.config(text=res)
    else:
        messagebox.showinfo("Error_Blank","Please type in your review")
def back():
    root.destroy()
    import main
    importlib.reload(main)
        


        
root=Tk()
root.geometry('500x500')
img1=ImageTk.PhotoImage(image=Image.open('bg2.jpg').resize((500,500)))
bg=Label(root,image=img1)
bg.place(x=1,y=1)
img2=ImageTk.PhotoImage(image=Image.open('logo.png').resize((475,75)))
logo=Label(root,image=img2)
logo.place(x=10,y=400)
root.resizable(width=False,height=False)
root.title("My Project")

lbl_title=Label(root,text='Review Analysis',font=('algerian',24,'bold italic'),bg='light grey')
lbl_title.place(x=100,y=10)


lbl_key=Label(root,text="Type in your Review",font=('',18,'bold'),bg='light grey')
lbl_key.place(x=120,y=150)

pred=Label(root,text='Prediction:',font=('times new roman',16,'bold italic'),fg='red',bg='white')
pred.place(x=240,y=350,anchor='center')

entry_key=Entry(root,font=('',14),bd=3)
entry_key.place(x=120,y=200)

btn_pred=Button(root,text="Predict",command=predict,font=('',13),bd=3)
btn_pred.place(x=120,y=250)
btn_rst=Button(root,text=" Reset ",command=reset,font=('',13),bd=3)
btn_rst.place(x=200,y=250)
btn_back=Button(root,text="Log Out",command=back,font=('',13),bd=3)
btn_back.place(x=280,y=250)



root.mainloop()

    
