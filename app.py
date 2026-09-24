from flask import Flask, render_template, request, redirect, session, send_file
import sqlite3
import os
from database import (
    create_table,
    register_user,
    login_user,
    check_email,
    update_password
)

from resume_parser import extract_resume_text
from candidate_info import extract_candidate_info
from nlp.skill_matcher import compare_skills
from nlp.ats_score import calculate_ats_score
from nlp.resume_strength import analyze_resume_strength
from nlp.suggestions import generate_suggestions
from chart import create_skill_chart
from pdf_report import create_pdf_report


# -----------------------------------
# Flask App
# -----------------------------------

app = Flask(__name__)

app.secret_key = "resume_ai_secret_key"


# -----------------------------------
# Configuration
# -----------------------------------

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

create_table()

latest_report = {}


# -----------------------------------
# Home Page
# -----------------------------------

@app.route("/")
def home():

    if "username" not in session:
        return redirect("/login")

    return render_template(
        "index.html",
        username=session["username"]
    )


# -----------------------------------
# Register
# -----------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        success = register_user(
            username,
            email,
            password
        )

        if success:
            return redirect("/login")

        else:
            return "Email already registered"

    return render_template("register.html")


# -----------------------------------
# Normal Login
# -----------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = login_user(
            email,
            password
        )

        if user:

            session["username"] = user[0]
            session["email"] = email

            return redirect("/")

        else:
            return "Invalid Email or Password"

    return render_template("login.html")
@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form["email"]

        user = check_email(email)

        if user:

            return render_template(
                "reset_password.html",
                email=email
            )

        else:

            return render_template(
                "forgot_password.html",
                error="Email not found!"
            )

    return render_template("forgot_password.html")
@app.route("/reset_password", methods=["POST"])
def reset_password():

    email = request.form["email"]

    password = request.form["password"]

    confirm = request.form["confirm_password"]

    if password != confirm:

        return render_template(
            "reset_password.html",
            email=email,
            error="Passwords do not match!"
        )

    update_password(email, password)

    return redirect("/login")
@app.route("/welcome")
def welcome():

    if "username" not in session:
        return redirect("/login")

    return render_template(
        "welcome.html",
        username=session["username"]
    )

# -----------------------------------
# Google Login
# -----------------------------------

@app.route("/login/google")
def login_google():

    return "Google Login button is working!"


# -----------------------------------
# GitHub Login
# -----------------------------------

@app.route("/login/github")
def login_github():

    return "GitHub Login button is working!"


# -----------------------------------
# Resume Analysis
# -----------------------------------

@app.route("/analyze", methods=["POST"])
def analyze_resume():

    global latest_report

    print("request.files =", request.files)
    print("request.form =", request.form)

    if "resume" not in request.files:
        return "Resume file not found."

    resume = request.files["resume"]

    print("Resume filename:", resume.filename)

    # Save Resume
    resume_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    resume.save(resume_path)

    # Extract Resume Text
    resume_text = extract_resume_text(resume_path)

    # -----------------------------------
    # Job Description
    # -----------------------------------

    job_text = ""

    if "job_description" in request.files:

        job_description = request.files["job_description"]

        if job_description.filename != "":

            job_path = os.path.join(
                app.config["UPLOAD_FOLDER"],
                job_description.filename
            )

            job_description.save(job_path)

            try:

                with open(
                    job_path,
                    "r",
                    encoding="utf-8"
                ) as file:

                    job_text = file.read()

            except UnicodeDecodeError:

                with open(
                    job_path,
                    "r",
                    encoding="cp1252"
                ) as file:

                    job_text = file.read()

    # -----------------------------------
    # Candidate Information
    # -----------------------------------

    candidate = extract_candidate_info(
        resume_text
    )

    # -----------------------------------
    # Skill Matching
    # -----------------------------------

    matched_skills, missing_skills, job_skills = compare_skills(
        resume_text,
        job_text
    )

    create_skill_chart(
        matched_skills,
        missing_skills
    )

    # -----------------------------------
    # ATS Score
    # -----------------------------------

    score, rating, status = calculate_ats_score(
        matched_skills,
        job_skills
    )

    print("\n========== Candidate Details ==========")
    print(candidate)

    print("\nMatched Skills")
    print(matched_skills)

    print("\nMissing Skills")
    print(missing_skills)

    print("\nATS Score:", score)
    print("Rating:", rating)
    print("Status:", status)

    # -----------------------------------
    # Suggestions
    # -----------------------------------

    suggestions = []

    if len(missing_skills) > 0:

        for skill in missing_skills:

            suggestions.append(
                f"Learn {skill} to improve your ATS score."
            )

    else:

        suggestions.append(
            "Excellent! Your resume matches the job description very well."
        )

    # -----------------------------------
    # Resume Strength
    # -----------------------------------

    strength = {

        "Matched Skills": len(matched_skills),

        "Missing Skills": len(missing_skills),

        "Resume Rating": rating,

        "Resume Status": status,

        "ATS Score": f"{score}%"
    }

    # -----------------------------------
    # Save Latest Report
    # -----------------------------------

    latest_report = {

        "candidate": candidate,

        "score": score,

        "rating": rating,

        "status": status,

        "matched": matched_skills,

        "missing": missing_skills,

        "suggestions": suggestions
    }

    # -----------------------------------
    # Result Page
    # -----------------------------------

    return render_template(
        "result.html",

        candidate=candidate,

        matched=matched_skills,

        missing=missing_skills,

        score=score,

        rating=rating,

        status=status,

        suggestions=suggestions,

        strength=strength
    )


# -----------------------------------
# Download Report
# -----------------------------------

@app.route("/download_report")
def download_report():

    pdf_path = "reports/resume_analysis_report.pdf"

    create_pdf_report(

        pdf_path,

        latest_report["candidate"],

        latest_report["score"],

        latest_report["rating"],

        latest_report["status"],

        latest_report["matched"],

        latest_report["missing"],

        latest_report["suggestions"]
    )

    return send_file(
        pdf_path,
        as_attachment=True
    )


# -----------------------------------
# Run Application
# -----------------------------------

if __name__ == "__main__":
    app.run(debug=True)