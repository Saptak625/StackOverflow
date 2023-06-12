# Transpose a pandas dataframe
import pandas as pd

# Create a dataframe
df = pd.DataFrame({'train': [0.6125, 0.8565, 0.7596, 0.0466, 0.9897, 0.9884], 'val': [0.0827, 0.9845, 0.982, 0.0454, 0.9949, 0.9949], 'score': ['loss', 'precision', 'recall']*2})

# Find list of unique values in the score column
new_cols = {f'{i}_{j}': [] for i in ['train', 'val'] for j in df.score.unique()}

# Iterate over the dataframe and append values to the new_cols dictionary
for _, row in df.iterrows():
    new_cols[f'train_{row["score"]}'].append(row[0])
    new_cols[f'val_{row["score"]}'].append(row[1])

# Create a new dataframe from the new_cols dictionary
new_df = pd.DataFrame(new_cols)
print(new_df)