import streamlit as st
import pandas as pd
import joblib

# Load the model
model = "./CreditCardFraudDetection.joblib"



def fraud_detection(data):
   fraud_prediction = model.predict(data)
   print("Prediction for the data given :")
   print(fraud_prediction)
   if fraud_prediction != 0 :
        return "Fraud detected"
   else:
        return "No Fraud detected"
   

def main():
    # Creating the streamlit app
    st.title('Credit Card Fraud Detection App')

    # Collect user input using Streamlit widgets
    time = st.slider('Time', min_value=0, max_value=200000, value=100001)
    v1 = st.slider('V1', min_value=-5.0, max_value=5.0, value=-1.0)
    v2 = st.slider('V2', min_value=-5.0, max_value=5.0, value=0.0)
    v3 = st.slider('V3', min_value=-5.0, max_value=5.0, value=-1.5)
    v4 = st.slider('V4', min_value=-5.0, max_value=5.0, value=0.5)
    v5 = st.slider('V5', min_value=-5.0, max_value=5.0, value=-0.5)
    v6 = st.slider('V6', min_value=-5.0, max_value=5.0, value=0.0)
    v7 = st.slider('V7', min_value=-5.0, max_value=5.0, value=-1.0)
    v8 = st.slider('V8', min_value=-5.0, max_value=5.0, value=0.5)
    v9 = st.slider('V9', min_value=-5.0, max_value=5.0, value=-1.0)
    v10 = st.slider('V10', min_value=-5.0, max_value=5.0, value=1.5)
    v11 = st.slider('V11', min_value=-5.0, max_value=5.0, value=-1.0)
    v12 = st.slider('V12', min_value=-5.0, max_value=5.0, value=1.0)
    v13 = st.slider('V13', min_value=-5.0, max_value=5.0, value=1.0)
    v14 = st.slider('V14', min_value=-5.0, max_value=5.0, value=0.5)
    v15 = st.slider('V15', min_value=-5.0, max_value=5.0, value=-0.5)
    v16 = st.slider('V16', min_value=-5.0, max_value=5.0, value=1.0)
    v17 = st.slider('V17', min_value=-5.0, max_value=5.0, value=-0.5)
    v18 = st.slider('V18', min_value=-5.0, max_value=5.0, value=1.0)
    v19 = st.slider('V19', min_value=-5.0, max_value=5.0, value=-1.0)
    v20 = st.slider('V20', min_value=-5.0, max_value=5.0, value=0.5)
    v21 = st.slider('V21', min_value=-5.0, max_value=5.0, value=-0.5)
    v22 = st.slider('V22', min_value=-5.0, max_value=5.0, value=1.0)
    v23 = st.slider('V23', min_value=-5.0, max_value=5.0, value=-0.5)
    v24 = st.slider('V24', min_value=-5.0, max_value=5.0, value=0.5)
    v25 = st.slider('V25', min_value=-5.0, max_value=5.0, value=-0.5)
    v26 = st.slider('V26', min_value=-5.0, max_value=5.0, value=0.5)
    v27 = st.slider('V27', min_value=-5.0, max_value=5.0, value=-0.5)
    v28 = st.slider('V28', min_value=-5.0, max_value=5.0, value=0.0)
    amount = st.slider('Amount', min_value=0.0, max_value=1000.0, value=100.0)


    # Create a dictionary with user input
    new_data_point = {
        'Time': time,
        'V1': v1,
        'V2': v2,
        'V3': v3,
        'V4': v4,
        'V5': v5,
        'V6': v6,
        'V7': v7,
        'V8': v8,
        'V9': v9,
        'V10': v10,
        'V11': v11,
        'V12': v12,
        'V13': v13,
        'V14': v14,
        'V15': v15,
        'V16': v16,
        'V17': v17,
        'V18': v18,
        'V19': v19,
        'V20': v20,
        'V21': v21,
        'V22': v22,
        'V23': v23,
        'V24': v24,
        'V25': v25,
        'V26': v26,
        'V27': v27,
        'V28': v28,
        'Amount': amount
    }

    new_data = pd.DataFrame([new_data_point])
    st.write(new_data)

    diagnoses =""

    #creating a button for prediction
    if st.button("Check"):
        diagnoses = fraud_detection(new_data)

    st.success(diagnoses)

if __name__ == "__main__":
    main()


