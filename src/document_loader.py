
from langchain_community.document_loaders import TextLoader, PyPDFLoader

def load_resume(path):
    if path.endswith(".pdf"):
        return PyPDFLoader(path).load()
    return TextLoader(path).load()
