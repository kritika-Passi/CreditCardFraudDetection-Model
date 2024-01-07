import streamlit as st 
import pandas as pd 
import joblib

model = joblib.load('C:/Users/jazz3/OneDrive/Desktop/CreditCardFraudDetection.joblib')

new_data_point = {
   'Time': 100001,   # Replace with an appropriate value
    'V1': -1.0,        # Replace with an appropriate value
    'V2': 0.0,         # Replace with an appropriate value
    'V3': -1.5,        # Replace with an appropriate value
    'V4': 0.5,         # Replace with an appropriate value
    'V5': -0.5,        # Replace with an appropriate value
    'V6': 0.0,         # Replace with an appropriate value
    'V7': -1.0,        # Replace with an appropriate value
    'V8': 0.5,         # Replace with an appropriate value
    'V9': -1.0,        # Replace with an appropriate value
    'V10': 1.5,        # Replace with an appropriate value
    'V11': -1.0,       # Replace with an appropriate value
    'V12': 1.0,        # Replace with an appropriate value
    'V13': 1.0,        # Replace with an appropriate value
    'V14': 0.5,        # Replace with an appropriate value
    'V15': -0.5,       # Replace with an appropriate value
    'V16': 1.0,        # Replace with an appropriate value
    'V17': -0.5,       # Replace with an appropriate value
    'V18': 1.0,        # Replace with an appropriate value
    'V19': -1.0,       # Replace with an appropriate value
    'V20': 0.5,        # Replace with an appropriate value
    'V21': -0.5,       # Replace with an appropriate value
    'V22': 1.0,        # Replace with an appropriate value
    'V23': -0.5,       # Replace with an appropriate value
    'V24': 0.5,        # Replace with an appropriate value
    'V25': -0.5,       # Replace with an appropriate value
    'V26': 0.5,        # Replace with an appropriate value
    'V27': -0.5,       # Replace with an appropriate value
    'V28': 0.0,        # Replace with an appropriate value
    'Amount': 100.0    # Replace with an appropriate value

}

new_data = pd.DataFrame([new_data_point])

fraud_prediction = model.predict(new_data)

print("Prediction for the data given :")
print(fraud_prediction)
if fraud_prediction != 0 :
  print("Fraud detected")
else:
  print("NO Fraud detected")