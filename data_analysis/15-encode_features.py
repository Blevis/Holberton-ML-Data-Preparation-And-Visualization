#!/usr/bin/env python3

import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Encode features for modeling."""

    df = df.copy()

    # Label encode Churn
    churn_le = preprocessing.LabelEncoder()
    df['Churn'] = churn_le.fit_transform(df['Churn'])

    # Ordinal encode binary columns
    binary_cols = [
        'Partner',
        'Dependents',
        'PaperlessBilling',
        'SeniorCitizen'
    ]

    binary_oe = preprocessing.OrdinalEncoder(
        categories=[['No', 'Yes']]
    )

    df[binary_cols] = binary_oe.fit_transform(
        df[binary_cols]
    ).astype(int)

    # One-hot encode Contract and PaymentMethod
    df = pd.get_dummies(
        df,
        columns=['Contract', 'PaymentMethod'],
        drop_first=True
    )

    dummy_cols = df.select_dtypes(include=['bool']).columns
    df[dummy_cols] = df[dummy_cols].astype(int)

    # Ordinal encode TenureGroup
    tenure_oe = preprocessing.OrdinalEncoder()

    df[['TenureGroup']] = tenure_oe.fit_transform(
        df[['TenureGroup']]
    ).astype(int)

    return df, churn_le, binary_oe, tenure_oe
