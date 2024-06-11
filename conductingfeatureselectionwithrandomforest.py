# -*- coding: utf-8 -*-
"""ConductingFeatureSelectionwithRandomForest.ipynb

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
feature_importances = pd.Series(rf_classifier.feature_importances_, index=X.columns).sort_values(ascending=False)
print("Ranked Feature Importance:")
print(feature_importances)