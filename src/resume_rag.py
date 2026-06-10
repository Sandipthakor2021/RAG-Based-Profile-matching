
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from src.document_loader import load_resume
from src.metadata_extractor import extract_metadata

class ResumeRAG:
    def __init__(self, resume_dir="data/resumes", persist_dir="chroma_db"):
        self.resume_dir=resume_dir
        self.persist_dir=persist_dir
        self.embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    def build(self):
        docs=[]
        for f in Path(self.resume_dir).glob("*"):
            loaded=load_resume(str(f))
            for d in loaded:
                md=extract_metadata(d.page_content)
                d.metadata.update(md)
                d.metadata["resume_path"]=str(f)
                docs.append(d)

        splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
        chunks=splitter.split_documents(docs)

        db=Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.persist_dir
        )
        return db
