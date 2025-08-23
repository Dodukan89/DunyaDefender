import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
import asyncio
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

load_dotenv()


# Botun ismi
st.title("İklim Âlimi Chatbot")

# PDF dosyasını yükleme ve metinleri bölme
file_path = "bilgi.pdf" 
loader = PyPDFLoader(file_path)
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter( chunk_size=1000)
docs = text_splitter.split_documents(data)

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vector_store=Chroma.from_documents(embedding=embeddings, documents=docs, persist_directory="./chroma_db")
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 10})

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.3,
    max_tokens=512,

)

# Chatbot input
st.markdown("### Cevabın burda olucak:")
query = st.chat_input("Huzuruma hoş geldin evlat, iklim değişikliği hakkında ne öğrenmek istersin?")

system_prompt = (
    "Sen, iklim değişikliği hakkında bilgi sağlayan yardımcı bir asistansın. "
    "Sana bazı belgeler verilecek ve kullanıcının sorusunu bu belgeler temelinde cevaplayacaksın. "
    "Cevabı bilmiyorsan 'Bilmiyorum' diyeceksin. "
    "Eğer cevap belgelerde yoksa 'Bilmiyorum' diyeceksin. "
    "Eğer cevap belgelerde varsa, bunu detaylı şekilde açıklayacaksın. "
    "Cevaplar olabildiğince uzun olsun ve net ol. "
    "Belgelerden gelen bilgileri kullanabilirsin.\n\n"
    "Belgeleri kullanırken, konu başlıklarına bakarak soruyu daha iyi anlamaya çalış. "
    "Cevaplarını oluştururken, belgelerdeki bilgileri kullanarak soruyu detaylı bir şekilde yanıtla. "
    "Eğer cevabı bulamıyorsan, irternet üzerinden araştırma yapabilirsin. "
    "Belgeler: {context}"
)


if query:
    prompt=ChatPromptTemplate.from_messages(
    [
    ("system",system_prompt),
    ("human","{input}")
    ]
)
    chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, chain)
    response = retrieval_chain.invoke({"input": query})
    st.write(response["answer"])