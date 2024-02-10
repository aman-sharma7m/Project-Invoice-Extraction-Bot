# Project Invoice Extraction Bot

## Introduction

The Invoice Extraction Bot is a Python program that helps extract data from PDF invoices. It provides a user-friendly interface where users can upload PDF files and choose the desired output format for the extracted data.

## Installation & create environment

Clone the project

```bash
  git clone link_to_copy
```

Go to the project directory

```bash
  cd proj_dir
```

Create the enviroment

```bash
  conda create --prefix ./lang_env
  conda activate {path}/lang_env
  python -m ipykernel install --user --name=lang_env
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Insert Open-ai api key

```bash
  touch .env
  insert your key as following
  OPENAI_API_KEY=""
  HUGGINGFACEHUB_API_TOKEN=""
```

Start the server

```bash
  streamlit run app.py
```

### Detailed Explanation:

Import necessary libraries: The program starts by importing the required libraries, including streamlit, dotenv, and pandas.

Load environment variables: The load_dotenv() function is called to load environment variables from a .env file. This step is important if the program requires any sensitive information.

Define the main function: The main() function is defined, which serves as the entry point of the program.

Set Streamlit page configuration: The st.set_page_config() function is called to set the title of the web page.

Display the title and subheader: The st.title() and st.subheader() functions are used to display the title and subheader of the web page, respectively.

File upload and data output selection: The st.file_uploader() function is used to allow users to upload PDF files. The st.selectbox() function is used to let users choose the desired output format for the extracted data.

Extract data button: The st.button() function is used to create a button that triggers the data extraction process when clicked.

Data extraction process: When the "Extract Data" button is clicked, the program performs the following steps:

Read the PDF files using the pdf_read() function from the utils module.
Determine the output format (CSV or JSON) based on the user's selection.
Iterate over each text extracted from the PDF files and pass it to the extract_data_prompt() function from the utils module. This function likely uses a machine learning model or natural language processing techniques to extract relevant data from the text.
Process the response from the extract_data_prompt() function and append it to a list.
Create a DataFrame from the list of responses using the pd.DataFrame() function from the pandas library.
Convert the DataFrame to CSV format using the to_csv() function and encode it as UTF-8.
Display the DataFrame on the web page using the st.write() function.
Provide a download button for users to download the extracted data as a CSV file.
Execute the main function: The if **name**=='**main**': block ensures that the main() function is only executed when the script is run directly, not when it is imported as a module.

The code provided consists of several functions that work together to extract data from PDF files:

pdf_read(files): This function takes a list of PDF files as input and returns a list of extracted texts from each file. It uses the PyPDF2 library to read the PDF files and extract the text data.

extract_data_prompt(pdf_data, json_op): This function takes the extracted text data and a boolean flag json_op as input. It creates a prompt template to extract specific values from the extracted text. The prompt template includes instructions for extracting values like Invoice Name, Date, Invoice Number, Description, Quantity, Unit Price, Amount, Total Amount, Mobile Number, Address, and Email. It also includes format instructions for the output.

llm_result(prompt): This function takes the prompt as input and uses the OpenAI LLM to generate a response based on the prompt.

## libraries

```
from PyPDF2 import PdfReader
from langchain.prompts import PromptTemplate,FewShotPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser, StructuredOutputParser, ResponseSchema
from langchain.llms import OpenAI
import streamlit as st
from dotenv import load_dotenv
from utils import *
import pandas as pd

```

## Conclusion

The Invoice Extraction Bot is a useful tool for extracting data from PDF invoices. It provides a user-friendly interface and supports both CSV and JSON output formats. By leveraging the power of Streamlit, the program allows users to easily upload PDF files and extract relevant data with just a few clicks.
