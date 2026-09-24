def calculate_ats_score(matched_skills, job_skills):
    """
    Calculate ATS Match Score, Rating and Status.
    """

    # Avoid division by zero
    total_skills = len(job_skills)

    if total_skills == 0:
        score = 0
    else:
        score = round((len(matched_skills) / total_skills) * 100, 2)

    # Resume Rating
    if score >= 80:
        rating = "⭐⭐⭐⭐⭐"
        status = "Excellent Resume"
    elif score >= 60:
        rating = "⭐⭐⭐⭐"
        status = "Good Resume"
    elif score >= 40:
        rating = "⭐⭐⭐"
        status = "Average Resume"
    else:
        rating = "⭐⭐"
        status = "Needs Improvement"

    return score, rating, status