# How to select a subset of a DataFrame
from typing import AsyncGenerator
import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

print(titanic.head())
# Get single columns in the DF
ages = titanic["Age"]
# Get multiple columns in the DF
ages_sex = titanic[["Age", "Sex"]]

# Single columns selection in DF
print("****** single columns in the DF ******")
print(ages.head())

# Multiple columns
print("****** multiple columns in the DF ******")
print(ages_sex.head())

# Give number of rows and columns
print("****** number of rows and columns ******")
print(ages_sex.shape)