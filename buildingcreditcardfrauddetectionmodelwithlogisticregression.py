# -*- coding: utf-8 -*-
"""BuildingCreditCardFraudDetectionModelwithLogisticRegression.ipynb

"""

import pandas as pd
from google.colab import files
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

uploaded = files.upload()

data = pd.read_csv("card_transdata.csv")

data.head()

X = data.drop("fraud",axis=1)
y = data["fraud"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
logreg_classifier = LogisticRegression(max_iter=1000, random_state=42)
logreg_classifier.fit(X_train_scaled,y_train)
new_transaction_features1 = pd.DataFrame({
    'distance_from_home': [89],
    'distance_from_last_transaction': [15],
    'ratio_to_median_purchase_price': [2.3],
    'repeat_retailer': [1],
    'used_chip': [0],
    'used_pin_number': [1],
    'online_order': [1]
})
prediction = logreg_classifier.predict(scaler.transform(new_transaction_features1))
print("\nPrediction for New Transaction:")
print("Fraud" if prediction[0] == 1 else "Legitimate")