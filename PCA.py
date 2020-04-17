#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:32:05 2020

@author: kellenbullock
"""
import pandas as pd
from statsmodels.multivariate.pca import PCA

df = pd.read_excel('Final.xlsx')
df = df.drop(columns=['Unnamed: 0'])

c = PCA(df, standardize=False)