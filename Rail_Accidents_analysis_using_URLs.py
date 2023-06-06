# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 00:03:30 2023

@author: Manoj Kaushik
"""

import time
import pandas as pd
import matplotlib.pyplot as plt

df_list = pd.read_html("https://en.wikipedia.org/wiki/List_of_accidents_and_disasters_by_death_toll")
df_rail_acci = df_list[12]
df_rail_acci['Continent'] = df_rail_acci['Location']
type(df_rail_acci['Location'][0])
df_rail_acci[['Continent','Country']] = df_rail_acci['Location'].str.split(',', expand=True)
df_rail_acci['Continent'] = df_rail_acci['Location'].str.slice(stop=2)
df_rail_acci.columns

