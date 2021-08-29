# How do I read and write tabular data
import pandas as pd

# Read data from a CSV file
print("****** Read data from a CSV file ******")
titanic = pd.read_csv("data/titanic.csv")
print("****** Show first 5 and last 5 rows from the data frame ******")
print(titanic) # Show first 5 and last 5 rows from the data frame

# To get first 8 rows of data frame
first_eight_data = titanic.head(8)
print("****** To get first 8 rows of data frame ******")
print(first_eight_data)

# To get data type of each columns
df_dataType = titanic.dtypes
print("****** To get data type of each columns ******")
print(df_dataType)

# Convert CSV to EXCEL
print("****** Convert CSV to EXCEL ******")
titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False)

print(titanic.head())

# Technical summary of DataFrame
print("****** Technical summary of DataFrame ******")
print(titanic.info())