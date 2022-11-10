# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 21:56:06 2022

@author: USER
"""
import pandas as pd
import matplotlib.pyplot as plt

df_covid = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-table-data.csv')

df_covid = df_covid.rename_axis('country').reset_index()