import csv

# Define the path to your CSV file
file_path = './gapminder.csv'

# Initialize variables to calculate the mean
total = 0
count = 0

# Open the CSV file and read it
with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through each row and sum the values of the 'lifeExp' column
    for row in reader:
        total += float(row['lifeExp'])  # Convert the value to float
        count += 1

# Calculate the mean
mean_life_exp = total / count

# Print the result
print(f"Mean of lifeExp: {mean_life_exp}")