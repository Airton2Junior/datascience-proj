import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("Zomato-data-.csv")
print(dataframe.head())

def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())

dataframe.info()

sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
