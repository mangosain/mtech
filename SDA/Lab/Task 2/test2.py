# write code to take input for a data frame and print it
import pandas as pd
import matplotlib.pyplot as plt

# Function to take inputs for a DataFrame
def create_dataframe():
    columns = input("Enter column names separated by commas: ").split(',')
    num_rows = int(input("Enter the number of rows: "))
    
    data = {}
    for col in columns:
        data[col] = []
        for i in range(num_rows):
            value = float(input(f"Enter value for {col} row {i+1}: "))
            data[col].append(value)
    
    return pd.DataFrame(data)

# Function to plot a boxplot
def plot_boxplot(df):
    plt.figure(figsize=(10, 6))
    df.boxplot()
    plt.title('Boxplot of DataFrame')
    plt.show()

# Main function
if __name__ == "__main__":
    df = create_dataframe()
    print("\nDataFrame:\n", df)
    plot_boxplot(df)
