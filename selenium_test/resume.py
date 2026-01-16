from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def create_pdf():
    # File name
    filename = "Kavya_Resume.pdf"
    doc = SimpleDocTemplate(filename, pagesize=LETTER,
                            rightMargin=50, leftMargin=50,
                            topMargin=50, bottomMargin=50)

    styles = getSampleStyleSheet()
    
    # Custom Styles
    style_name = ParagraphStyle(name='Name', parent=styles['Heading1'], alignment=TA_CENTER, fontSize=16, spaceAfter=6)
    style_contact = ParagraphStyle(name='Contact', parent=styles['Normal'], alignment=TA_CENTER, fontSize=10, spaceAfter=20)
    style_section_head = ParagraphStyle(name='Section', parent=styles['Heading2'], fontSize=12, spaceAfter=6, spaceBefore=12,
                                        textColor=colors.black, borderPadding=0)
    style_job_title = ParagraphStyle(name='JobTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11, spaceAfter=2)
    style_company_date = ParagraphStyle(name='CompanyDate', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=10, spaceAfter=4)
    style_bullet = ParagraphStyle(name='Bullet', parent=styles['Normal'], fontSize=10, leftIndent=15, bulletIndent=5, spaceAfter=2)
    style_normal = ParagraphStyle(name='Body', parent=styles['Normal'], fontSize=10, spaceAfter=4)

    story = []

    # --- Header ---
    story.append(Paragraph("KAVYABAI R G", style_name))
    story.append(Paragraph("Bengaluru, India | kavyaadithi8787@gmail.com | 9740892694", style_contact))

    # --- Summary ---
    story.append(Paragraph("SUMMARY", style_section_head))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.lightgrey, spaceAfter=5))
    summary_text = ("Results-driven Python Developer with 2+ years of experience building scalable, cloud-integrated backend systems. Recently expanded expertise into Quality Assurance (QA) with hands-on experience in Manual and Automation Testing using Selenium and the Pytest framework. Skilled in FastAPI, Flask, Azure, and RESTful API development. Known for reducing latency, optimizing data flows, and integrating secure ingestion pipelines.")
    story.append(Paragraph(summary_text, style_normal))

    # --- Experience ---
    story.append(Paragraph("EXPERIENCE", style_section_head))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.lightgrey, spaceAfter=5))

    # Job 1: Zemoso
    story.append(Paragraph("Software Engineer", style_job_title))
    story.append(Paragraph("Zemoso Technologies | Dec 2025 – Present | Bengaluru, India", style_company_date))
    story.append(Paragraph("• Built robust automation scripts for an AI-driven project, ensuring model reliability and performance stability using Python.", style_bullet))
    story.append(Paragraph("• Implemented end-to-end (E2E) testing using Selenium, automating user interaction scenarios to reduce manual testing efforts.", style_bullet))
    story.append(Paragraph("• Designed comprehensive test suites utilizing the Pytest framework, achieving high code coverage and ensuring bug-free deployments for AI modules.", style_bullet))

    story.append(Spacer(1, 10))

    # Job 2: Cogniquest
    story.append(Paragraph("Software Engineer", style_job_title))
    story.append(Paragraph("Cogniquest.ai | Sep 2022 – May 2025 | Bengaluru, India", style_company_date))
    story.append(Paragraph("• Led Input Channel integration (Google Drive, Outlook); reduced latency by 30%.", style_bullet))
    story.append(Paragraph("• Developed RESTful APIs using FastAPI, improving data latency by 30%.", style_bullet))
    story.append(Paragraph("• Re-designed PostgreSQL/MongoDB schemas for secure, optimized access.", style_bullet))
    story.append(Paragraph("• Migrated Redis to disk caching; reduced memory usage by 60%.", style_bullet))
    story.append(Paragraph("• Integrated Azure Blob Storage for scalable document storage.", style_bullet))
    story.append(Paragraph("• Used BERT for extracting TOC and semantic structure.", style_bullet))

    # --- Projects ---
    story.append(Paragraph("PROJECTS", style_section_head))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.lightgrey, spaceAfter=5))

    # Project 1: Input Channel
    story.append(Paragraph("Input Channel", style_job_title))
    story.append(Paragraph("• Developed a secure and scalable ingestion pipeline to extract documents from Gmail, Outlook, and Google Drive, supporting formats like PDF, DOCX, and images.", style_bullet))
    story.append(Paragraph("• Integrated OAuth authentication, error handling, and content classification using Python and FastAPI.", style_bullet))
    story.append(Paragraph("• Led a team of 3 developers through agile sprints using Jira, ensuring timely and production-grade deliveries.", style_bullet))
    story.append(Paragraph("• Reduced ingestion latency by 30% and improved document traceability by optimizing PostgreSQL and MongoDB schemas.", style_bullet))

    story.append(Spacer(1, 6))

    # Project 2: CloudOptimal
    story.append(Paragraph("CloudOptimal", style_job_title))
    story.append(Paragraph("• Designed and implemented a real-time dashboard to visualize cloud usage metrics using FastAPI, asynchronous I/O, and Redis disk caching.", style_bullet))
    story.append(Paragraph("• Created REST APIs to aggregate and serve usage data from Azure and VM infrastructure.", style_bullet))
    story.append(Paragraph("• Collaborated with product stakeholders to define KPIs including CPU, memory, and bandwidth usage.", style_bullet))
    story.append(Paragraph("• Achieved 2x faster API responses through efficient caching mechanisms and asynchronous design.", style_bullet))

    story.append(Spacer(1, 6))

    # Project 3: MRT
    story.append(Paragraph("MRT", style_job_title))
    story.append(Paragraph("• Built a scalable NLP pipeline to extract Table of Contents (TOC) and semantic sections from enterprise documents using BERT models.", style_bullet))
    story.append(Paragraph("• Engineered a multi-stage architecture for parallel and reliable processing of large PDFs using FastAPI and Azure Blob Storage.", style_bullet))
    story.append(Paragraph("• Integrated semantic analysis to enhance document intelligence and indexing.", style_bullet))
    story.append(Paragraph("• Achieved over 90% TOC detection accuracy and improved overall processing throughput by 40%.", style_bullet))

    # --- Education ---
    story.append(Paragraph("EDUCATION", style_section_head))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.lightgrey, spaceAfter=5))
    
    story.append(Paragraph("Bachelor of Engineering - Computer Science", style_job_title))
    story.append(Paragraph("JSS Academy of Technical Education, Bengaluru | Sep 2019 – Dec 2023", style_company_date))
    
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Senior Secondary (AISSCE)", style_job_title))
    story.append(Paragraph("Jawahar Navodaya Vidyalaya, Bengaluru | Apr 2013 – Jul 2019", style_company_date))

    # --- Skills ---
    story.append(Paragraph("SKILLS", style_section_head))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.lightgrey, spaceAfter=5))
    
    # Corrected commas and formatting
    story.append(Paragraph("<b>Languages:</b> Python, JavaScript", style_normal))
    story.append(Paragraph("<b>Frameworks:</b> FastAPI, Flask, Django, Pytest, Selenium", style_normal))
    story.append(Paragraph("<b>Databases:</b> PostgreSQL, MySQL, MongoDB", style_normal))
    story.append(Paragraph("<b>Tools:</b> Git, Linux, GitHub Actions, Jira", style_normal))
    story.append(Paragraph("<b>Concepts:</b> OOP, REST APIs, Async I/O, Pandas, System Design, Caching Strategies, BERT", style_normal))

    # Build
    doc.build(story)
    print(f"PDF Generated Successfully: {filename}")

if __name__ == "__main__":
    create_pdf()