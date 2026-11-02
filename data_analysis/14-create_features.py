#!/usr/bin/env python3
"""Module for engineering new features from the Telco churn dataset."""
import pandas as pd


def create_features(df):
    """
    Create the NumServices and TenureGroup features.

    Args:
        df: pandas DataFrame

    Returns:
        The modified DataFrame, without the columns used to build the features
    """
    df = df.copy()

    # Service columns where 'Yes' means the customer subscribes
    yes_cols = ['MultipleLines', 'OnlineSecurity', 'OnlineBackup',
                'DeviceProtection', 'TechSupport', 'StreamingTV',
                'StreamingMovies']

    # Each 'Yes' counts as one service
    num_services = (df[yes_cols] == 'Yes').sum(axis=1)
    # InternetService: 'DSL' and 'Fiber optic' count as subscribed, 'No' not
    num_services += (df['InternetService'] != 'No').astype(int)
    df['NumServices'] = num_services

    # Bins right-inclusive: (0, 12], (12, 24], (24, 48], (48, 60], (60, inf)
    df['TenureGroup'] = pd.cut(df['tenure'],
                               bins=[0, 12, 24, 48, 60, float('inf')],
                               labels=['0-12', '13-24', '25-48', '49-60',
                                       '60+'])

    # Drop the original columns used to create the new features
    return df.drop(columns=yes_cols + ['InternetService', 'tenure'])
