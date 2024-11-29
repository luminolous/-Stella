import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

from Mathematic.connector import run_math_operation
# from Mathematic.connector.basic_math_op import penjumlahan, pengurangan, perkalian, pembagian, perpangkatan, prime
from Text_summarize.first import generate_sum

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('.\Stella-2.0\intents.json').read())

words = pickle.load(open('.\Stella-2.0\words.pkl', 'rb'))
classes = pickle.load(open('.\Stella-2.0\classes.pkl', 'rb'))
model = load_model('.\Stella-2.0\Stella-model.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    
    results = [[i, r] for i, r in  enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)

    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

print("Stella is ready...")

while True:
    message = input("You : ")
    ints = predict_class(message)
    res = get_response(ints, intents)
    if res == "operasi_matematika_penjumlahan":
        run_math_operation(res)
    elif res == "summarizing_function":
        file_name = ""
        generate_sum(file_name, 2)
    elif res == "cek_bilangan_prima":
        run_math_operation(res)
    else:
        print(f"Stella : {res}")