# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:41:47 2019

@author: HP-PC
"""

'''
Ce code permet de créer un nouveau fichier CSV et d'ajouter la colonne "City" pour les
differents aéroports.

De plus la variable "listOfCity" contient la liste des differentes villes. Il faudra 
l'utiliser pour télécharger les dataset concernant la météo.

Pour générer le fichier "2008_1.csv" il faudra exécuter le 
fichier python: "essaie.py"

Pour générer le fichier "2008_1_modified.csv" il faudra exécuter le 
fichier python: "Generate_CSV_2008_1_modified.py"

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_slice=pd.read_csv('2008_1.csv')
df_slice_modified=pd.read_csv('2008_1_modified.csv')

dep=df_slice['Origin']
a=dep.value_counts()

listAirports=[]
for i in range(len(a.index.values)): 
    listAirports.append(a.index.values[i])

airportCsv=pd.read_csv('airports.csv')

dataAirportAndCity=airportCsv[['iata','city']].copy()

dataAirportAndCity.columns=['Origin','City']#Renommer les colonnes pour pouvoir faire la fusion

#Fusion et Ajout de la colonne city au dataset
df_slice_modified_add_city=pd.merge(df_slice_modified,dataAirportAndCity)

#Création et Sauvegarde du dataset dans un fichier
df_slice_modified_add_city.to_csv('2008_1_modified_add_city.csv',index = False)

#La liste des villes (concernant les dataset à téléchager)
listOfCity=[]
b=df_slice_modified_add_city['City'].value_counts()
for i in range(len(b.index.values)): 
    listOfCity.append(b.index.values[i])
