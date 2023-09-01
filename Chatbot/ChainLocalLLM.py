from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import GPT4AllEmbeddings
from langchain.llms import OpenLLM


def createLocalLLMChain(text_chunks):
    embeddings = GPT4AllEmbeddings()

    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)

    llm = OpenLLM(
        model_name="dolly-v2",
        model_id="databricks/dolly-v2-3b",
        temperature=0.94,
        repetition_penalty=1.2,
    )

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain
