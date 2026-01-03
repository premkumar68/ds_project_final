import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("Dataset Loaded Successfully")
    print(df.head())
    return df
