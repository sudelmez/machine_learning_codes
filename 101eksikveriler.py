import numpy as np
import pandas as pd
import matplotlib as plt 

veriler = pd.read_csv('eksikveriler.csv') 

print(veriler)
 
from sklearn.impute import SimpleImputer
 
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')

yas=veriler.iloc[:,1:4].values #integer to location
print(yas)

imputer=imputer.fit(yas[:,1:4]) #istenileni bulur...1den 4e kadar olan columnlar
yas[:,1:4]=imputer.transform(yas[:,1:4]) #istenileni değiştirir
#yas columunun ortalaması alınır ve transform ile istenilen değerlerin yerine koyulur 
print(yas)