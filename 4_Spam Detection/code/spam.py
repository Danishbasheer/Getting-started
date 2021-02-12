from tkinter import *
import string
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from PIL import ImageTk,Image
import importlib
from tkinter import messagebox

sw=list(ENGLISH_STOP_WORDS)
sw.remove('not')

def removePunc(doc):
	pc=string.punctuation
	clean_doc=re.sub(f'[{pc}]','',doc)
	return clean_doc

df=pd.read_csv('sms.txt',delimiter='\t')
df.columns=['type','msg']
df['msg']=df.msg.apply(removePunc)
cv=CountVectorizer(stop_words=sw)

X=cv.fit_transform(df.msg).todense()
gnb=MultinomialNB()
gnb.fit(X,df.type)	

def mypredict():
        if(e.get()):                 
                new_rvw=e.get()
                X_test=cv.transform([new_rvw]).todense()
                p=gnb.predict(X_test)
                if(p[0]=='ham'):
                        l3.configure(text='Ham',fg='green')
                else:
                        l3.configure(text='Spam',fg='red')
        else:
                messagebox.showinfo("ErrorBlank","Type in a message")
                
def back():
        root.destroy()
        import main
        importlib.reload(main)

root=Tk()
root.geometry('800x500')
root.resizable(width=False,height=False)
img1=ImageTk.PhotoImage(image=Image.open('bg2.jpg').resize((800,500)))
bg=Label(root,image=img1)
bg.place(x=1,y=1)
img2=ImageTk.PhotoImage(image=Image.open('logo.png').resize((475,75)))
logo=Label(root,image=img2)
logo.place(x=175,y=400)

l=Label(root,text='Spam Detection',font=('Algerian',30,'bold'))
l.place(x=200,y=20)

l2=Label(root,text='Enter Msg:',font=('',16,'bold'))
l2.place(x=100,y=200)

l3=Label(root,text='Prediction',font=('',16,'bold'))
l3.place(x=300,y=100)

e=Entry(root,font=('',16,'bold'))
e.place(x=300,y=200)

b=Button(root,command=mypredict,text='Predict',font=('',14,'bold'))
b.place(x=300,y=300)
b2=Button(root,command=back,text='Log out',font=('',14,'bold'))
b2.place(x=400,y=300)

root.mainloop()
