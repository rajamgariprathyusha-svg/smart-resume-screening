import re

def extract_candidate_info(text):
    info = {}

    # Email
    email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    info["email"] = email[0] if email else "Not Found"

    # Phone Number
    phone = re.findall(r'\b\d{10}\b', text)
    info["phone"] = phone[0] if phone else "Not Found"

    # Name (First line of resume)
    lines = text.split("\n")
    info["name"] = lines[0].strip() if lines else "Unknown"

    return info