# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 15:24:14 2018

@author: Light
"""

import pandas as pd
import os
import shutil

new_df = {}

os.chdir("E:/Derma/")
x = pd.read_csv('HAM10000_metadata.csv')
df = pd.DataFrame(x)
for i in pd.unique(df.dx):
    os.mkdir(i)
for i in pd.unique(df.dx):
    new_df[i] = df[(df['dx']== i)]

for i in new_df:
    for j in new_df[i]['image_id']:
        try:
            shutil.move(('HAM10000_images/'+ j +'.jpg'), i)
        except:
            continue