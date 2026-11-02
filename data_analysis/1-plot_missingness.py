#!/usr/bin/env python3
"""Module for visualizing missing values in a pandas DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """
    Plot missing values of a DataFrame as vertical bars.

    Each row of the plot is a column of the DataFrame and each bar marks
    a record (row index) where that column has a missing value.

    Args:
        df: pandas DataFrame to analyze

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    for i, col in enumerate(df.columns):
        # Positions of the records where this column is missing
        x = np.where(df[col].isnull())[0]
        # One vertical bar per missing value, default color (C0)
        plt.scatter(x, [i] * len(x), marker='|', color='C0')

    # Map y-ticks to the DataFrame column names
    plt.yticks(range(len(df.columns)), df.columns)
    plt.title('Missingness Plot')

    plt.tight_layout()
    plt.show()
