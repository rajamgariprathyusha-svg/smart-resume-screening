import re

# Master Skills List
SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Node.js",
    "SQL",
    "MongoDB",
    "Flask",
    "Git",
    "Machine Learning",
    "Deep Learning",
    "AI",
    "Django",
    "Docker",
    "AWS",
    "Power BI",
    "Excel"
]


def extract_skills(text):
    """
    Extract skills from resume/job description.
    """

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))


def compare_skills(resume_text, job_text):

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_text)

    matched = []

    missing = []

    for skill in job_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing, job_skills