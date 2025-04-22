from employee_feedback_generator import EmployeeFeedbackGenerator
from organization_feedback_generator import OrganizationFeedbackGenerator
from unified_feedback_generator import UnifiedFeedbackGenerator
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT
from utils.scoring import calculate_employee_score, calculate_organization_score
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.lib.colors import black
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib import fonts
import re

def load_questionnaire(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_user_responses(questionnaire):
    responses = {}
    for item in questionnaire['questions']:
        if 'category' in item:
            print(f"\nCategory: {item['category']}")
        if 'questions' in item:
            for question in item['questions']:
                print(f"\n{question['question']}")
                for idx, answer in enumerate(question['answers']):
                    print(f"{idx + 1}. {answer['option']}")
                while True:
                    try:
                        response = int(input("Select an option (1-5): ")) - 1
                        if 0 <= response < len(question['answers']):
                            responses[question['question']] = question['answers'][response]['score']
                            break
                        else:
                            print("Invalid choice. Please select a valid option.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 5.")
        else:
            print(f"\n{item['question']}")
            for idx, answer in enumerate(item['answers']):
                print(f"{idx + 1}. {answer['text']}")
            while True:
                try:
                    response = int(input("Select an option (1-5): ")) - 1
                    if 0 <= response < len(item['answers']):
                        responses[item['question']] = item['answers'][response]['value']
                        break
                    else:
                        print("Invalid choice. Please select a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 5.")
    return responses

def format_bullet(text, style):
    """
    Converts a Markdown-style bullet point into a formatted Paragraph with:
    - Bold label at the start (e.g., "Access Control:")
    - Bold inline phrases using **like this**
    """
    # Remove leading * or - or whitespace
    text = text.strip()
    if text.startswith("*") or text.startswith("-"):
        text = text[1:].strip()

    # Bold label before colon
    if ':' in text:
        parts = text.split(":", 1)
        label = f'<b>{parts[0]}:</b>'
        remainder = parts[1].strip()
        text = f'{label} {remainder}'

    # Convert **bold** markdown to HTML <b> for ReportLab
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)

    return Paragraph(f'• {text}', style)

def save_feedback_to_pdf(feedback_text, title, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    elements = []

    # Define styles for different heading levels
    title_style = ParagraphStyle(name='TitleStyle', 
                                fontSize=18, 
                                leading=24, 
                                alignment=TA_LEFT, 
                                spaceAfter=12, 
                                fontName='Helvetica-Bold')
    
    h1_style = ParagraphStyle(name='H1Style',
                            fontSize=16,
                            leading=20,
                            spaceAfter=10,
                            fontName='Helvetica-Bold',
                            textColor=black)
    
    h2_style = ParagraphStyle(name='H2Style',
                            fontSize=14,
                            leading=18,
                            spaceAfter=8,
                            fontName='Helvetica-Bold',
                            textColor=black)
    
    h3_style = ParagraphStyle(name='H3Style',
                            fontSize=12,
                            leading=16,
                            spaceAfter=6,
                            fontName='Helvetica-Bold',
                            textColor=black)
    
    bullet_style = ParagraphStyle(name='BulletStyle',
                                fontSize=11,
                                leading=16,
                                leftIndent=20,
                                spaceAfter=6,
                                fontName='Helvetica')
    
    body_style = ParagraphStyle(name='BodyStyle',
                              fontSize=11,
                              leading=16,
                              spaceAfter=10,
                              fontName='Helvetica')

    # Add main title
    elements.append(Paragraph(title, title_style))
    elements.append(Spacer(1, 12))

    # Process feedback content
    lines = feedback_text.split('\n')
    
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue

        # Handle different header levels
        if stripped_line.startswith('# '):
            # H1: Main section (e.g., "# Cybersecurity Assessment Feedback")
            header_text = stripped_line[2:].strip()
            elements.append(Paragraph(header_text, h1_style))
            elements.append(HRFlowable(width="100%", thickness=0.5, color=black))
            elements.append(Spacer(1, 12))
            
        elif stripped_line.startswith('## '):
            # H2: Subsection (e.g., "## What You're Doing Well")
            header_text = stripped_line[3:].strip()
            elements.append(Paragraph(header_text, h2_style))
            elements.append(HRFlowable(width="100%", thickness=0.5, color=black))
            elements.append(Spacer(1, 8))
            
        elif stripped_line.startswith('### '):
            # H3: Sub-subsection (e.g., "### Access Control")
            header_text = stripped_line[4:].strip()
            elements.append(Paragraph(header_text, h3_style))
            elements.append(Spacer(1, 6))
            
        elif stripped_line.startswith('- '):
            # Bullet points
            bullet_text = stripped_line[2:].strip()
            formatted_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', bullet_text)
            elements.append(Paragraph(f'• {formatted_text}', bullet_style))
            elements.append(Spacer(1, 4))
            
        else:
            # Body text with optional bold formatting
            formatted_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', stripped_line)
            elements.append(Paragraph(formatted_text, body_style))
            elements.append(Spacer(1, 6))

    doc.build(elements)

def main():
    # Load the questionnaires
    employee_questionnaire = load_questionnaire('src/data/employee_questionnaire.json')
    organization_questionnaire = load_questionnaire('src/data/organization_questionnaire.json')

    # Get user responses
    print("Employee Questionnaire:")
    employee_responses = get_user_responses(employee_questionnaire)
    print("\nOrganization Questionnaire:")
    organization_responses = get_user_responses(organization_questionnaire)

    # Initialize the feedback generators
    employee_feedback_generator = EmployeeFeedbackGenerator(employee_responses)
    organization_feedback_generator = OrganizationFeedbackGenerator(organization_responses)

    # Generate feedback for employee questionnaire
    employee_feedback = employee_feedback_generator.generate_feedback()
    print("\nEmployee Feedback:")
    print(employee_feedback)

    # Generate feedback for organization questionnaire
    organization_feedback = organization_feedback_generator.generate_feedback()
    print("\nOrganization Feedback:")
    print(organization_feedback)

    # Calculate scores for unified feedback
    org_score = calculate_organization_score(organization_responses)
    emp_score = calculate_employee_score(employee_responses)
    unified_feedback_generator = UnifiedFeedbackGenerator(org_score, emp_score)

    # Generate unified feedback
    unified_feedback = unified_feedback_generator.generate_feedback()
    print("\nUnified Feedback:")
    print(unified_feedback)

    # Save feedback to separate PDFs
    save_feedback_to_pdf(employee_feedback, "Employee Feedback", "employee_feedback_report.pdf")
    save_feedback_to_pdf(organization_feedback, "Organization Feedback", "organization_feedback_report.pdf")
    save_feedback_to_pdf(unified_feedback, "Unified Feedback", "unified_feedback_report.pdf")

if __name__ == "__main__":
    main()