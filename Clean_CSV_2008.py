# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:14:19 2019

@author: HP-PC
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('2008_1_modified_add_x_time.csv')

df=df.drop(['FlightNum', 'TailNum', 'TaxiIn', 'TaxiOut', 'Cancelled', 'CancellationCode', 'Diverted', 'Hour'], axis = 1) 

df = df.dropna()
df.to_csv('Clean_2008.csv',index = False)

# Créer une nouvelle fonction qui détermine si la valeur en paramètre est manquante:
def num_missing(x):
    return sum(x.isnull())

print(df.apply(num_missing, axis=0))