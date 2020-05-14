# ---
# jupyter:
#   jupytext:
#     formats: notebooks//ipynb,rmd//Rmd,scripts//py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
import os.path

numbers = pd.read_excel('sensitive/mossley-hill-numbers.xlsx',sheet_name=None)

for key in numbers:
    print(key)
    print(numbers[key])
    print('\n')

ages = pd.read_excel(os.path.join('sensitive','mossley-hill-numbers.xlsx'), sheet_name='Regulars', index_col=1)

ages[:-1].plot.bar()

cofe = pd.read_excel('sensitive/2018StatisticsForMission_tables.xlsx',sheet_name=None)

for key in cofe:
    print(key)
    print(cofe[key])
    print('\n')
