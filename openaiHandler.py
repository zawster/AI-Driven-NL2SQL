import os
from openai import OpenAI
from config import OPENIAI_API_KEY
def get_completion_from_messages(system_message, user_message, model="gpt-3.5-turbo", temperature=0, max_tokens=500) -> str:
    """
    This method calls openai chatcompletion with the provided system message
    and user message(passed by user) and returns the content response returned 
    by openai model.
    """
    try:
        messages = [
            {'role': 'system', 'content': system_message},
            {'role': 'user', 'content': f"{user_message}"}
        ]
        client = OpenAI(api_key=OPENIAI_API_KEY)        
        # response = openai.ChatCompletion.create(
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature, 
            max_tokens=max_tokens, 
        )
        message = response.choices[0].message.content
        return message
    except Exception as exp:
        print(f"#### Openai Issue: {exp}")