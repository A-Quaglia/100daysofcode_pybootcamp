#%%
import csv

import pandas as pd

#%%
# challenge read file with readlines

with open("weather_data.csv", 'r') as data_file:
    data = data_file.readlines()

weather_data = list()
for entry in data:
    entry = entry.replace('\n', '')
    ls = entry.split(',')
    ls = list(map(lambda x: int(x) if str.isnumeric(x) else x.strip(), ls))
    weather_data.append(ls)

print(weather_data)
# %%
with open("weather_data.csv", 'r') as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)


#%%
# Challenge - get list of temp
temperature_index = weather_data[0].index('temp')

temperatures = list()
for entry in weather_data[1:]:
    temperatures.append(entry[temperature_index])

print(temperatures)
# %%
#using pandas

data = pd.read_csv('weather_data.csv')
print(data['temp'])
# %%
