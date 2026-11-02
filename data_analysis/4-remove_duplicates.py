#!/usr/bin/env python3
"""Module for removing duplicate rows from a DataFrame."""


def remove_duplicates(df):
    """
    Remove duplicate rows from a DataFrame.

    Args:
        df: pandas DataFrame to process

    Returns:
        The deduplicated DataFrame
    """
    # Keep the first occurrence of each row and drop the repeats
    return df.drop_duplicates()
