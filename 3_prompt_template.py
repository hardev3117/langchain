from langchain_core.prompts import PromptTemplate
#from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv

load_dotenv()

#model = ChatOpenAI()

# Create Ollama chat model instance
model = ChatOllama(
    model="llama3.2:1b",  # LLaMA 3.2 1B model
    temperature=1.5
    #num_predict=10  # Similar to max_completion_tokens
)

# detailed way
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

# fill the values of the placeholders
prompt = template2.invoke({'name':'Hardev'})

print(prompt)

# result = model.invoke(prompt)

# print(result.content)
