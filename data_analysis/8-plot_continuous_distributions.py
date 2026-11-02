#!/usr/bin/env python3
"""Module for visualizing continuous feature distributions."""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """
    Plot histogram + KDE and boxplot for continuous numerical features.

    Args:
        df: pandas DataFrame
        columns_to_plot: optional list of continuous numeric columns.
            Defaults to all numeric columns

    Returns:
        None
    """
    if columns_to_plot is None:
        # All numeric columns (SeniorCitizen is categorical after cleaning)
        columns_to_plot = df.select_dtypes(include=[np.number]).columns

    # One row of subplots per feature
    n_cols = len(columns_to_plot)
    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3*n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    for i, col in enumerate(columns_to_plot):
        data = df[col].dropna()

        # Left: density-normalized histogram
        axes[i, 0].hist(data, bins=30, density=True, alpha=0.7,
                        edgecolor='black')
        # Gaussian KDE evaluated over the range of the data
        kde = stats.gaussian_kde(data)
        x = np.linspace(data.min(), data.max(), 200)
        axes[i, 0].plot(x, kde(x), color='red', linestyle='--')
        axes[i, 0].set_title(f"{col} Histogram + KDE")

        # Right: horizontal boxplot
        axes[i, 1].boxplot(data, vert=False)
        axes[i, 1].set_title(f"{col} Boxplot")

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()
