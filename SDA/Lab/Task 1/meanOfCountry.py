import csv

file_path = './gapminder.csv'
country_name = 'Albania'

# Initialize variables to calculate the mean
total = 0
count = 0

# Open the CSV file and read it
with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through each row and sum the values of the 'lifeExp' column for the specified country
    for row in reader:
        if row['country'] == country_name:
            total += float(row['lifeExp'])  # Convert the value to float
            count += 1

# Calculate the mean if there are matching rows
if count > 0:
    mean_life_exp = total / count
    print(f"Mean of lifeExp for {country_name}: {mean_life_exp}")
else:
    print(f"No data found for the country: {country_name}")
