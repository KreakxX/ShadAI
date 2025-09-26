# Api for exposing the Model to the frontendfrom fastapi import FastAPI
from fastapi import FastAPI
from tensorflow import keras
from keras.utils import pad_sequences
import numpy as np
import pickle
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",           
    allow_credentials=True,         
    allow_methods=["*"],             
    allow_headers=["*"],             
)
 
def generate_button_code(prompt):
    decoder_transformer = keras.models.load_model('Models/MultiComponentModel.keras')
    max_seq_len = 37
    with open("tokenizer.pkl", "wb") as f:
      tokenizer = pickle.load(tokenizer, f)
    prompt = "<Start> " + prompt + " <SEP>"
    
    input_sequence = tokenizer.texts_to_sequences([prompt])[0]
    current_sequence = pad_sequences([input_sequence], maxlen=max_seq_len-1, padding='post')
    
    generated_tokens = []
    for _ in range(50):  
        predictions = decoder_transformer.predict(current_sequence, verbose=0)
        next_token = np.argmax(predictions[0, len(input_sequence) + len(generated_tokens) - 1])
        
        if next_token == tokenizer.word_index.get("<End>", 0) or next_token == 0:
            break
            
        generated_tokens.append(next_token)
        
        new_sequence = input_sequence + generated_tokens
        current_sequence = pad_sequences([new_sequence], maxlen=max_seq_len-1, padding='post')
    
    result = [tokenizer.index_word.get(token, "") for token in generated_tokens]
    return " ".join(result)

test_prompt = "Generate a Dark Blue Button saying Jan"
generated = generate_button_code(test_prompt)
print("Generated Button Code:", generated)


@app.get("/get/response/{prompt}")
def getResponseFromModel(prompt:str):
    generate_button_code(prompt)