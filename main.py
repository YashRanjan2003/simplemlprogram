import pandas as pd

# Load and display dataset info
df = pd.read_csv('sample_data.csv')
print(df.describe())
print("\nFirst 5 rows:")
print(df.head())
