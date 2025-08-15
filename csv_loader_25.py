from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='content/Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[0])
print(docs[1])
print(docs[2])