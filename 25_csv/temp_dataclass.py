"""
testing use of dataclass
"""
import csv
from dataclasses import dataclass

@dataclass
class  DayTemperature:
    day: str
    temp: int
    condition: str

    def __post_init__(self):
        self.day = self.day.strip()
 


with open("weather_data.csv", 'r') as data_file:
    data = data_file.readlines()

week_temps = list()
for entry in data[1:]:
    ls = entry.split(',')
    ls = list(map(lambda x: int(x) if str.isnumeric(x) else x.strip(), ls))
    week_temps.append(DayTemperature(*ls))