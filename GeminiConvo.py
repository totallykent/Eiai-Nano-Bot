import os
import google.generativeai as gemini
from google.generativeai.types import HarmCategory, HarmBlockThreshold


from dotenv import load_dotenv

def conversation(prompt):
    model = gemini.GenerativeModel('gemini-pro')
    response = model.generate_content(
        prompt,
        safety_settings={
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE 
        }
    )
    return response.text

def loadEnv():
    load_dotenv(override=True)
    gemini.configure(api_key=os.getenv('super_duper_secret_owo'))

def inviteLink():
    return os.getenv('invite_link')

def botID():
    return os.getenv('bot_id')

def main(userInput):
    return conversation(userInput)
