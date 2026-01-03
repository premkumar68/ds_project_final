from data_loader import load_data
from data_export import export_data
from data_cleaning import clean_data
from data_transform import transform_data
from descriptive_stats import descriptive_statistics
from basic_visual import plot_hist
from advanced_visual import corr_heatmap
from interactive_visual import interactive_plot
from probability_analysis import probability_dist
from kmeans_cluster import run_kmeans

# Load dataset
df = load_data("student_data.csv")

# Clean data
df = clean_data(df)

# Select numeric columns
num_cols = df.select_dtypes(include=["float64","int64"]).columns

# Transform numeric data
df = transform_data(df, num_cols)

# Statistics + visualizations
descriptive_statistics(df)
plot_hist(df)
corr_heatmap(df)
interactive_plot(df, num_cols[0], num_cols[1])
probability_dist(df, num_cols[0])



# ---- K-Means Clustering ----
df = run_kmeans(df, ["G1", "G2", "G3"])

# Export output file
export_data(df)
