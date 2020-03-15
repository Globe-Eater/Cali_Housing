#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 11:04:29 2020

@author: kellenbullock
"""

import pandas as pd
import sys
sys.path.append('/Users/kellenbullock/Desktop/Geographic Analysis II/Ex1')
sys.path.append('/Users/kellenbullock/Desktop/Geographic Analysis II/Ex3')
import EDA
import Correlations

def ocean_to_num(series):
    '''This mothod will convert ocean proxminity into a numerical category
    so that it can be used in calculations as opposed to strings.'''
    if series == 'NEAR BAY':
        return 1
    elif series == '<1H OCEAN':
        return 2
    elif series == 'INLAND':
        return 3
    elif series == 'NEAR OCEAN':
        return 4
    elif series == 'ISLAND':
        return 5
    else:
        return 0

# Univariate
df = pd.read_excel('/Users/kellenbullock/Desktop/Cali_housing/Bullock_BM2.xlsx')

df = df.loc[df['median_house_value'] < 500000]
df = df.loc[df['housing_median_age'] < 52]

df['ocean_proximity'] = df['ocean_proximity'].apply(ocean_to_num)
df = df.drop(columns=['Unnamed: 0'])
df = df.dropna()

df.to_excel('FINAL.xlsx')

EDA.Descrptives(df, df)
EDA.figures(df, '')

# Bivar
Correlations.corr_w_sig(df, df['median_house_value'])
x = ['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','ocean_proximity']
y = 'median_house_value'
Correlations.corr_scatter(df, x, y)
EDA.merge_pdfs()
# corr.style.background_gradient(cmap='coolwarm')
# df.corr(method='spearman')
# corr.style.background_gradient(cmap='coolwarm')