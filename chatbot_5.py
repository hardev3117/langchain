#from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

#model = ChatOpenAI()

model = ChatOllama(
    model="llama3.2:1b",  # LLaMA 3.2 1B model
    temperature=1.5
    #num_predict=10  # Similar to max_completion_tokens
)

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break

    print(chat_history)
    result = model.invoke(chat_history)
    #result = model.invoke(user_input)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)