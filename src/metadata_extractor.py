
import re

SKILLS = ["Python","Java","Spring Boot","AWS","Docker","Kubernetes","React","SQL","Machine Learning"]

def extract_metadata(text):
    skills=[s for s in SKILLS if s.lower() in text.lower()]
    exp=0
    m=re.search(r"(\d+)\+?\s*years", text,re.I)
    if m: exp=int(m.group(1))
    lines=[l.strip() for l in text.splitlines() if l.strip()]
    return {
        "name": lines[0] if lines else "Unknown",
        "skills": skills,
        "experience_years": exp,
        "education": "Detected from resume"
    }
