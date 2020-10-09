from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import pickle
from fastapi import FastAPI
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import re
import numpy as np
import os
import pandas as pd
import json
from pydantic import BaseModel
from enum import Enum

app = FastAPI()


def clean_text(text):
    #text = text.lower()
    text = re.sub(r"what's","what is", text)
    text = re.sub(r"rt", '',text)
    text = re.sub(r"\'ve","have", text)
    text = re.sub(r"can't","cannot",text)
    text = re.sub(r"n't", "not", text)
    text = re.sub(r"i'm","i am", text)
    text = re.sub(r"\'re'","are", text)
    text = re.sub(r"\'d'","would",text)
    text = re.sub(r"\'ll'", "will", text)
    text = re.sub(r"\'scuse'", "excuse", text)
    text = re.sub("\W",' ', text)
    text = re.sub('\s+',' ',text)
    text = text.strip(' ')
    return text

def clean(text):
    text = clean_text(text)
    x = vect.fit_transform([text])
    return (x)
    
max_features = 20000

def fake_news_preprocess(text):
    text = clean_text(text)
    tokenized_text = TK.texts_to_sequences(np.array([text]))
    vector = pad_sequences(tokenized_text, maxlen=400)
    return vector
    


def convertBytesToString(bytes):
    data = bytes.decode('utf-8').splitlines()
    df = pd.DataFrame(data)
    print(df)
    return parse_csv(df)
    
    
def parse_csv(df):
    result = df.to_json(orient='records')
    parsed = json.loads(result)
    return parsed
    

    
#@app.get('/')
async def main():
    return "Deploy Model"

class Strictness(str, Enum):
    strict = 'strict'
    moderate = 'moderate'
    relaxed = 'relaxed'

@app.get('/model/{strictness}')
async def get_model(strictness: Strictness):
    level = strictness.value
    if level=='strict':
        a = 0.8
        b = 0.8
    elif level=='moderate':
        a = 0.90
        b = 0.88
    elif level =='relaxed':
        a = 0.98
        b = 0.95
    else:
        a = 0.9
        b = 0.8
    global c
    c=a
    global d
    d=b
    global LEVEL
    LEVEL=level
    return {'level':level}
    

class Config:
    orm_mode = True



with open("TK1.pkl",'rb') as f:
    TK = pickle.load(f)
       
model_path = os.path.abspath('model1.keras')
model = load_model(model_path)

class LEVEL(str, Enum):
    medium = 'medium'
    strict = 'strict'
    relaxed = 'relaxed'

no_tolerance = []
offensive = []
"""
@app.put('/items/{item_id}')
def save_item(item_id:int):
    return{"item_id":item_id}
"""
#print(item_id)
@app.post('/items/{item_id}')
async def parsecsv(file:UploadFile = File(...)):
    #print(level())
    no_tolerance = []
    offensive = []
    #a= 0
    #b=0
    print('------')
    #print(level)
    #a, b = 0.9, 0.9
    print(c, d)
    #a=0.9
    #b=0.9
    contents = await file.read()
    text = convertBytesToString(contents)
    json_string =convertBytesToString(contents)
    json_string = list(map(lambda x: (clean_text(str(x))) , json_string))
    #list_tokenized_x = TK.texts_to_sequences(json_string[1])
    maxlen = 400
    tokenized_text = TK.texts_to_sequences(json_string)
    vector = pad_sequences(tokenized_text, maxlen=400)
    prediction = model.predict(vector)
    for i in range (len(prediction)):
        if prediction[i][0]>c:
            no_tolerance.append(text[i]['0'])
        elif prediction[i][0]+prediction[i][1]>d:
            offensive.append(text[i]['0'])
    return {'level':LEVEL, 'no_tolerance':no_tolerance, 'offensive':offensive}

if __name__=='__main__':
    import uvicorn
    uvicorn.run(app, port=8000, debug=True)
