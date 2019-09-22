import numpy as np
import pandas as pd
solar_production=pd.read_csv("Data/Solar_Panels_Production.csv")
temperature=pd.read_csv("Data/Temperature.csv")
print(temperature.columns)
temperature = temperature.loc[:, ~temperature.columns.str.contains('^Unnamed')]
#solar_production.drop(solar_production.columns[solar_production.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
solar_production['day_power']=solar_production['cum_power'].shift(-1) - solar_production['cum_power']


#drop any rows that have missing data
#df.dropna(how="any")

#join multiple data frames in pandas
#new_df=pd.merge(solar_production,temperature,on='date')

print(solar_production.head())
print(temperature.head())
