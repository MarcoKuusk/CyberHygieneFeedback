import tkinter as tk
from tkinter import filedialog, messagebox
from main import load_questionnaire, save_feedback_to_pdf
from employee_feedback_generator import EmployeeFeedbackGenerator
from organization_feedback_generator import OrganizationFeedbackGenerator
from unified_feedback_generator import UnifiedFeedbackGenerator
from utils.scoring import calculate_employee_score, calculate_organization_score

class FeedbackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Hygiene Feedback")
        self.root.geometry("600x400")

        # UI Elements
        self.label = tk.Label(root, text="Cyber Hygiene Feedback Generator", font=("Arial", 16))
        self.label.pack(pady=10)

        self.load_employee_btn = tk.Button(root, text="Load Employee Questionnaire", command=self.load_employee_questionnaire)
        self.load_employee_btn.pack(pady=5)

        self.load_organization_btn = tk.Button(root, text="Load Organization Questionnaire", command=self.load_organization_questionnaire)
        self.load_organization_btn.pack(pady=5)

        self.generate_feedback_btn = tk.Button(root, text="Generate Feedback", command=self.generate_feedback, state=tk.DISABLED)
        self.generate_feedback_btn.pack(pady=20)

        self.employee_questionnaire = None
        self.organization_questionnaire = None
        self.employee_responses = {}
        self.organization_responses = {}

    def load_employee_questionnaire(self):
        file_path = filedialog.askopenfilename(title="Select Employee Questionnaire", filetypes=[("JSON Files", "*.json")])
        if file_path:
            self.employee_questionnaire = load_questionnaire(file_path)
            messagebox.showinfo("Success", "Employee Questionnaire Loaded Successfully!")
            self.check_ready_state()

    def load_organization_questionnaire(self):
        file_path = filedialog.askopenfilename(title="Select Organization Questionnaire", filetypes=[("JSON Files", "*.json")])
        if file_path:
            self.organization_questionnaire = load_questionnaire(file_path)
            messagebox.showinfo("Success", "Organization Questionnaire Loaded Successfully!")
            self.check_ready_state()

    def check_ready_state(self):
        if self.employee_questionnaire and self.organization_questionnaire:
            self.generate_feedback_btn.config(state=tk.NORMAL)

    def generate_feedback(self):
        # Generate feedback for employee questionnaire
        employee_feedback_generator = EmployeeFeedbackGenerator(self.employee_responses)
        employee_feedback = employee_feedback_generator.generate_feedback()

        # Generate feedback for organization questionnaire
        organization_feedback_generator = OrganizationFeedbackGenerator(self.organization_responses)
        organization_feedback = organization_feedback_generator.generate_feedback()

        # Calculate scores for unified feedback
        org_score = calculate_organization_score(self.organization_responses)
        emp_score = calculate_employee_score(self.employee_responses)
        unified_feedback_generator = UnifiedFeedbackGenerator(org_score, emp_score)

        # Generate unified feedback
        unified_feedback = unified_feedback_generator.generate_feedback()

        # Save feedback to PDFs
        save_feedback_to_pdf(employee_feedback, "Employee Feedback", "employee_feedback_report.pdf")
        save_feedback_to_pdf(organization_feedback, "Organization Feedback", "organization_feedback_report.pdf")
        save_feedback_to_pdf(unified_feedback, "Unified Feedback", "unified_feedback_report.pdf")

        messagebox.showinfo("Success", "Feedback Generated and Saved as PDFs!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FeedbackApp(root)
    root.mainloop()