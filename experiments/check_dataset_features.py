import pandas as pd

# Load training CSV
train_df = pd.read_csv("sampled_2000.csv")

# Print the first 5 rows
print(train_df.head())

# Print min/max for numeric columns
print("\nFeature ranges:")
print(train_df.describe().T[['min', 'max']])
