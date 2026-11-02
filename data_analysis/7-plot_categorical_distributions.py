#!/usr/bin/env python3
"""Module for visualizing categorical feature distributions."""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    Plot the distribution of categorical features as a grid of bar plots.

    Args:
        df: pandas DataFrame
        columns_to_plot: optional list of categorical columns. Defaults to
            all columns of dtype object, excluding the target Churn

    Returns:
        None
    """
    if columns_to_plot is None:
        # All object columns except the target variable
        columns = [col for col in df.columns
                   if df[col].dtype == 'object' and col != 'Churn']
    else:
        columns = columns_to_plot
    # 3 plots per row, enough rows to fit every column (ceiling division)
    n_cols, n_rows = 3, (len(columns) + 2) // 3
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
    # Flatten the 2D array of axes so it can be indexed with a single index
    axes = axes.flatten()

    for ax, col in zip(axes, columns):
        # Category counts, sorted from most to least frequent
        counts = df[col].value_counts()
        ax.bar(counts.index, counts.values)
        ax.set_title(col)
        # Rotate the x-axis labels by 45 degrees
        ax.tick_params(axis='x', rotation=45)

    # Hide the unused axes left over in the last row of the grid
    for ax in axes[len(columns):]:
        ax.set_visible(False)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
