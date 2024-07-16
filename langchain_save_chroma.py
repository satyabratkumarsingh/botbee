# import
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import chromadb
import uuid
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document



import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

OPENAI_API_KEY = '<KEY>'

def store_in_chroma(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0, separators=[
        "\n\n",
        "\n",
        " ",
        ".",
        ",",
        "\u200b",  # Zero-width space
        "\uff0c",  # Fullwidth comma
        "\u3001",  # Ideographic comma
        "\uff0e",  # Fullwidth full stop
        "\u3002",  # Ideographic full stop
        "",
    ])
    print('@@@@@@@@Splitting documents @@@@@@@@@@@@@')
    all_splits = text_splitter.split_text(text)
    docs = []
    for split in all_splits: 
        doc =  Document(page_content=split)
        docs.append(doc)
    vectorstore = Chroma.from_documents(documents=docs, embedding=OpenAIEmbeddings(api_key= OPENAI_API_KEY), persist_directory="./../../chroma_db")


