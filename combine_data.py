# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:37:48 2019

@author: 郭倩毓
Description:使用Pandas拼接多个CSV文件到一个文件（即合并）
"""

import pandas as pd
import os
Folder_Path = r'C:\Users\HP-PC\Documents\AJourneyToADataScientist\Meteo_10_villes'       #Le chemin de dossier qui contient les fichiers des villes
SaveFile_Path =  r'C:\Users\HP-PC\Documents\AJourneyToADataScientist\Meteo_10_villes'       #Le chemin de dossier qui contient un fichier de 10 villes
SaveFile_Name = r'Is_10_villes.csv'              #le nom de ficher de 10 villes

#修改当前工作目录
os.chdir(Folder_Path)
#将该文件夹下的所有文件名存入一个列表
file_list = os.listdir()

#读取第一个CSV文件并包含表头
df = pd.read_csv(Folder_Path +'\\'+ file_list[0])   #编码默认UTF-8，若乱码自行更改

#将读取的第一个CSV文件写入合并后的文件保存
df.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False)

#循环遍历列表中各个CSV文件名，并追加到合并后的文件
for i in range(1,len(file_list)):
    df = pd.read_csv(Folder_Path + '\\'+ file_list[i])
    df.to_csv(SaveFile_Path+'\\'+ SaveFile_Name,encoding="utf_8_sig",index=False, header=False, mode='a+')

