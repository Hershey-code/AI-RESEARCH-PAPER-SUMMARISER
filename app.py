import streamlit as st
from summarizer import extract_text_from_pdf, generate_summary

st.set_page_config(page_title="AI Research Paper Summariser", layout="centered")

st.title("📄 AI-Based Research Paper Summariser (Powered by Ollama)")
st.write("Upload a research paper (PDF) and get an AI-generated summary using a local LLM via Ollama.")

uploaded_file = st.file_uploader("Upload your academic research paper (PDF)", type="pdf")

if uploaded_file:
    with st.spinner("🔍 Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)

    st.subheader("📝 Preview of Extracted Text:")
    st.code(text[:1000] + "...", language="text")
  # Show first 1000 characters

    if st.button("Generate Summary"):
        with st.spinner("🤖 Generating summary using Ollama..."):
            try:
                summary = generate_summary(text[:4000])  # Trim if too long
                st.subheader("📚 Summary:")
                st.write(summary)
            except Exception as e:
                st.error(f"⚠️ Failed to generate summary using Ollama.\n\nDetails: {str(e)}")
