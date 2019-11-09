# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:38:52 2019

@author: HP-PC
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime

df = pd.read_csv('2008.csv')
#print(df.head())
#df_slice=df[df['WeatherDelay']>0]
#print(df_slice.head())
df_slice=pd.read_csv('2008_1.csv')
'''print(df.describe())
print(df_slice.describe(include='all'))
print(df_slice.dtypes)'''

for col in df_slice.columns:
    print(df_slice[col].describe())
    

# Créer une nouvelle fonction qui détermine si la valeur en paramètre est manquante:
def num_missing(x):
    return sum(x.isnull())

# On applique cette fonction  au dataset principal 2 pour chaque colonne:
print("Valeurs manquantes par colonne:")
print(df_slice.apply(num_missing, axis=0)) #axis=0 définit que la fonction sera bien appliquée sur chaque colonne

a=df_slice['Month'].value_counts()
print(a)
df_slice['Month'].hist(figsize=(12,8))

y=pd.value_counts(df_slice['Month'].values, sort=False)
print(y)

data = pd.DataFrame({'temps': [2015, 2016]})
pd.to_datetime('2015', format='%Y%m%d', errors='ignore')

#conversion string en heure:minute
'''
t="49"
a = pd.to_datetime(t, format='%H%M')
print(a.hour)
print(a.minute)
print(a.hour,":",a.minute)
'''
'''
#Modifier le nom d'une colonne
myList = list(df_slice.columns)
myList[2] = 'Day'
df_slice.columns = myList

#Créer une colonne "Start_Date"
df_slice["Start_Date"] = pd.to_datetime(df_slice[['Year','Month', 'Day']])
'''

'''
conserve=""
def convertHourMinute(s):
    print(type(s))
    if type(s) is int or type(s) is float:
        s=str(s)
    if len(s)<2:
        s=s+"0"
    #if len(s)==2:
        
    print(type(s))
    temporaire = pd.to_datetime(s, format='%H%M',errors='raise')
    if type(temporaire) is str:
        conserve = temporaire
        print(conserve)
    else:
        return temporaire.hour,temporaire.minute

convertHourMinute(900)
'''


def findHour(s):
    s=int(s)
    if (len(str(s)))>=3:
        return s//100
    
    if (len(str(s)))==2 and s<24:
        return s
    
    if (len(str(s)))==2 and s>24:
        return s//10

findHour(1829.0)

#df_slice['DepTime']=df_slice['DepTime'].astype(object)
df_slice['hour']=df_slice['DepTime'].apply(lambda x : findHour(x))
