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
        # y is the column's position where the value is missing, NaN
        # otherwise. NaN points are not drawn but still make the x-axis
        # span all rows, even when the DataFrame has no missing values
        y = np.where(df[col].isnull(), i, np.nan)
        # Vertical bar marker in matplotlib's default color
        plt.scatter(df.index, y, marker='|', color='C0')

    # Map y-ticks to the DataFrame column names
    plt.yticks(range(len(df.columns)), df.columns)

    plt.tight_layout()
    plt.show()
