from tkinter import *
from tkinter import filedialog
import os
import docxpy as dx
import resume_finder as rf
from tkinter import scrolledtext
from PIL import ImageTk,Image
import importlib

def reset():
    #reset dir path
    s=entry_dir.get()
    ln=len(s)
    entry_dir.delete(0,ln)
    #reset keyword
    p=entry_key.get()
    ln2=len(p)
    entry_key.delete(0,ln2)
    #reset text box
    text_box.delete('1.0',END)
    
def browse():
    dir_path=filedialog.askdirectory()
    entry_dir.insert(0,dir_path)

def search():
    keyword=entry_key.get()
    dir_path=entry_dir.get()
    all_files, docx_files, matched_files=rf.search(dir_path,keyword)
    text_box.delete('1.0',END)
    res_str=""
    
    res_str=res_str+f'Total files found: {len(all_files)}\n'
    res_str=res_str+f'Total docx files found: {len(docx_files)}\n'
    res_str=res_str+f'Total Matched files: {len(matched_files)}\n'
    for res in matched_files:
        res_str=res_str+"  >"+res+"\n"
    text_box.insert(END,res_str)
def back():
    root.destroy()
    import main
    importlib.reload(main)

        
root=Tk()
root.geometry('850x500')
#root.state('zoomed')
img1=ImageTk.PhotoImage(image=Image.open('bg2.jpg').resize((850,500)))
bg=Label(root,image=img1)
bg.place(x=1,y=1)
img2=ImageTk.PhotoImage(image=Image.open('logo.png').resize((475,75)))
logo=Label(root,image=img2)
logo.place(x=0,y=400)
root.resizable(width=False,height=False)
root.title("My Project")

lbl_title=Label(root,text='Resume Finder',font=('algerian',24,'bold italic'))
lbl_title.place(x=150,y=10)

lbl_dir=Label(root,text="Directory Path:",font=('',14,'bold'))
lbl_dir.place(x=50,y=150)

lbl_key=Label(root,text="Keyword:",font=('',14,'bold'))
lbl_key.place(x=50,y=200)

entry_dir=Entry(root,font=('',14),bd=3)
entry_dir.place(x=200,y=150)


entry_key=Entry(root,font=('',14),bd=3)
entry_key.place(x=200,y=200)

btn_brwse=Button(root,command=browse,text=" Browse ",font=('',13),bd=3)
btn_brwse.place(x=440,y=150)
btn_srch=Button(root,text=" Search ",command=search,font=('',13),bd=3)
btn_srch.place(x=200,y=250)
btn_rst=Button(root,text=" Reset ",command=reset,font=('',13),bd=3)
btn_rst.place(x=300,y=250)
btn_back=Button(root,text=" Log Out ",command=back,font=('',13),bd=3)
btn_back.place(x=400,y=250)


text_box=scrolledtext.ScrolledText(root,width=35,height=20,font=('',10))
text_box.place(x=540,y=150)


root.mainloop()

    
