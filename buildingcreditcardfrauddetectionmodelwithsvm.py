# -*- coding: utf-8 -*-
"""BuildingCreditCardFraudDetectionModelwithSVM.ipynb


"""

import pandas as pd
from google.colab import files
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.calibration import CalibratedClassifierCV

uploaded = files.upload()

data = pd.read_csv("card_transdata.csv").sample(1000,random_state=42)

data.head()

X = data.drop("fraud",axis=1)
y = data["fraud"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
svm_classifier = SVC(kernel = "linear", probability=True, random_state=42)
calibrated_svm = CalibratedClassifierCV(svm_classifier)
calibrated_svm.fit(X_scaled,y)
distance_from_home = float(input("Enter Distance From Home: "))
distance_from_last_transaction = float(input("Enter Distance From Last Transaction: "))
ratio_to_median_purchase_price = float(input("Enter Ratio to Median Purchase Price: "))
repeat_retailer = int(input("Enter Repeat Retailer (0 or 1): "))
used_chip = int(input("Enter Used Chip (0 or 1): "))
used_pin_number = int(input("Enter Used Pin Number (0 or 1): "))
online_order = int(input("Enter Online Order (0 or 1): "))
new_transaction_features = pd.DataFrame({
    'distance_from_home': [distance_from_home],
    'distance_from_last_transaction': [distance_from_last_transaction],
    'ratio_to_median_purchase_price': [ratio_to_median_purchase_price],
    'repeat_retailer': [repeat_retailer],
    'used_chip': [used_chip],
    'used_pin_number': [used_pin_number],
    'online_order': [online_order]
})
scaled_transaction = scaler.transform(new_transaction_features)
prediction = calibrated_svm.predict(scaled_transaction)
probability_of_fraud = calibrated_svm.predict_proba(scaled_transaction)[:,1][0]
print("\nPrediction for New Transaction:")
print("Fraud" if prediction[0] == 1 else "Legitimate")
print(f"Probability of Fraud: {probability_of_fraud * 100:.2f}%")