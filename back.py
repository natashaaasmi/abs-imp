import langchain
import os
os.environ["OPENAI_API_KEY"] = "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"
from langchain import OpenAI, LLMChain, PromptTemplate

llm = OpenAI(temperature=0.5)

template = """
Define the term {term} 
"""
prompt = PromptTemplate(template=template,input_variables= ["term"])
llm_chain = LLMChain(prompt=prompt, llm=llm,verbose=True)

respnse = print(llm_chain.predict(term="DNA synthesis"))