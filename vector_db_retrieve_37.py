
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


vector_store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory='my_chroma_db',
    collection_name='sample'
)

# search with similarity score
result = vector_store.similarity_search_with_score(
    query='Who among these are a bowler?',
    k=2
)


print(result)