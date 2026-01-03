from sklearn.preprocessing import StandardScaler

def transform_data(df, num_cols):
    scaler = StandardScaler()
    
    print("\nBefore Transformation (first 5 rows):")
    print(df[num_cols].head())

    df[num_cols] = scaler.fit_transform(df[num_cols])

    print("\nAfter Transformation (first 5 rows):")
    print(df[num_cols].head())

    print("\nData Transformation Done ✔")
    return df
