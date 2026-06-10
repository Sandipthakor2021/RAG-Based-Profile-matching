# Resume RAG System - AI-Powered Job Matching Engine

## Overview

The Resume RAG System is an AI-powered recruitment solution that leverages Retrieval-Augmented Generation (RAG), Vector Databases, Semantic Search, and Embedding Models to intelligently match candidate resumes with job descriptions.

Traditional keyword-based recruitment systems often fail to identify suitable candidates when resumes and job descriptions use different terminology. This project addresses that challenge by implementing semantic understanding through embeddings and vector search.

The system processes resumes, extracts meaningful metadata, generates embeddings, stores them in a vector database, and retrieves the most relevant candidates for a given job description.

---

## Features

### Document Processing Pipeline

* Resume ingestion from PDF and TXT files
* Intelligent document chunking
* Section-aware processing (Skills, Experience, Education)
* Metadata extraction
* Embedding generation using HuggingFace models
* Vector storage using ChromaDB

### Metadata Extraction

The system automatically extracts:

* Candidate Name
* Technical Skills
* Years of Experience
* Education Details
* Resume Source Path

### Semantic Search

* Job Description Embedding Generation
* Similarity Search
* Top-K Candidate Retrieval
* Semantic Matching Beyond Keywords

### Hybrid Search

Combines:

* Semantic Similarity Search
* Keyword-Based Filtering
* Skill Matching

This improves retrieval accuracy compared to purely semantic approaches.

### Ranking & Scoring

Candidates are ranked based on:

* Semantic Similarity
* Skill Overlap
* Experience Match
* Education Relevance

Scores are generated on a scale of 0–100.

### Match Explanation

For each candidate, the system provides:

* Matching Skills
* Relevant Resume Excerpts
* Score Breakdown
* Selection Reasoning

---

## System Architecture

```text
Job Description
       │
       ▼
Embedding Model
       │
       ▼
Vector Search
       │
       ▼
ChromaDB
       │
       ▼
Top-K Resume Retrieval
       │
       ▼
Hybrid Ranking Engine
       │
       ▼
Final Candidate Recommendations
```

---

## Technology Stack

### Programming Language

* Python 3.10+

### AI & NLP

* LangChain
* HuggingFace Sentence Transformers

### Vector Database

* ChromaDB

### Data Processing

* Pandas
* NumPy

### Document Handling

* PyPDF
* Text Loaders

---

## Project Structure

```text
resume-rag-system/
│
├── data/
│   ├── resumes/
│   └── job_descriptions/
│
├── src/
│   ├── resume_rag.py
│   ├── job_matcher.py
│   ├── metadata_extractor.py
│   ├── document_loader.py
│   └── config.py
│
├── notebooks/
│   └── rag_experiments.ipynb
│
├── chroma_db/
│
├── requirements.txt
│
├── demo.py
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd resume-rag-system
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

### Activate Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Dataset

### Resumes

The system uses 30+ resumes from multiple domains:

* Python Developers
* Java Developers
* Data Scientists
* DevOps Engineers
* Frontend Developers
* Full Stack Developers
* QA Engineers
* Cloud Engineers
* Machine Learning Engineers
* Business Analysts

### Job Descriptions

Included roles:

* Python Developer
* Java Backend Developer
* Data Scientist
* DevOps Engineer
* React Developer

---

## Running the Project

### Build Vector Database

```bash
python3 demo.py
```

This will:

1. Load resumes
2. Extract metadata
3. Generate embeddings
4. Build ChromaDB vector store

### Run Job Matching

Provide a job description and retrieve the best candidates.

Example:

```python
jd = """
Python Developer

Requirements:
- Python
- AWS
- Docker
- SQL
- 5+ Years Experience
"""
```

---

## Sample Output

```json
{
  "job_description": "Python Developer",
  "top_matches": [
    {
      "candidate_name": "John Doe",
      "resume_path": "data/resumes/john_doe.pdf",
      "match_score": 92,
      "matched_skills": [
        "Python",
        "AWS",
        "Docker"
      ],
      "relevant_excerpts": [
        "5 years of experience in backend development..."
      ],
      "reasoning": "Strong experience in Python backend systems and cloud deployment."
    }
  ]
}
```

---

## Performance Metrics

The project evaluates:

### Retrieval Metrics

* Precision@K
* Recall@K
* Top-K Accuracy

### System Metrics

* Embedding Generation Time
* Query Latency
* Average Retrieval Time

### Ranking Metrics

* Match Score Distribution
* Candidate Relevance Analysis

---

## Experimentation

The Jupyter Notebook includes experiments for:

### Chunk Size Analysis

* 256
* 512
* 1024

### Embedding Model Comparison

* all-MiniLM-L6-v2
* BGE Small
* E5 Base

### Top-K Retrieval Analysis

* K=5
* K=10
* K=20

---

## Future Enhancements

* LLM-powered candidate summaries
* Resume parsing using Named Entity Recognition
* Experience timeline extraction
* Multi-language resume support
* Pinecone Integration
* Weaviate Integration
* Streamlit Dashboard
* Recruiter Analytics Dashboard
* Interview Question Generation
* Candidate Recommendation Engine

---

## Learning Outcomes

This project demonstrates practical implementation of:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Embedding Models
* Information Retrieval
* Metadata Filtering
* AI-Powered Recruitment Systems

---


## License

This project is developed for educational and research purposes.
