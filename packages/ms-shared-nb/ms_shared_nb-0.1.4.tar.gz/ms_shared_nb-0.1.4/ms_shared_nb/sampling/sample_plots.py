import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def plot_kde(samples):
    fig = go.Figure()
    for sample in samples:
        fig.add_trace(go.Histogram(x=sample['close'], name=sample['name'], histnorm='probability density'))
    fig.update_layout(
        title_text='KDE Plot',
        xaxis_title_text='Close',
        yaxis_title_text='Probability Density',
        bargap=0.2,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )
    return fig

    
# sample plot types: kde, markers, line, bar
def plot_samples(samples, plot_type):
    pass

