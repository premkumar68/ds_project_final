def descriptive_statistics(df):
    print(df.describe())
    print(df.mean(numeric_only=True))
