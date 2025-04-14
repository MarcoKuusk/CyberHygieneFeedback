from employee_feedback_generator import EmployeeFeedbackGenerator
from organization_feedback_generator import OrganizationFeedbackGenerator
from unified_feedback_generator import UnifiedFeedbackGenerator
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT
from utils.scoring import calculate_employee_score, calculate_organization_score

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
                response = int(input("Select an option (1-5): ")) - 1
                responses[question['question']] = question['answers'][response]['score']
        else:
            print(f"\n{item['question']}")
            for idx, answer in enumerate(item['answers']):
                print(f"{idx + 1}. {answer['text']}")
            response = int(input("Select an option (1-5): ")) - 1
            responses[item['question']] = item['answers'][response]['value']
    return responses

def save_feedback_to_pdf(feedback_list, title, file_path):
    """
    Saves the feedback to a PDF file with basic formatting.
    """
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    margin = 40
    y = height - margin

    # Draw the title
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y, title)
    y -= 20  # Space after the title

    # Draw the feedback
    c.setFont("Helvetica", 12)
    for feedback in feedback_list:
        lines = feedback.split("\n")  # Split feedback into lines if needed
        for line in lines:
            if y < margin:  # Check if we need a new page
                c.showPage()
                y = height - margin
                c.setFont("Helvetica", 12)
            c.drawString(margin, y, line)
            y -= 15  # Line spacing

    c.save()

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
    for feedback in employee_feedback:
        print(feedback)

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
    for key, value in unified_feedback.items():
        if key != "Feedback":
            print(f"{key}: {value}")
        else:
            print(value)

    # Save feedback to separate PDFs
    save_feedback_to_pdf(employee_feedback, "<b>Employee Feedback:</b>", "employee_feedback_report.pdf")
    save_feedback_to_pdf(organization_feedback, "<b>Organization Feedback:</b>", "organization_feedback_report.pdf")
    save_feedback_to_pdf([unified_feedback["Feedback"]], "<b>Unified Feedback:</b>", "unified_feedback_report.pdf")

if __name__ == "__main__":
    main()