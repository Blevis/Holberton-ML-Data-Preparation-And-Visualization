#!/usr/bin/env python3
"""Module for visualizing correlations between numeric features."""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """
    Plot an annotated correlation heatmap of the numeric features.

    Args:
        df: pandas DataFrame

    Returns:
        None
    """
    plt.figure(figsize=(6, 5))

    # Pairwise correlations between the numeric columns only
    corr = df.corr(numeric_only=True)
    # Annotated heatmap with the color scale fixed to the full range
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix')

    plt.show()
