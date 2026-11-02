#!/usr/bin/env python3
"""Encode features for modeling."""

import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Encode categorical features using sklearn preprocessing."""

    df = df.copy()

    # Encode Churn using LabelEncoder
    churn_le = preprocessing.LabelEncoder()
    df['Churn'] = churn_le.fit_transform(df['Churn'])

    # Encode binary columns using OrdinalEncoder
    binary_cols = [
        'Partner',
        'Dependents',
        'PaperlessBilling',
        'SeniorCitizen'
    ]

    binary_oe = preprocessing.OrdinalEncoder(
        categories=[['No', 'Yes']]
    )

    df[binary_cols] = binary_oe.fit_transform(df[binary_cols]).astype(int)

    # One-hot encode Contract and PaymentMethod
    df = pd.get_dummies(
        df,
        columns=['Contract', 'PaymentMethod'],
        drop_first=True,
        dtype=int
    )

    # Encode TenureGroup alphabetically
    tenure_oe = preprocessing.OrdinalEncoder()

    df[['TenureGroup']] = tenure_oe.fit_transform(
        df[['TenureGroup']]
    ).astype(int)

    return df, churn_le, binary_oe, tenure_oe
