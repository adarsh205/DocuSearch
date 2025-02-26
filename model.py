import os
from dotenv import load_dotenv
from google import genai
# Load variables from .env file
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)


def generate(extracted_text, question):

    prompt = f'''
    You are an expert at answering questions based on some context provided to you.
    Your goal is to help the users with questions they have about the information below.
    
    ____________________________________________________________________________
    Context:
    {extracted_text}
    
    ____________________________________________________________________________
    Question:
    {question}
    
    '''

    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return response.text
