import os
from dotenv import load_dotenv
import google.generativeai as genai
# Load variables from .env file
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Define the endpoint for generating text
ENDPOINT = "https://api.openai.com/v1/completions"

model = genai.GenerativeModel('gemini-pro')


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

    response = model.generate_content(prompt)
    return response.text
