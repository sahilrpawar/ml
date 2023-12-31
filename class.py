# -*- coding: utf-8 -*-
"""Class.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oSjlTzJ2xE4BfIB_0VkJcWL7P8xBeJu8
"""

'''https://www.kaggle.com/datasets/nanditapore/healthcare-diabetes'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load your dataset (replace 'your_dataset.csv' with your dataset file path)
data = pd.read_csv('/content/Healthcare-Diabetes.csv')
data.fillna(data.mean(), inplace=True)


# Split the data into features (X) and the target variable (y)
X = data.drop('Outcome', axis=1)  # 'target_variable' is the column indicating the disease status
y = data['Outcome']

# Data preprocessing
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model selection (Logistic Regression)
model = LogisticRegression()

# Model training
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", confusion)
print("Classification Report:\n", report)