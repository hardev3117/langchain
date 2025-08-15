from langchain_community.document_loaders import TextLoader
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Create Ollama chat model instance
model = ChatOllama(
    model="llama3.2:1b",  # LLaMA 3.2 1B model
    temperature=0.3,
    top_p=0.3
    #num_predict=10  # Similar to max_completion_tokens
)

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('content/cricket.txt', encoding='utf-8')

docs = loader.load()

# print(type(docs))

# print(len(docs))

# print(docs[0].page_content)

# print(docs[0].metadata)

chain = prompt | model | parser

result = chain.invoke({'poem':docs[0].page_content})

print(result)
