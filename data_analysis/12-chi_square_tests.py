#!/usr/bin/env python3
"""Module for chi-square independence tests against the Churn target."""
import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """
    Test the independence of each categorical feature and Churn.

    Args:
        df: pandas DataFrame with Churn and categorical columns

    Returns:
        A dictionary {feature_name: p_value}
    """
    p_values = {}
    # Categorical features are the object columns, excluding the target
    for col in df.select_dtypes(include='object').columns:
        if col == 'Churn':
            continue
        # Contingency table of observed counts: feature categories x Churn
        table = pd.crosstab(df[col], df['Churn'])
        # chi2_contingency returns (chi2, p, dof, expected_freq)
        p_values[col] = stats.chi2_contingency(table)[1]
    return p_values
