import streamlit as st
import requests

APP_URL = "http://127.0.0.1:8000/predict"

st.title('News Article Classifier')

text = st.text_area("Enter News")

if st.button("Classify"):

    sentences = [line.strip() for line in text.split("\n") if line.strip()]
    if not sentences:
        st.warning("Enter valid News")
    else:
        response = requests.post(
            APP_URL,
            json = {"texts":sentences}
        )
    
        if response.status_code == 200:
            results = response.json()
            #st.write(response.json())

            for r in results:
                st.write(f"{r['Sentence']}")
                st.success(f"Category :{r['Category']}")
                st.info(f"Confidence:{r['Confidence']}")

        else:
            st.error("response.text()")
