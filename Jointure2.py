# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:12:35 2019

@author: HP-PC
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfJoin1=pd.read_csv('Jointure1.csv')

df4 = pd.DataFrame({'Nom': ['S','S'],
                    'Prenom': ['D','T'],
                    'Naissance':[1999,2003],
                    'Sexe':['F','F']})

df5 = pd.DataFrame({'Nom': ['O','O'],
                    'Prenom': ['S','G'],
                    'Naissance':[1997,2006],
                    'Sexe':['M','F']})
'''
df6 = pd.DataFrame({'Nom': ['O'],
                    'Prenom': ['K'],
                    'Naissance':[1990],
                    'Sexe':['M']})
'''

dfJoin1=pd.merge(dfJoin1,df4, how = 'left',on=['Nom', 'Prenom'])
dfMerge4=dfJoin1.copy()

dfJoin1=pd.merge(dfJoin1,df5, how = 'left',on=['Nom', 'Prenom'])
dfMerge5=dfJoin1.copy()

'''dfJoin1=pd.merge(dfJoin1,df6, how = 'left',on=['Nom', 'Prenom'])
dfMerge6=dfJoin1.copy()'''

dfJoin1.reset_index(drop = True, inplace = True)

dfJoin1['Naissance'].update(dfJoin1.pop('Naissance_x'))
dfJoin1['Naissance'].update(dfJoin1.pop('Naissance_y'))
dfJoin1['Sexe'].update(dfJoin1.pop('Sexe_x'))
dfJoin1['Sexe'].update(dfJoin1.pop('Sexe_y'))

dfJoin1.to_csv('Jointure2.csv',index = False)