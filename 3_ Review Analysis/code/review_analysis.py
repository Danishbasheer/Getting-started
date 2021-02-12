import pandas as pd
import re
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import stop_words
from sklearn.naive_bayes import MultinomialNB


sw=list(stop_words.ENGLISH_STOP_WORDS)
sw.remove('not')
sw.remove('no')
sw.remove("cannot")
sw.remove("cant")
    
cv=CountVectorizer(stop_words=sw,ngram_range=(2,3))

def clean_text(text):
    #change to lower case
    text=text.lower()
    
    #remove punctuations
    punc=string.punctuation
    text=re.sub(f'[{punc}]','',text)
    
    return text

def feature_vectors(clean_text_list):
    fv=cv.fit_transform(clean_text_list)
    return fv

def Review(msg):
    df=pd.read_csv('Restaurant_Reviews.txt',delimiter='\t')   
    df['Review']=df.Review.apply(clean_text)

    X=feature_vectors(df.Review)
    y=df.Liked
    gnb=MultinomialNB()
    gnb.fit(X.todense(),y)

    msg_new=cv.transform([msg]).todense()
    pred=gnb.predict(msg_new)
    if(pred[0]==1):
        return "Liked"
    else:
        return 'Disliked'


