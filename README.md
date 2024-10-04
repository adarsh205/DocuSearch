# DocuSearch

**DocuSearch** is an AI-powered platform that allows users to upload files (TXT, PDF, CSV, DOCX) and ask queries related to the file contents, delivering instant, intelligent answers through a simple interface.

## Features
- **Multi-file Format Support**: Supports TXT, PDF, and DOCX file types.
- **AI-Powered Querying**: Allows users to ask natural language questions about file contents and receive instant answers.
- **Flask Web Interface**: Simple and user-friendly web-based interface using Flask.
- **Fast & Accurate**: Quickly retrieves relevant information from documents.

## How It Works
1. **Upload a File**: Upload a TXT, PDF, CSV, or DOCX file.
2. **Submit a Query**: Enter a question related to the contents of the file.
3. **Get Answers**: The system processes the document and provides a precise answer to your question.

## Installation

### Prerequisites
- Python 3.x
- Flask

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/adarsh205/DocuSearch.git
   ```
   
2. Navigate to the project directory:
   ```bash 
   cd project-name
   ```
   
3. Install the dependencies from `requirements.txt`:
   ```bash 
   pip install -r requirements.txt
   ```
   
4.Get your GEMINI_API_KEY from `https://ai.google.dev/gemini-api?lang=python`

5.Set your SECRET_KEY for CSRF:
   ```python
   import os
   SECRET_KEY = os.urandom(32)
   ```
   
5. Store your SECRET_KEY and GEMINI_API_KEY in .env file:
   ```plaintext
   GEMINI_API_KEY = { Your api key }
   SECRET_KEY = { Your secret key }
   ```
   
6. Run the Flask server:
   ```bash 
   flask run
   ```
   
The server will start on `http://127.0.0.1:5000/` by default.

### Requirements
Make sure the `requirements.txt` file includes:
```plaintext
python-docx
google-generativeai
Bootstrap_Flask==2.2.0
Flask_WTF==1.2.1
WTForms==3.0.1
Flask==2.3.2
PyPDF2~=3.0.1
python-dotenv==1.0.1
```

## Usage
1. Navigate to `http://127.0.0.1:5000/` in your browser.
2. Upload your file (`TXT`, `PDF`, or `DOCX`).
3. Type a query related to the file content.
4. Get an instant response powered by the AI model.
   
## Contact

For questions or feedback, please contact us at `adarshg205205@gmail.com`.
