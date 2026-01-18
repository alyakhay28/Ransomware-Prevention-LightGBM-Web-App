import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('data_file.csv')
df_small, _ = train_test_split(df, train_size=2000, stratify=df['Benign'], random_state=42)
df_small.to_csv('sampled_2000.csv', index=False)

print("Sample created:", df_small.shape)
print(df_small['Benign'].value_counts())
