from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

def createConversationalChain():
    loader = PyPDFLoader('TheEconomist.2023.08.26.pdf')
    pages = loader.load_and_split()
    vectorstore = FAISS.from_documents(pages, OpenAIEmbeddings())
    retriever = vectorstore.as_retriever()

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    
    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(),
        retriever=retriever,
        memory=memory
    )
    return chain

def main():
    load_dotenv()
    os.system('cls' if os.name == 'nt' else 'clear')

    print('\033[34m')
    print('preparing ConversationalRetrievalChain ...')
    chain  = createConversationalChain()
    print('chain construction completed')
    while True:
        print('\033[35m')
        question = input('Your Question: ')
        history = chain({'question': question})['chat_history']
        print('\033[0m')
        print(history[len(history) - 1].content)
        print()



if __name__ == '__main__':
    main()