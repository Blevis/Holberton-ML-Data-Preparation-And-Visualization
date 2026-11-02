#!/usr/bin/env python3
"""Module for dropping the customerID column from a DataFrame."""


def drop_customerID(df):
    """
    Remove the customerID column from a DataFrame.

    Args:
        df: pandas DataFrame containing a customerID column

    Returns:
        The modified DataFrame
    """
    # Unique identifiers carry no predictive value, so drop the column
    return df.drop(columns=['customerID'])
