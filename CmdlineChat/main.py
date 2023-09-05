from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
# from langchain.llms import HuggingFaceHub
# from langchain.llms import LlamaCpp
# from langchain.callbacks.manager import CallbackManager
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


def createConversationalChain():
    llm = ChatOpenAI()

    # from huggingface hub
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl",
    #                      model_kwargs={"temperature": 0.5, "max_length": 512})

    # from local model bin
    #  - original from huggingface TheBloke/Llama-2-7B-Chat-GGML
    #  - downloaded its llama-2-7b-chat.ggmlv3.q2_K.bin file to local
    #  - converted from ggml format to gguf, by `python3 ./convert-llama-ggmlv3-to-gguf.py --eps 1e-5 --input llama-2-7b-chat.ggmlv3.q2_K.bin --output llama-2-7b-chat.gguf.q2_K.bin``
    # llm = LlamaCpp(
    #     model_path="C:\\Users\\WTAO-WIN\\Documents\\llama-2-7b-chat.gguf.q2_K.bin",
    #     temperature=0.75,
    #     max_tokens=2000,
    #     top_p=1,
    #     n_ctx=2048,
    #     callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    #     verbose=True,  # Verbose is required to pass to the callback manager
    # )

    loader = PyPDFLoader('C:\\Users\\WTAO-WIN\\Downloads\\taowenwei.pdf')
    # loader = PyPDFLoader('C:\\Users\\WTAO-WIN\\Downloads\\TheEconomist.2023.08.26.pdf')
    pages = loader.load_and_split()
    vectorstore = FAISS.from_documents(pages, OpenAIEmbeddings())
    retriever = vectorstore.as_retriever()

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )
    return chain


def main():
    load_dotenv()
    os.system('cls' if os.name == 'nt' else 'clear')

    print('\033[34m')
    print('preparing ConversationalRetrievalChain ...')
    chain = createConversationalChain()
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
