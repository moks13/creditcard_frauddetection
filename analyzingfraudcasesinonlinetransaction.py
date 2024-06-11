# -*- coding: utf-8 -*-


import pandas as pd
from google.colab import files

uploaded = files.upload()

data = pd.read_csv("card_transdata.csv")

data.head()

online_order_df = data[["online_order","fraud"]]

total_online_orders = online_order_df["online_order"].sum()
total_online_fraud = online_order_df[(online_order_df["fraud"]==1)&(online_order_df["online_order"]==1)]["fraud"].count()
fraud_rate_online = total_online_fraud/total_online_orders
total_offline_orders = len(online_order_df) - total_online_orders
total_offline_fraud = online_order_df[(online_order_df["fraud"]==1)&(online_order_df["online_order"]==0)]["fraud"].count()
fraud_rate_offline = total_offline_fraud/total_offline_orders
print(f"Fraud rate for online transactions: {fraud_rate_online:.2%} ({total_online_fraud} cases out of {total_online_orders} online transactions)")
print(f"Fraud rate for offline transactions: {fraud_rate_offline:.2%} ({total_offline_fraud} cases out of {total_offline_orders} offline transactions)")