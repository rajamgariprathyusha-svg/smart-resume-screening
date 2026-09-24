import re

def analyze_resume_strength(text):

    result = {}

    text = text.lower()

    result["Personal Information"] = (
        "Complete"
        if re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
        else "Missing"
    )

    result["Skills"] = (
        "Complete"
        if "skills" in text
        else "Missing"
    )

    result["Projects"] = (
        "Complete"
        if "project" in text
        else "Needs Improvement"
    )

    result["Education"] = (
        "Complete"
        if "education" in text
        else "Missing"
    )

    result["Certifications"] = (
        "Complete"
        if "certification" in text or "certificate" in text
        else "Missing"
    )

    return result