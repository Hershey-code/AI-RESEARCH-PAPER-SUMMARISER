import os
import fitz  # PyMuPDF
import ollama
from dotenv import load_dotenv

# Load .env (not necessary for Ollama unless you're storing something else)
load_dotenv()

# Extract text from uploaded PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Generate summary using Ollama (e.g., Mistral model)
def generate_summary(text):
    prompt = f"""Summarize the following academic research paper in a clear and concise way, covering objectives, methodology, and conclusion:

{text}

Summary:"""

    response = ollama.chat(
        model="tinyllama",  # or "llama3", "gemma", etc.
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response['message']['content']
