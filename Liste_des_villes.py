# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:34:06 2019

@author: HP-PC
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df_slice_modified_add_city=pd.read_csv('2008_1_modified_add_city.csv')
a=df_slice_modified_add_city['City'].value_counts()

total=sum(list(a.values)[0:30])
'''
#'Id':[1,2,3,4,5,6,7,8,9],
df = pd.DataFrame({
                   'Nom': ['C', 'C', 'C', 'C', 'C', 'K','K','D','D'],
                    'Prenom': ['Y', 'Ab', 'F', 'W', 'Au', 'N','F','Dr','A']})

df1 = pd.DataFrame({'Nom': ['C', 'C', 'C', 'C', 'C'],
                    'Prenom': ['Y', 'Ab', 'F', 'W', 'Au'],
                    'Naissance':[1967,1970,1997,2000,2004],
                    'Sexe':['M','F','M','F','F']})

df2 = pd.DataFrame({'Nom': ['K','K'],
                    'Prenom': ['N','F'],
                    'Naissance':[1965,1971],
                    'Sexe':['F','F']})

df3 = pd.DataFrame({'Nom': ['D','D'],
                    'Prenom': ['Dr','A'],
                    'Naissance':[1980,1981],
                    'Sexe':['M','F']})


df=pd.merge(df,df1, how = 'outer')

df=pd.merge(df,df2, how = 'outer')
dfMerge2=df.copy()

df=pd.merge(df,df3, how = 'outer')
dfMerge3=df.copy()

df=df.dropna()

df.reset_index(drop = True, inplace = True)

initial=pd.DataFrame({'Id':[1,2,3,4,5,6,7,8,9],
                   'Nom': ['C', 'C', 'C', 'C', 'C', 'K','K','D','D'],
                    'Prenom': ['Y', 'Ab', 'F', 'W', 'Au', 'N','F','Dr','A']})

initial['Naissance']=df['Naissance'].values
'''