import pandas as pd

df = pd.read_csv('data_file.csv')
print('Shape:', df.shape)
print('\nColumns:\n', df.columns.tolist())
print('\nFirst 5 rows:\n', df.head())

