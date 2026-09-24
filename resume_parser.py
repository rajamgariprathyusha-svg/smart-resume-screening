from PyPDF2 import PdfReader

def extract_resume_text(pdf_path):
    """
    Extract text from the uploaded resume PDF.
    """

    reader = PdfReader(pdf_path)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    return resume_text