import pandas as pd
import numpy as np

csv_file = pd.read_csv("Real_es.csv")
print(type(csv_file))
csv_file.columns # field names

df_flats = pd.DataFrame(csv_file) # csv to df

df_flats['Price'] = df_flats['Price'].str.replace('$','').str.replace(',','').astype(float) # string to float

# 2 new columns
modified_data = df_flats.assign(square_meter=lambda x: x['Area (ft.)'] * 0.09290304, \
    meter_price=lambda x: df_flats['Price'] / x['square_meter'])

df_new = modified_data[['square_meter', 'meter_price', 'State']]
filter = ""
#print(df_new)
#print(type(df_new))

californian_flat = df_new[df_new['State'].isin(['California'])]
#californian_flat.reset_index(inplace=True)
#print(californian_flat)

pd.DataFrame.sum(californian_flat['square_meter'])


covariance = np.cov(californian_flat['meter_price'],californian_flat['square_meter'])
print(covariance[1][0])


