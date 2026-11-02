#!/usr/bin/env python3
"""Module for visualizing churn rate per category of a feature."""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """
    Plot the churn rate (proportion of 'Yes') for each category of a column.

    Args:
        df: pandas DataFrame with a Churn column
        col: categorical column name

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    # Mean of the boolean (Churn == 'Yes') per category is the churn rate;
    # groupby sorts the categories alphabetically, as in the reference
    rate = (df['Churn'] == 'Yes').groupby(df[col]).mean()

    plt.bar(rate.index, rate.values)
    plt.title(f'Churn Rate by {col}')
    plt.ylabel('Churn Rate')
    # Rotate the x-axis labels by 45 degrees
    plt.xticks(rotation=45)

    plt.show()
