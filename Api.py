# Api for exposing the Model to the frontendfrom fastapi import FastAPI
from fastapi import FastAPI
from tensorflow import keras
from keras.utils import pad_sequences
import numpy as np
import pickle
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
from keras import mixed_precision
import tensorflow as tf
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",           
    allow_credentials=True,         
    allow_methods=["*"],             
    allow_headers=["*"],             
)
print(tf.config.list_physical_devices('GPU'))

policy = mixed_precision.Policy('mixed_float16')
mixed_precision.set_global_policy(policy)

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    tf.config.experimental.set_memory_growth(gpus[0], True)
else:
    print("Bruh")

decoder_transformer = keras.models.load_model('Models/LoginFormModelNew.keras')
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f) 

def generate_button_code(prompt):
    max_seq_len = 165
    prompt = "<Start> " + prompt + " <SEP>"
    
    input_sequence = tokenizer.texts_to_sequences([prompt])[0]
    current_sequence = pad_sequences([input_sequence], maxlen=max_seq_len-1, padding='post')
    
    generated_tokens = []
    for _ in range(200):  
        predictions = decoder_transformer.predict(current_sequence, verbose=0)
        next_token = np.argmax(predictions[0, len(input_sequence) + len(generated_tokens) - 1])
        
        if next_token == tokenizer.word_index.get("<End>", 0) or next_token == 0:
            break
            
        generated_tokens.append(next_token)
        
        new_sequence = input_sequence + generated_tokens
        current_sequence = pad_sequences([new_sequence], maxlen=max_seq_len-1, padding='post')
    
    result = [tokenizer.index_word.get(token, "") for token in generated_tokens]
    return " ".join(result)

@app.get("/get/response/{prompt}")
def getResponseFromModel(prompt:str):
    return generate_button_code(prompt)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Api:app", host="0.0.0.0", port=8000, reload=True)