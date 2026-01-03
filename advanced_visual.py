import seaborn as sns
import matplotlib.pyplot as plt

def corr_heatmap(df):
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.show()
