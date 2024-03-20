# ProtonDatalabs AI developer Assignment - Chatbot application

## Preface

This is an assignment given to me by ProtonDatalabs.

In this assignment, my goal was to build a chatbot application which accurately provides answers based on the uploaded file and question entered. 

As a starting file, I was provided with a simple application consisting:
1. A `frontend` directory with **typescript** code   
2. A `backend` directory with **python** code

The 2 parts of this application were linked using `fastapi` and when run, a simple webapp that would only display the result as `hello world!` no matter the input would start. Moreover, the only file format that could be accepted was the `csv` file extension.

## The Assignment
### Tasks
#### A. Frontend
1. To modify the `typescript` code such that it accepts `pdf, docx, txt` file extensions in addition to the `csv` file extension.
2. To use `CSS` to add simple design and structure to the application.
#### B. Backend
1. To extract the data in the input file as a `string`.
2. To use an `LLM` (large language model) in the `backend` to generate the answer to be displayed as the result.


## Approach

### Accepting different file extensions & Extracting data as text:
I have created a separate python file, `text_extraction.py` which contains the logic for the conversion of the file's data into `string` format.   

1. `pandas` library used for `csv`
2. `PyPDF2` library used for `pdf`
3. `textract` library used for `docx`
4. `open()` method used foe `txt`

If the file format is none of the above, The result is simply **"Unsupported file format"**.

### Generating the answer:
The python file, `model.py` is responsible for the loading of the LLM and the generation of the answer.

The LLM I have used is the `Gemini API`

The function `generate()` in this file takes the textual data extracted from the file and the question as input parameters and returns the answer to be displayed on the application as an output.

