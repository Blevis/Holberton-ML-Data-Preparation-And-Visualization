#!/usr/bin/env python3
"""Module for visualizing the Churn class distribution."""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """
    Plot the distribution of the Churn column as a bar plot.

    Args:
        df: pandas DataFrame with a Churn column

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    # Number of customers per class ('No' first, being the majority)
    counts = df['Churn'].value_counts()
    # skyblue for 'No', salmon for 'Yes', matched by label, not position
    colors = ['skyblue' if label == 'No' else 'salmon'
              for label in counts.index]

    plt.bar(counts.index, counts.values, color=colors)
    plt.title('Churn Distribution')
    plt.ylabel('Count')

    plt.show()
