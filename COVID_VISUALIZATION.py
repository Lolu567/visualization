# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 21:56:06 2022

@author: USER
"""
import pandas as pd
import matplotlib.pyplot as plt
#reading in a csv data file
df_covid = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-table-data.csv')
#Adding an index to the data 
df_covid = df_covid.rename_axis('country').reset_index()
#Renaming the dataset columns
df_covid = df_covid.rename(columns={'Name':'Who_Region', 'WHO Region':'Cases_cumulative_total',
                                   'Cases - cumulative total':'Cases_cumulative_total_per_100000_population',
                                   'Cases - cumulative total per 100000 population':'Cases_newly_reported_in_last_7_days',
                                   'Cases - newly reported in last 7 days':'Cases_newly_reported_in_last_7_days_per_100000_population',
                                   'Cases - newly reported in last 7 days per 100000 population':'Cases_newly_reported_in_last_24_hours',
                                   'Cases - newly reported in last 24 hours':'Deaths_cumulative_total',
                                   'Deaths - cumulative total':'Deaths_cumulative_total_per_100000_population',
                                   'Deaths - cumulative total per 100000 population':'Deaths_newly_reported_in_last_7_days',
                                   'Deaths - newly reported in last 7 days':'Deaths_newly_reported_in_last_7_days_per_100000_population',
                                   'Deaths - newly reported in last 7 days per 100000 population':'Deaths_newly_reported_in_last_24_hours'})
#droppping a column tht is not necessary
df_covid.pop('Deaths - newly reported in last 24 hours')
df_covid
#doing a groupby to get distinct dataset
new=df_covid.groupby(df_covid['Who_Region']).sum()

new = new.rename_axis('Who_Region').reset_index()
new

df_new=df_covid.groupby(df_covid['Who_Region'])[['Cases_cumulative_total', 'Deaths_cumulative_total']].sum()
df_new['Cases_cumulative_total / 1m'] = df_new['Cases_cumulative_total']/10
df_new = df_new.rename_axis('Who_Region').reset_index()
#calling a function that print lineplot alone
def line_plot(x_axis,y_axis,xticks,label,title):
    """This function generates a lineplot by accepting five args"""
    plt.figure(figsize=(7,6))
    for i in range(len(y_axis)):
        plt.plot(x_axis,y_axis[i],label=label[i])
    plt.legend()
    plt.xticks(x_axis,xticks,rotation='vertical')
    plt.title(title)
    plt.show()
    
x_axis = df_new['Who_Region']
y_axis = [df_new['Cases_cumulative_total / 1m'],df_new['Deaths_cumulative_total']]

xticks = ["Africa", "Americas", "Eastern Mediterranean", "Europe", "Other", "South-East Asia", "Western Pacific"]
label = ['cases','deaths']
title =['Cases and Deaths by Region']
    

line_plot(x_axis, y_axis, xticks, label, title)

def pie_chart(data,mylabels,explode):
    """This function plots a pie_chart using three args"""
    plt.figure()
    plt.pie(data, labels=mylabels, explode=explode, startangle = 180,autopct='%1.2f%%')
    plt.title('Cumulative by Region')
    plt.xlabel('Who_Region')
    plt.ylabel('counts')
    plt.show()
data= df_new['Cases_cumulative_total']
mylabels = ["Africa", "Americas", "Eastern Mediterranean", "Europe", "Other", "South-East Asia", "Western Pacific"]
explode = [0.2, 0, 0, 0, 0, 0, 0]
pie_chart(data,mylabels,explode)

df_groupped = df_covid.groupby(['Who_Region'])['Cases_cumulative_total_per_100000_population'].sum()
df_groupped = df_groupped.reset_index()

plt.figure()
plt.bar(df_groupped['Who_Region'], df_groupped['Cases_cumulative_total_per_100000_population'])
plt.xlabel('who_region')
plt.ylabel('cumulative per 1000000')
plt.title('Cases per 100,000 population')
plt.xticks(rotation='vertical')
plt.show()

