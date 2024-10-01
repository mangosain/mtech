import pandas as pd

# Read the data from the file gapminder.csv
data = pd.read_csv("/Users/manav/Documents/mtech/SDA/Lab/Task 1/gapminder.csv")

# Verify that the data has been loaded correctly
print(data.head())

# Replace missing values in 'lifeExp' with 0
data["lifeExp"].fillna(0, inplace=True)

# Calculate the mean of lifeExp from all the data
mean_all = data["lifeExp"].mean()
print("Mean of lifeExp from all the data:", mean_all)

# Calculate the mean of lifeExp by country
mean_country = data.groupby("country")["lifeExp"].mean()
print("\nMean of lifeExp by country:")
print(mean_country)

# Calculate the mean of lifeExp by year
mean_year = data.groupby("year")["lifeExp"].mean()
print("\nMean of lifeExp by year:")
print(mean_year)

# Calculate the mean of lifeExp by continent
mean_continent = data.groupby("continent")["lifeExp"].mean()
print("\nMean of lifeExp by continent:")
print(mean_continent)
