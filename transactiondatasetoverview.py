# -*- coding: utf-8 -*-
"""CreditCardTransactionDatasetOverview.ipynb
"""

import pandas as pd
from google.colab import files

uploaded = files.upload()

data = pd.read_csv("card_transdata.csv")

data.head()

data.tail()

data.info()

data.shape

data.describe()

data.columns

data.dtypes