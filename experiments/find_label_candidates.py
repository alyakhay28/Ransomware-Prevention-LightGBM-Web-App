import pandas as pd

df = pd.read_csv('data_file.csv')

for col in df.columns:
    nunique = df[col].nunique()
    if nunique <= 10:
        print(col, df[col].value_counts(), '\n')
