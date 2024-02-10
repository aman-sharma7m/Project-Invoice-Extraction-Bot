from PyPDF2 import PdfReader
from langchain.prompts import PromptTemplate,FewShotPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser, StructuredOutputParser, ResponseSchema
from langchain.llms import OpenAI

def pdf_read(files):
  texts=[]
  for file in files:
    pdf_obj=PdfReader(file)
    text=''
    for page in pdf_obj.pages:
      data=page.extract_text()
      text+=data
    texts.append(text)
  return texts


def extract_data_prompt(pdf_data,json_op):
  template='''Extract all the following values: \n\n
                Invoice Name, Date, Invoice Number, Description, Quantity, Unit Price, Amount, Total Amount,Mobile Number,Address,Email \n\n
                from this data: \n\n {page} \n\n
                {format_ins}'''
  
  output_parser=CommaSeparatedListOutputParser()
  output_ins=output_parser.get_format_instructions()

  response_schema=[
    ResponseSchema(name='Name',description="This field covers information regarding person to whom bill is generated. it includes name,address,email."),
    ResponseSchema(name='Date',description='This field covers the date that has been mentioned on the document.'),
    ResponseSchema(name='Invoice_Number',description='This field covers the invoice number that has been mentioned on the document.'),
    ResponseSchema(name='Description',description='This field covers the description that has been mentioned on the document.'),
    ResponseSchema(name='Quantity',description='This field covers the Quantity that has been mentioned on the document.'),
    ResponseSchema(name='Unit_Price',description='This field covers the Unit Price that has been mentioned on the document.'),
    ResponseSchema(name='Amount',description='This field covers the Amount that has been mentioned on the document.'),
    ResponseSchema(name='Total_Amount',description='This field covers the Total Amount that has been mentioned on the document.'),
    ResponseSchema(name='Mobile_Number',description='This field covers the Mobile Number that has been mentioned on the document.'),
    ResponseSchema(name='Address',description='This field covers the Address that has been mentioned on the document.'),
    ResponseSchema(name='email',description='This field covers the email that has been mentioned on the document.')
  ]
  output_parser2=StructuredOutputParser.from_response_schemas(response_schema)
  format_inst2=output_parser2.get_format_instructions()
  prompt2=PromptTemplate(template=template,input_variables=['page'],partial_variables={'format_ins':format_inst2})
  prompt=PromptTemplate(template=template,input_variables=['page'],partial_variables={'format_ins':output_ins})
  final_prompt=prompt.format(page=pdf_data)
  final_prompt2=prompt2.format(page=pdf_data)

  if json_op:
    return final_prompt2
  else:
    return final_prompt

def llm_result(prompt):
  llm=OpenAI()
  return llm(prompt)




