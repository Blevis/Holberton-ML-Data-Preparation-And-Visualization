#!/usr/bin/env python3
"""Module for Welch's t-tests of numeric features against Churn."""
from scipy import stats


def ttest_numeric(df):
    """
    Run Welch's t-test on each numeric feature, Churn=Yes vs Churn=No.

    Args:
        df: pandas DataFrame with a Churn column

    Returns:
        A dictionary {feature_name: p_value}
    """
    p_values = {}
    # Split the data once into the two churn groups
    yes = df[df['Churn'] == 'Yes']
    no = df[df['Churn'] == 'No']
    # Numeric columns only (SeniorCitizen is text in the pre-cleaned CSV)
    for col in df.select_dtypes(include='number').columns:
        # equal_var=False selects Welch's test (no equal-variance assumption)
        p_values[col] = stats.ttest_ind(yes[col], no[col],
                                        equal_var=False).pvalue
    return p_values
