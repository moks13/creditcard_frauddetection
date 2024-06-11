# -*- coding: utf-8 -*-
"""BuildingCreditCardFraudDetectionModelwithRandomForest.ipynb

"""

import pandas as pd
from google.colab import files
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

uploaded = files.upload()

data = pd.read_csv("card_transdata.csv")

data.head()

X = data.drop("fraud",axis=1)
y = data["fraud"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train,y_train)
new_transaction_features = data.sample(1).drop('fraud',axis=1)
print("\nRandomly sampled features for new transaction:")
print(new_transaction_features)
prediction = rf_classifier.predict(new_transaction_features)
print("\nPrediction for new transaction:")
print("Fraud" if prediction[0] == 1 else "Legitimate")

new_transaction_features1 = pd.DataFrame({
    'distance_from_home': [7],
    'distance_from_last_transaction': [3],
    'ratio_to_median_purchase_price': [0.1],
    'repeat_retailer': [0],
    'used_chip': [1],
    'used_pin_number': [0],
    'online_order': [0]
})
prediction = rf_classifier.predict(new_transaction_features1)
print("\nPrediction for new transaction:")
print("Fraud" if prediction[0] == 1 else "Legitimate")