#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:05:03 2020

@author: kellenbullock
"""

import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_excel('Final.xlsx')
df = df.drop(columns='Unnamed: 0')

dependent = df['median_house_value']
independent = df.drop(columns=['median_house_value'])

mod = sm.OLS(dependent, independent)
res = mod.fit()
res_sum = res.summary()

vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(independent.values, i) for i in range(independent.shape[1])]
vif["features"] = independent.columns