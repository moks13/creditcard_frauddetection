# -*- coding: utf-8 -*-
"""FindingCorrelationBetweenTransactionAmount&Fraud.ipynb

"""

import pandas as pd
from google.colab import files
import matplotlib.pyplot as plt

uploaded = files.upload()

data = pd.read_csv("card_transdata.csv")

data.head()

correlation_df = data[["ratio_to_median_purchase_price","fraud"]]

correlation = correlation_df["ratio_to_median_purchase_price"].corr(correlation_df["fraud"])
print(f"Correlation between transaction amount and fraud:{correlation}")

avgnonfraudtransaction = correlation_df[correlation_df["fraud"]==0]["ratio_to_median_purchase_price"].mean()
avgfraudtransaction = correlation_df[correlation_df["fraud"]==1]["ratio_to_median_purchase_price"].mean()
print(f"Average ratio to median purchase price for non frudelent transactions: {avgnonfraudtransaction}")
print(f"Average ratio to median purchase price for frudelent transactions: {avgfraudtransaction}")

categories = ["Non-fraudulent","Fraudulent"]
average_ratio = [avgnonfraudtransaction,avgfraudtransaction]
plt.bar(categories,average_ratio,color=['blue','red'])
plt.title("Ratio to Median Purchase Price")
plt.xlabel("Fraud Category")
plt.ylabel("Average ratio to median purchase price")
plt.show()