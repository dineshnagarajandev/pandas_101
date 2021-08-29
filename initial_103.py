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

# Filter specific rows from a DataFrame
print("****** Age > 35 from DF ******")
above_35 = titanic[titanic["Age"] > 35]
print(above_35)

# Filter passanger with cabin calss 2 and class 3
print("****** isin usage list of passangers in class 2 and 3 from DF ******")
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
print(class_23);

# Filter non null value from age
print("****** Filter non null value from age DF (notna()) ******")
age_no_ana = titanic[titanic["Age"].notna()]
print(age_no_ana)

# Select specific rows and columns from a DataFrame
print("****** Select specific rows and columns from a DataFrame ******")
adult_name = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_name)

# Filter with specific row and columns
print("***** Specific rows and columns ******")
print(titanic.iloc[9:25, 2:5])

# loc is used to locate with name
# iloc is used to identify with integer

# Set value for DataFrame
# Generally update first 3 rows 3rd column value to anonymous
titanic.iloc[0:3, 3] = "anonymous"
print(titanic.head())