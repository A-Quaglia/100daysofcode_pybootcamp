#%% Challenge 1 count Squirrels by fur color & generate a csv with the values
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data.groupby(by='Primary Fur Color')['Primary Fur Color'].count().to_csv("squirrels_count.csv")
# %%
