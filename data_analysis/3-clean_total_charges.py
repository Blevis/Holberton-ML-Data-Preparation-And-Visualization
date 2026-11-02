#!/usr/bin/env python3
"""Module for handling missing values in the TotalCharges column."""
import pandas as pd


def clean_total_charges(df, method='drop'):
    """
    Handle missing values in the TotalCharges column.

    Args:
        df: pandas DataFrame with missing values in TotalCharges
        method: strategy to handle missing values
            'drop': remove rows with missing TotalCharges
            'median': fill with the column median
            'impute': replace with MonthlyCharges * tenure

    Returns:
        The modified DataFrame (a copy, the original is left untouched)
    """
    # Work on a copy so repeated calls on the same df don't interfere
    df = df.copy()

    if method == 'drop':
        # Remove rows where TotalCharges is missing
        df = df.dropna(subset=['TotalCharges'])
    elif method == 'median':
        # Fill missing values with the median of the column
        median = df['TotalCharges'].median()
        df['TotalCharges'] = df['TotalCharges'].fillna(median)
    elif method == 'impute':
        # Estimate total charges as monthly charges times months of tenure
        estimate = df['MonthlyCharges'] * df['tenure']
        df['TotalCharges'] = df['TotalCharges'].fillna(estimate)

    return df
