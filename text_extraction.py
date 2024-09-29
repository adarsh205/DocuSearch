import PyPDF2
from docx import Document


def extract(file, file_extension):
    if file_extension == "txt":
        extracted_text = extract_txt(file)
    elif file_extension == "pdf":
        extracted_text = extract_pdf(file)
    elif file_extension == "docx":
        extracted_text = extract_docx(file)
    return extracted_text


def extract_pdf(file):
    # Read PDF file using PyPDF2
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    return text


def extract_docx(file):
    doc = Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text


def extract_txt(file):
    # Read TXT file
    text = file.read()
    return text
