#!/usr/bin/env python3
"""Module for scaling numeric features."""

from sklearn import preprocessing


def scale_numeric(df):
    """Standardize MonthlyCharges and TotalCharges."""

    df = df.copy()

    scaler = preprocessing.StandardScaler()

    columns = ['MonthlyCharges', 'TotalCharges']

    df[columns] = scaler.fit_transform(df[columns])

    return df
