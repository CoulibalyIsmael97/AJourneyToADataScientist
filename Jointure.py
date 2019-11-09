# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:40:58 2019

@author: HP-PC
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'Id':[1,2,3,4,5,6,7,8,9],
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


df=pd.merge(df,df1, how = 'left',on=['Nom', 'Prenom'])
dfMerge1=df.copy()


df=pd.merge(df,df2, how = 'left',on=['Nom', 'Prenom'])
dfMerge2=df.copy()


df=pd.merge(df,df3, how = 'left',on=['Nom', 'Prenom'])
dfMerge3=df.copy()

df.reset_index(drop = True, inplace = True)

df['Naissance'].update(df.pop('Naissance_x'))
df['Naissance'].update(df.pop('Naissance_y'))
df['Sexe'].update(df.pop('Sexe_x'))
df['Sexe'].update(df.pop('Sexe_y'))

'''df['Naissance']=df['Naissance'].fillna(df['Naissance_x'])
df['Naissance']=df['Naissance'].fillna(df['Naissance_y'])
df['Sexe']=df['Sexe'].fillna(df['Sexe_x'])
df['Sexe']=df['Sexe'].fillna(df['Sexe_y'])
df=df.drop(['Naissance_x', 'Naissance_y','Sexe_x','Sexe_y'], axis = 1)
'''