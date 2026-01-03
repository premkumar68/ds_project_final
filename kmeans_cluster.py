from sklearn.cluster import KMeans

def run_kmeans(df, cols):
    kmeans = KMeans(n_clusters=3, random_state=42)
    df["Cluster"] = kmeans.fit_predict(df[cols])

    print("\nClustering Completed ")

    print("\nCluster Count:")
    print(df["Cluster"].value_counts())

    print("\nSample Records from Each Cluster:")
    print(df.groupby("Cluster").head(3))

    return df
