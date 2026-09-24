from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(
        filename,
        candidate,
        score,
        rating,
        status,
        matched,
        missing,
        suggestions):

    pdf = SimpleDocTemplate(filename, pagesize=letter)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph("AI Resume Screening Report", styles["Title"])
    )

    content.append(Spacer(1, 20))


    content.append(
        Paragraph(
            f"Name: {candidate.get('name','N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Email: {candidate.get('email','N/A')}",
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            f"ATS Score: {score}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Rating: {rating}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Status: {status}",
            styles["Normal"]
        )
    )


    content.append(Spacer(1,15))


    content.append(
        Paragraph(
            "Matched Skills:",
            styles["Heading3"]
        )
    )

    content.append(
        Paragraph(
            ", ".join(matched),
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            "Missing Skills:",
            styles["Heading3"]
        )
    )

    content.append(
        Paragraph(
            ", ".join(missing),
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            "AI Suggestions:",
            styles["Heading3"]
        )
    )


    for item in suggestions:
        content.append(
            Paragraph(
                "• " + item,
                styles["Normal"]
            )
        )


    pdf.build(content)