
from src.resume_rag import ResumeRAG
from src.job_matcher import JobMatcher

ResumeRAG().build()

jd="""Python Developer with 5+ years experience,
AWS, Docker, SQL"""
matcher=JobMatcher()
print(matcher.match(jd))
