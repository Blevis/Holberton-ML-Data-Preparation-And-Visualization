#!/usr/bin/env python3
"""Module for encoding features using Scikit-learn."""

import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Encode categorical features for modeling."""

    df = df.copy()

    # 1. Label encode Churn
    churn_le = preprocessing.LabelEncoder()
    df['Churn'] = churn_le.fit_transform(df['Churn'])

    # 2. Ordinal encode binary columns
    binary_cols = [
        'Partner',
        'Dependents',
        'PaperlessBilling',
        'SeniorCitizen'
    ]

    binary_oe = preprocessing.OrdinalEncoder(
        categories=[['No', 'Yes']]
    )

    # Fit on the first binary column
    binary_oe.fit(df[['Partner']].to_numpy())

    # Transform all binary columns
    for col in binary_cols:
        df[[col]] = binary_oe.transform(
            df[[col]].to_numpy()
        ).astype(int)

    # 3. One-hot encode Contract and PaymentMethod
    df = pd.get_dummies(
        df,
        columns=['Contract', 'PaymentMethod'],
        drop_first=True,
        dtype=int
    )

    # 4. Ordinal encode TenureGroup
    tenure_oe = preprocessing.OrdinalEncoder()

    df[['TenureGroup']] = tenure_oe.fit_transform(
        df[['TenureGroup']]
    ).astype(int)

    return df, churn_le, binary_oe, tenure_oe
