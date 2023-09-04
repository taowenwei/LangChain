from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA

ProductBase = """
    PlutoTV mopnthly subscription
    Description: Watch in Full HD (1080p) with select titles in 4K HDR with Dolby Atmos. Stream on 1 screens at a time. Pay monthly and cancel at any time,
    Price: $14.99
    
    PlutoTV annualy subscription
    Description: Watch in 4K UHD. Stream on 3 screens at a time. ay annually and cancel at any time',
    Price: $99.99
    """


def getKnowledgebase():
    splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=0)
    texts = splitter.split_text(ProductBase)

    llm = OpenAI(temperature=0)
    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(
        texts, embeddings, collection_name="product-knowledge-base"
    )

    knowledgeBase = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=docsearch.as_retriever()
    )
    return knowledgeBase
