\# 🤖 Smart Resume Screening Powered by NLP \& Machine Learning



An AI-powered web application that analyzes resumes against job descriptions and provides an ATS-style score, skill analysis, resume strength evaluation, and personalized improvement suggestions.



\## 📌 About the Project



\*\*Smart Resume Screening\*\* is a Flask-based web application designed to simplify the initial resume screening process.



The system allows users to upload a resume and provide a job description. It analyzes the resume content using Natural Language Processing techniques, compares relevant skills with the job requirements, calculates an ATS Match Score, identifies matched and missing skills, and provides suggestions for improving the resume.



\## ✨ Key Features



\* 📄 Resume PDF Upload

\* 📝 Job Description Analysis

\* 🤖 NLP-based Resume Analysis

\* 🎯 ATS Match Score

\* ✅ Matched Skills Detection

\* ❌ Missing Skills Detection

\* 📊 Resume Strength Analysis

\* 💡 Personalized Resume Suggestions

\* 📑 PDF Report Generation

\* 🔐 User Registration and Login

\* 🗄️ SQLite Database

\* 🌐 Flask Web Application



\## 🛠️ Technologies Used



| Category             | Technologies                |

| -------------------- | --------------------------- |

| Programming Language | Python                      |

| Backend              | Flask                       |

| NLP                  | Natural Language Processing |

| Frontend             | HTML, CSS, JavaScript       |

| Database             | SQLite                      |

| PDF Processing       | PyPDF2                      |

| Authentication       | Werkzeug Security           |

| Version Control      | Git \& GitHub                |



\## ⚙️ How It Works



```text

User

&#x20; ↓

Register / Login

&#x20; ↓

Upload Resume

&#x20; ↓

Enter Job Description

&#x20; ↓

Extract Resume Text

&#x20; ↓

NLP Processing

&#x20; ↓

Skill Matching

&#x20; ↓

ATS Score Calculation

&#x20; ↓

Resume Strength Analysis

&#x20; ↓

Personalized Suggestions

&#x20; ↓

Generate PDF Report

```



\## 📂 Project Structure



```text

smart-resume-screening/

│

├── ats/

│   └── ATS-related modules

│

├── models/

│   └── Model-related files

│

├── nlp/

│   └── NLP and skill matching modules

│

├── reports/

│   └── Generated reports

│

├── static/

│   ├── charts/

│   ├── result.css

│   └── style.css

│

├── templates/

│   ├── login.html

│   ├── register.html

│   └── application templates

│

├── uploads/

│   └── Uploaded resume files

│

├── utils/

│   └── Utility modules

│

├── app.py

├── database.py

├── requirements.txt

└── README.md

```



\## 🚀 Installation \& Setup



\### 1. Clone the Repository



```bash

git clone https://github.com/rajamgariprathyusha-svg/smart-resume-screening.git

```



\### 2. Open the Project



```bash

cd smart-resume-screening

```



\### 3. Create a Virtual Environment



```bash

python -m venv venv

```



\### 4. Install Dependencies



```bash

python -m pip install -r requirements.txt

```



\### 5. Run the Application



```bash

python app.py

```



\### 6. Open in Browser



```text

http://127.0.0.1:5000

```



\## 📊 Output



The application provides:



\* ATS Match Score

\* Matched Skills

\* Missing Skills

\* Resume Strength

\* Personalized Suggestions

\* Resume Analysis Report



\## 🎯 Project Objectives



\* Automate the initial resume screening process.

\* Compare resumes with job descriptions.

\* Identify relevant and missing skills.

\* Calculate an ATS-style compatibility score.

\* Provide actionable resume improvement suggestions.

\* Reduce manual effort during preliminary resume screening.



\## 🔮 Future Enhancements



\* Advanced transformer-based NLP models

\* Semantic skill matching

\* Resume ranking system

\* Job recommendation system

\* Recruiter dashboard

\* Multiple resume comparison

\* Cloud deployment

\* Support for additional document formats

\* Integration with job portals



\## 👩‍💻 Developer



\*\*Prathyusha Rajamgari\*\*



\*\*Bachelor of Science – Computer Science\*\*



K.L.M College of Engineering for Women



GitHub: \[rajamgariprathyusha-svg](https://github.com/rajamgariprathyusha-svg)



\## ⭐ Support



If you find this project useful, consider giving the repository a ⭐ on GitHub.



