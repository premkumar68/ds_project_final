import plotly.express as px

def interactive_plot(df, x, y):
    fig = px.scatter(df, x=x, y=y)
    fig.show()
