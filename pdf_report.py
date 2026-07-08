from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def generate_pdf(
    patient_name,
    age,
    gender,
    diagnosis,
    confidence,
    filename
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Medical Diagnosis Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Patient Name: {patient_name}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Age: {age}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Gender: {gender}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Diagnosis: {diagnosis}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Confidence: {confidence:.2f}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Generated On: {datetime.now()}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    if diagnosis == "Pneumonia":

        recommendation = """
        Recommendations:
        • Consult a physician
        • Take prescribed medications
        • Stay hydrated
        • Get adequate rest
        """

    else:

        recommendation = """
        Recommendations:
        • Maintain healthy lifestyle
        • Exercise regularly
        • Schedule routine checkups
        """

    content.append(
        Paragraph(
            recommendation,
            styles["Normal"]
        )
    )

    doc.build(content)
    