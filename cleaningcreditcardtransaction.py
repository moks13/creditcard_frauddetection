# -*- coding: utf-8 -*-
"""CleaningCreditCardTransaction.ipynb

"""

import pandas as pd
from google.colab import files

uploaded = files.upload()

data = pd.read_csv("card_transdata.csv")

data.head()

missing_values = data.isnull().any(axis=1)
print("Rows with Missing Values:")
print(missing_values)

duplicate_rows = data[data.duplicated()]
print("Deuplicated Rows:")
print(duplicate_rows)

data.dropna(axis=0, inplace=True)

data.drop_duplicates(inplace=True)