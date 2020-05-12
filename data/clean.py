import pandas as pd
import numpy as np

churches = ['mossleyhill','gateway','sthelens','stoneycroftsalvationarmy']

csv = {}
for church in churches:
    csv[church] = pd.read_csv(f'sensitive/postcodes/{church}.csv')
    csv[church]['Postcode'] = csv[church]['Postcode'].str.upper()
    csv[church]['Postcode'] = csv[church]['Postcode'].str.replace(' ','')
    csv[church]['Postcode'] = csv[church]['Postcode'].str[:-3] + ' ' + csv[church]['Postcode'].str[-3:]
    csv[church].to_csv(f'{church}.csv', index=False)
