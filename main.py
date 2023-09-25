# main.py
import openai
openai.organization = "org-xAb1HpJGdShnFnr5luwmicwH"
openai.api_key = "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" #os.getenv("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")

#messages - {"role": "user", "content": '너는 누구니'}
def chat(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    assistant_messages = response['choices'][0]['message']
    return assistant_messages # {'role':'assistant', 'content':'blahblahblah'} 형식임!


from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()

class Turn(BaseModel):
    role:str
    content:str

class Messages(BaseModel):
    message_list:List[Turn]

@app.post('/chat')
def post_chat(messages : Messages):
    messages = messages.model_dump()  #dict()
    assistant_messages = chat(messages['message_list'])
    return assistant_messages
# uvicorn main:app --reload
