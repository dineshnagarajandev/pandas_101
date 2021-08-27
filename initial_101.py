import pandas as pd

# DataFrame Data Structure in pandas
df = pd.DataFrame(
    {
        "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
            ],
            "Age": [22, 35, 58],
            "Sex": ["male", "male", "female"],
    }
)

print("****** df ******")
print(df)
print("****** Age column in df ******")
print(df["Age"])

# Series Data Structure in pandas
ages = pd.Series([22, 35, 58, 60], name="Age")
print("****** Age Series ******")
print(ages)
print("****** Max of Age in Series ******")
max_of_ages = ages.max()
print(max_of_ages)

# Get max value from a df
max_of_age = df["Age"].max()
print("****** Max of Age in df ******")
print(max_of_age)

# some basic statistics of numerical data
# describe() - provide quick overview of the numeric data in a DataFrame
# Text data from the df will not be consisered by this method
basic_stat = df.describe()
print("****** Basic statistics of df ******")
print(basic_stat)

# REMEMBER
# Import the package, aka import pandas as pd
# A table of data is stored as a pandas DataFrame
# Each column in a DataFrame is a Series
# You can do things by applying a method to a DataFrame or Series