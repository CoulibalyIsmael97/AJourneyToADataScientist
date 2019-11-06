# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:39:51 2019

@author: HP-PC
"""

'''

Ce code permet de générer le fichier "2008_1_modified.csv"

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_slice=pd.read_csv('2008_1.csv')

# Convertion des numeros des jours en chaine de caractères
def numToday(x):
    if x==1:
        return "Monday"
    if x==2:
        return "Tuesday"
    if x==3:
        return "Wednesday"
    if x==4:
        return "Thursday"
    if x==5:
        return "Friday"
    if x==6:
        return "Saturday"
    if x==7:
        return "Sunday"
    

# Convertion des numeros des mois en chaine de caractères
def numToMonth(x):
    if x==1:
        return "January"
    if x==2:
        return "February"
    if x==3:
        return "March"
    if x==4:
        return "April"
    if x==5:
        return "May"
    if x==6:
        return "June"
    if x==7:
        return "July"
    if x==8:
        return "August"
    if x==9:
        return "September"
    if x==10:
        return "October"
    if x==11:
        return "November"
    if x==12:
        return "December"
    
df_slice['DayOfWeek']= df_slice['DayOfWeek'].apply(lambda x : numToday(x) )
df_slice['Month']= df_slice['Month'].apply(lambda x : numToMonth(x) )
df_slice['FlightNum']=df_slice['FlightNum'].astype(object)
df_slice['DepTime']=df_slice['DepTime'].astype(object)
df_slice['CRSDepTime']=df_slice['CRSDepTime'].astype(object)
df_slice['ArrTime']=df_slice['ArrTime'].astype(object)
df_slice['CRSArrTime']=df_slice['CRSArrTime'].astype(object)

df_slice_modified=df_slice
df_slice_modified.to_csv('2008_1_modified.csv',index = False)