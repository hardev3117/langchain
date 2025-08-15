
from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv

load_dotenv()


# No need for .env if running Ollama locally (unless you want to load other vars)
# from dotenv import load_dotenv
# load_dotenv()

# Create Ollama chat model instance
model = ChatOllama(
    model="llama3.2:1b",  # LLaMA 3.2 1B model
    temperature=0.3,
    top_p=0.3
    #num_predict=10  # Similar to max_completion_tokens
)

# Run the model
result = model.invoke("write 5 line summary on generativ AI. provide summary in points")

# Print only the generated text
print(result.content)