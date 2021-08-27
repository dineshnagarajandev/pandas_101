# How to select a subset of a DataFrame
from typing import AsyncGenerator
import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

print(titanic.head())
# Get single coloums in the DF
ages = titanic["Age"]
# Get multiple coloums in the DF
ages_sex = titanic[["Age", "Sex"]]

print("****** single coloums in the DF ******")
print(ages.head())
print("****** multiple coloums in the DF ******")
print(ages_sex.head())
# Give number of rows and coloumns
print("****** number of rows and coloumns ******")
print(ages_sex.shape)