from openai import OpenAI
import speech_recognition as sr
from voice_to_text import listen_mic_text
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA
from pathlib import Path
from openai import OpenAI
import pygame
import io
import warnings
from langchain.prompts import PromptTemplate

warnings.filterwarnings("ignore", category=DeprecationWarning)


OPENAI_API_KEY = '<KEY>'
client = OpenAI(api_key=OPENAI_API_KEY)

def play_audio(content):
    pygame.init()
    speech_data = io.BytesIO(content)
    pygame.mixer.music.load(speech_data)
    pygame.mixer.init()
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    

def text_to_speech(input_text):
    response = client.audio.speech.create(model="tts-1",voice="alloy", input=input_text)
    play_audio(response.content)


def run_qa_answer():
    question = listen_mic_text()
    vectorstore = Chroma(persist_directory='./chroma_db', embedding_function=OpenAIEmbeddings(api_key= OPENAI_API_KEY))
    llm = ChatOpenAI(model_name="gpt-4-0125-preview", temperature=0, api_key = OPENAI_API_KEY)
    prompt_template = """Use the following pieces of context to answer the question at the end. 
        If you don't know the answer, please say I don't know

        {context}

        Question: {question}
        """
    prompt = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
    )

    chain_type_kwargs = {"prompt": prompt}


    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectorstore.as_retriever(), chain_type_kwargs=chain_type_kwargs)
    result = qa_chain({"query": question})
    print(result["result"])
    text = result["result"]
    text_to_speech(str(text))

run_qa_answer()

