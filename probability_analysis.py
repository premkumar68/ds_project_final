import seaborn as sns
import matplotlib.pyplot as plt

def probability_dist(df, col):
    sns.kdeplot(df[col], shade=True)
    plt.show()
