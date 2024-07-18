
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('countries.csv')

us = data[data.country == 'United States']
china = data[data.country == 'China']

plt.plot(us.year, us.population/us.population.iloc[0] * 100)
plt.plot(china.year, china.population/ china.population.iloc[0] * 100)
plt.legend(['USA', 'China'])
plt.xlabel('Metai')
plt.ylabel('Populiacijos kilimas (pirmi metai = 100 proc.)')
plt.show()