from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

model = ChatOllama(
    model="llama3.2:1b",  # LLaMA 3.2 1B model
    temperature=1.5
    #num_predict=10  # Similar to max_completion_tokens
)

def chat_with_llm(domain_name:str, topic_name:str):
    chat_template = ChatPromptTemplate([
        ('system', 'You are a helpful {domain} expert'),
        ('human', 'Explain in simple terms, what is {topic}')
    ])

    prompt = chat_template.invoke({'domain':domain_name,'topic':topic_name})
    
    result = model.invoke(prompt)

    return result.content



if __name__ == "__main__":        
    result = chat_with_llm("cricket","bicket")
    print(result)