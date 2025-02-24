import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model

def main():
    st.set_page_config(page_title="QA with Documents", layout="wide")

    st.title("📄 QA with Documents (Information Retrieval)")

    # Add the sparkle cursor effect using HTML & JavaScript
    sparkle_effect = """
    <style>
    body { cursor: none; } /* Hide default cursor */
    .sparkle {
        position: fixed;
        width: 8px;
        height: 8px;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 50%;
        pointer-events: none;
        animation: fadeOut 0.5s linear forwards;
    }
    @keyframes fadeOut {
        0% { transform: scale(1); opacity: 1; }
        100% { transform: scale(3); opacity: 0; }
    }
    </style>

    <script>
    document.addEventListener("mousemove", function(e) {
        var sparkle = document.createElement("div");
        sparkle.className = "sparkle";
        sparkle.style.left = `${e.pageX}px`;
        sparkle.style.top = `${e.pageY}px`;
        sparkle.style.backgroundColor = `hsl(${Math.random() * 360}, 100%, 80%)`; // Random colors
        document.body.appendChild(sparkle);
        
        setTimeout(() => sparkle.remove(), 500); // Remove after animation
    });
    </script>
    """
    st.markdown(sparkle_effect, unsafe_allow_html=True)  # Add the sparkle effect

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
