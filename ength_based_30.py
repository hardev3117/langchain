from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('content/dl-curriculum.pdf')

docs = loader.load()
3
splitter = CharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50,
    separator=''
)

result = splitter.split_documents(docs)

print(result[1].page_content)

print("--------------------------")
print(result[2].page_content)

print("--------------------------")

print(result[3].page_content)