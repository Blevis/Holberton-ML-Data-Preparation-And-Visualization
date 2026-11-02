
#!/usr/bin/env python3
"""Module for encoding features using Scikit-learn."""

import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Encode categorical features for machine learning."""

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

    df[binary_cols] = binary_oe.fit_transform(
        df[binary_cols]
    ).astype(int)

    # 3. One-hot encode Contract and PaymentMethod
    df = pd.get_dummies(
        df,
        columns=['Contract', 'PaymentMethod'],
        drop_first=True,
        dtype=int
    )

    # 4. Ordinal encode TenureGroup alphabetically
    tenure_oe = preprocessing.OrdinalEncoder()

    df[['TenureGroup']] = tenure_oe.fit_transform(
        df[['TenureGroup']]
    ).astype(int)

    return df, churn_le, binary_oe, tenure_oe
