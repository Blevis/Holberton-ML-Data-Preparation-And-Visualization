#!/usr/bin/env python3
"""Module for comparing a numeric feature's distribution by churn."""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """
    Plot histograms of a numeric column for each Churn class.

    Args:
        df: pandas DataFrame with a Churn column
        col: numeric column name

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    # Values of the feature for each churn class, 'No' first
    no = df.loc[df['Churn'] == 'No', col]
    yes = df.loc[df['Churn'] == 'Yes', col]

    # Passing both arrays at once gives shared bins (30) and side-by-side bars
    plt.hist([no, yes], bins=30, label=['No', 'Yes'])
    plt.title(f'{col} Distribution by Churn')
    plt.xlabel(col)
    plt.legend(title='Churn')

    plt.show()
