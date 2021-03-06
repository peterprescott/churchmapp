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
import numpy as np

churches = ['mossleyhill','gateway','sthelens','stoneycroftsalvationarmy']

csv = {}
for church in churches:
    csv[church] = pd.read_csv(f'../data/sensitive/postcodes/{church}.csv')
    csv[church]['Postcode'] = csv[church]['Postcode'].str.upper()
    csv[church]['Postcode'] = csv[church]['Postcode'].str.replace(' ','')
    csv[church]['Postcode'] = csv[church]['Postcode'].str[:-3] + ' ' + csv[church]['Postcode'].str[-3:]
    csv[church].to_csv(f'../data/sensitive/derived/{church}.csv', index=False)
