from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

while(True):
    print("\n Ask the SEC filing report a question: ")
    response = query_engine.query(str(input()))
    print(response)
