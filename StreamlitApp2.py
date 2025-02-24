import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model

def main():
    st.set_page_config(page_title="QA with Documents", layout="wide")

    st.title("📄 QA with Documents (Information Retrieval)")

    # Chat input box with file upload
    query_input = st.chat_input("Upload a document and ask your question...")
    
    # File uploader in sidebar (optional) or inside the chat bar
    doc = st.file_uploader("", type=["pdf", "txt", "docx"], label_visibility="collapsed")

    if query_input and doc:
        with st.spinner("Processing..."):
            document = load_data(doc)  # Load document
            model = load_model()  # Load LLM model
            query_engine = download_gemini_embedding(model, document)  # Embed document
            
            response = query_engine.query(query_input)  # Process query
            st.chat_message("assistant").write(response.response)  # Display response

if __name__ == "__main__":
    main()
