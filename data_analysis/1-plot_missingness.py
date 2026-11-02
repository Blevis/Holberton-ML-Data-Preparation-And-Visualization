#!/usr/bin/env python3
"""
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """
    """
    plt.figure(figsize=(12, 8))

    for i, col in enumerate(df.columns):
        x = np.where(df[col].isnull())[0]
        plt.scatter(x, [i] * len(x), marker='|', color='C0')
    plt.yticks(range(len(df.columns)), df.columns)

    plt.tight_layout()
    plt.show()
