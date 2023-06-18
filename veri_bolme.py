import numpy as np
import pandas as pd
import matplotlib as plt 

veriler = pd.read_csv('veriler.csv') 

print(veriler)

ulke= veriler.iloc[:,0:1].values #bir columnda tüm satır verileri alıyor 
print(ulke) #numpy (obje) dizisi. bunu nümeriğe çevirmeliyiz

from sklearn import preprocessing

le= preprocessing.LabelEncoder()
ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke) #sırayla kategorik olarak numaralandırılıyor

ohe=preprocessing.OneHotEncoder()
ulke=ohe.fit_transform(ulke).toarray() #bir önceki kategoriler öğrenip ona göre array oluşturuyor. true olan veri 1
print(ulke)

print("-----------------")

print(list(range(22)))
sonuc= pd.DataFrame(data=ulke,index=range(22),columns=['fr','tr','us'])
print(sonuc)

cinsiyet= veriler.iloc[:,-1].values

yas=veriler.iloc[:,1:4].values 
print(yas)

sonuc2= pd.DataFrame(data=yas,index=range(22),columns=['boy','kilo','yas'])

sonuc3= pd.DataFrame(data=cinsiyet,index=range(22),columns=['cinsiyet'])
print(sonuc2)
s=pd.concat([sonuc,sonuc2],axis=1) #iki sonucu birleştiriyor
print(s)
s2=pd.concat([s,sonuc3],axis=1)
print(s2)


from sklearn.model_selection import train_test_split #belli bir satıra kadar olanlar train, sonra olanlar test

x_train, x_test, y_train, y_test= train_test_split(s,sonuc3,test_size=0.33,random_state=0) #3te1 oranında satır işleme girecek. 0ıncı indeksten başlayacak
print(x_train)

