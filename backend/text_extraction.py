import pandas as pd
import PyPDF2
from docx import Document
import textract


def extract(file_path, file_extension):
    if file_extension == "csv":
        extracted_text = extract_csv(file_path)
    elif file_extension == "txt":
        extracted_text = extract_txt(file_path)
    elif file_extension == "pdf":
        extracted_text = extract_pdf(file_path)
    elif file_extension == "docx":
        extracted_text = extract_docx(file_path)
    return extracted_text


def extract_csv(file_path):
    df = pd.read_csv(file_path)
    text = "\n".join(df.iloc[:, :].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1))
    return text


def extract_pdf(file_path):
    # Read PDF file using PyPDF2
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text


def extract_docx(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text


def extract_txt(file_path):
    # Read TXT file
    with open(file_path, "r") as f:
        text = f.read()
    return text
