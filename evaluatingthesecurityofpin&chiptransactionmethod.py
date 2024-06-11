# -*- coding: utf-8 -*-
"""EvaluatingtheSecurityofPin&ChipTransactionMethod.ipynb

"""

import pandas as pd
from google.colab import files
import matplotlib.pyplot as plt

uploaded = files.upload()

data = pd.read_csv("card_transdata.csv")

data.head()

chippindf = data[["used_chip","used_pin_number","fraud"]]

total_transactions = len(chippindf)
total_fraud = chippindf["fraud"].sum()
fraud_by_chip = chippindf[chippindf["used_chip"]==1]["fraud"].sum()
fraud_by_pin = chippindf[chippindf["used_pin_number"]==1]["fraud"].sum()

print("Total transactions:", total_transactions)
print("Total fraud cases:", total_fraud)
print("Fraud cases using chip: {} out of {}".format(fraud_by_chip,total_transactions))
print("Fraud cases using pin: {} out of {}".format(fraud_by_pin,total_transactions))

labels_chip = ["Non-Fraud","Fraud"]
sizes_chip = [total_transactions - fraud_by_chip,fraud_by_chip]
colors_chip = ["lightskyblue", "lightcoral"]
labels_pin = ["Non-Fraud","Fraud"]
sizes_pin = [total_transactions - fraud_by_pin,fraud_by_pin]
colors_pin = ["lightskyblue", "lightcoral"]
plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.pie(sizes_chip,labels=labels_chip, colors=colors_chip, startangle=140)
plt.axis("equal")
plt.title("Chip Transactions")
plt.subplot(1,2,2)
plt.pie(sizes_pin,labels=labels_pin, colors=colors_pin, startangle=140)
plt.axis("equal")
plt.title("Pin Transactions")
plt.suptitle("Fraud cases in Chip and pin transaction")
plt.show