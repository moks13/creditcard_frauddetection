# -*- coding: utf-8 -*-
"""AnalyzingRepeatRetailerFraudPattern.ipynb

"""

import pandas as pd
from google.colab import files

uploaded = files.upload()

data = pd.read_csv("card_transdata.csv")

data.head()

repeat_retailer_df = data[data["repeat_retailer"]==1]

fraud_sequences = []
current_sequence = []

for index, row in repeat_retailer_df.iterrows():
    repeat_retailer, is_fraud = row['repeat_retailer'], row['fraud']

    if is_fraud == 1:
        if current_sequence:
            fraud_sequences.append(current_sequence.copy())
        current_sequence = []
    else:
        current_sequence.append('Repeat Retailer' if repeat_retailer == 1 else 'No Repeat Retailer')

for i, sequence in enumerate(fraud_sequences[:10], start=1):
    print(f"Fraud Sequence {i}: {', '.join(sequence)}")