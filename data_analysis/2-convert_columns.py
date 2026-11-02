#!/usr/bin/env python3
"""Module for converting column types of the Telco churn DataFrame."""
import pandas as pd


def convert_columns(df):
    """
    Convert TotalCharges to numeric and SeniorCitizen to categorical strings.

    Args:
        df: pandas DataFrame containing the columns TotalCharges and
            SeniorCitizen

    Returns:
        The modified DataFrame
    """
    # Non-numeric entries (e.g. ' ') become NaN instead of raising an error
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    # Map the numeric flags 0/1 to the categories "No"/"Yes"
    df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
    return df
