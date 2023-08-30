from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
# from langchain.vectorstores import Pinecone

def createOpenAIChain(text_chunks):
    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    # vectorstore = Pinecone.from_texts(texts=text_chunks, embedding=embeddings, index_name='sandbox')

    llm = ChatOpenAI()

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain