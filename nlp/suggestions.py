def generate_suggestions(missing_skills, score):

    suggestions = []

    if score >= 80:
        suggestions.append("Excellent resume! Keep it updated.")
        suggestions.append("Add recent certifications.")
        suggestions.append("Include measurable achievements.")

    elif score >= 60:
        suggestions.append("Your resume is good but can be improved.")
        suggestions.append("Add more technical projects.")
        suggestions.append("Mention your internships clearly.")

    else:
        suggestions.append("Improve your resume by adding missing skills.")
        suggestions.append("Customize your resume for each job.")
        suggestions.append("Add certifications and projects.")

    if len(missing_skills) > 0:
        suggestions.append(
            "Missing Skills: " + ", ".join(missing_skills)
        )

    return suggestions