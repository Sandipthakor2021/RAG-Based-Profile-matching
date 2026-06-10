
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

class JobMatcher:
    def __init__(self,persist_dir="chroma_db"):
        self.db=Chroma(
            persist_directory=persist_dir,
            embedding_function=HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
        )

    def match(self, job_description, k=10):
        results=self.db.similarity_search_with_score(job_description,k=k)
        output={"job_description":job_description,"top_matches":[]}

        for doc,score in results:
            skills=doc.metadata.get("skills",[])

            output["top_matches"].append({
                "candidate_name":doc.metadata.get("name"),
                "resume_path":doc.metadata.get("resume_path"),
                "match_score":round(max(0,100-(score*10)),2),
                "matched_skills":skills,
                "relevant_excerpts":[doc.page_content[:300]],
                "reasoning":"Semantic similarity and skill overlap."
            })
        return output
