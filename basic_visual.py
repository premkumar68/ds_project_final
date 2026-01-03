import matplotlib.pyplot as plt

def plot_hist(df):
    df.hist(figsize=(8,6))
    plt.show()
