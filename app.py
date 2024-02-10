import streamlit as st 
from dotenv import load_dotenv
from utils import *
import pandas as pd


load_dotenv()


def main():
  st.set_page_config(page_title='Invoice Extraction Bot')
  st.title('Invoice Extraction Bot 🙎‍♀️...')
  st.subheader('I help you to extract the data out of pdf invoices')

  files=st.file_uploader('Please upload file here (*.pdf)',type=['pdf'],accept_multiple_files=True)
  data_output=st.selectbox('Data Output',['CSV','JSON'])

  ex_button=st.button('Extract Data')
  

  if ex_button:
    
    with st.spinner('Wait for it.....'):
      #get data
      texts=pdf_read(files)
      # st.write(texts)

      json_op=True if data_output=='JSON' else False
      response_list=[]
      for text in texts:
        prompt=extract_data_prompt(text,json_op=json_op)
        # st.write(prompt)
        # st.divider()
        response=llm_result(prompt)
        # st.write(response)
        response_list.append(eval(response[response.find('{'):response.find('}')+1]))
      
      #output
      df=pd.DataFrame(response_list)
      df_csv=df.to_csv(index=False).encode("utf-8")
      st.write(df)
      #show_case in table format

      st.download_button(
        'Download as CSV',
        df_csv,
        'invoice_extraction.csv',
        'text/csv',
        key='download_button'
      )




if __name__=='__main__':
  main()