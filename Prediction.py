import json
import tensorflow as tf
import numpy as np 
import pandas as pd 
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json

import re



Model_path = "Model/News_Classfication.keras"
Tokenizer_path = "Model/tokenizer.json"


Model = load_model(Model_path)
with open(Tokenizer_path,'r') as f:
    tokenizer = tokenizer_from_json(f.read())


def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
class_names = ['World', 'Sports', 'Business', 'Sci/Tech']
def Predict(sentences: list[str]):
    results = []
    cleaned = [clean_text(s) for s in sentences]
    sen_seq = tokenizer.texts_to_sequences(cleaned)
    sen_padded = pad_sequences(sen_seq, padding = 'post', truncating = 'post',maxlen =  400)

    preds = Model.predict(sen_padded)

    for sen,pred in zip(cleaned,preds):

        idx = int(np.argmax(pred))
        results.append({
            'Sentence' : sen,
            'Category' : class_names[idx],
            'Confidence' : float(np.max(pred))
        }
            
        )
        
    return results





