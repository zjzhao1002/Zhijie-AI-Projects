import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI


def run_pdf_rag(question):
    file_path = "./data/"
    dir_list = os.listdir(file_path)

    pdf_files = []
    for f in dir_list:
        if "pdf" in f:
            pdf_files.append(os.path.join(file_path, f))

    text = ""
    for pdf in pdf_files:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap =200)
    chunks = text_splitter.split_text(text=text)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(texts=chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

    prompt_template = """
    You are an assistant for question-answering tasks. 
    Use the following pieces of retrieved context to answer the question. 
    If you do not know the answer, just say "answer is not available in this context". 
    Do not provide wrong answer.
    Use three sentences maximum and keep the answer concise.\n
    Context: {context}\n
    Question: {question}\n
    Answer: 
    """

    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    chain = prompt | model

    context = vector_store.similarity_search(question)
    response = chain.invoke({"context": context, "question": question})
    return response.content