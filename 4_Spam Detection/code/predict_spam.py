import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

df=pd.read_csv('dataset/sms.txt',delimiter='\t')
df.columns=['label','msg']
cv=CountVectorizer(stop_words='english')
X=cv.fit_transform(df.msg).todense()
y=df.iloc[:,0].values
mnb=MultinomialNB()
mnb.fit(X,y)
msg=input('enter msg:')
X_test=cv.transform([msg])
pred=mnb.predict(X_test)
print(pred[0])


