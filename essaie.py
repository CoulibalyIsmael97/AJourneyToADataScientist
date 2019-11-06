# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:22:17 2019

@author: HP-PC
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('2008.csv')
df_slice=df[df['WeatherDelay']>=0]

df_slice.to_csv('2008_1.csv',index = False)