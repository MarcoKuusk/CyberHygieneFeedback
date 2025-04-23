import tkinter as tk
from tkinter import messagebox
from main import load_questionnaire, save_feedback_to_pdf
from employee_feedback_generator import EmployeeFeedbackGenerator
from organization_feedback_generator import OrganizationFeedbackGenerator
from unified_feedback_generator import UnifiedFeedbackGenerator
from utils.scoring import calculate_employee_score, calculate_organization_score
import os

class FeedbackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Hygiene Feedback")
        self.root.geometry("800x600")
        
        # Initialize state
        self.employee_responses = {}
        self.organization_responses = {}
        self.current_questionnaire = None
        self.current_category = None
        self.current_question_index = 0
        
        # Load questionnaires
        self.load_questionnaires()
        self.create_main_menu()

    def load_questionnaires(self):
        try:
            # Get the correct base path
            base_path = os.path.join(os.path.dirname(__file__), "data")
            print(f"Looking for questionnaires in: {base_path}")  # For debugging
            
            employee_path = os.path.join(base_path, "employee_questionnaire.json")
            organization_path = os.path.join(base_path, "organization_questionnaire.json")
            
            print(f"Employee path: {employee_path}")  # For debugging
            print(f"Organization path: {organization_path}")  # For debugging
            
            self.employee_questionnaire = load_questionnaire(employee_path)
            self.organization_questionnaire = load_questionnaire(organization_path)
            return True
        except Exception as e:
            messagebox.showerror("Error", 
                f"Failed to load questionnaires: {str(e)}\n"
                f"Checked paths:\n{employee_path}\n{organization_path}")
            self.root.destroy()
            return False

    def create_main_menu(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main menu UI
        tk.Label(self.root, text="Cyber Hygiene Assessment", 
                font=("Arial", 16, "bold")).pack(pady=20)
        
        buttons = [
            ("Employee Assessment", self.start_employee_assessment),
            ("Organization Assessment", self.start_organization_assessment),
            ("Generate Unified Report", self.generate_unified_report)
        ]
        
        for text, cmd in buttons:
            tk.Button(self.root, text=text, command=cmd,
                     width=30, height=2, font=("Arial", 12)).pack(pady=10)

    def start_questionnaire(self, questionnaire_type):
        # Reset state
        self.current_question_index = 0
        self.current_questionnaire = (
            self.employee_questionnaire if questionnaire_type == "employee" 
            else self.organization_questionnaire
        )
        self.current_responses = {}
        
        # Flatten questions based on structure
        self.flat_questions = []
        for item in self.current_questionnaire['questions']:
            if 'questions' in item:  # Employee structure with categories
                self.current_category = item['category']
                for q in item['questions']:
                    q['category'] = self.current_category
                    self.flat_questions.append(q)
            else:  # Organization structure
                self.flat_questions.append(item)
        
        self.show_next_question()

    def show_next_question(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        if self.current_question_index >= len(self.flat_questions):
            self.finish_questionnaire()
            return
            
        question_data = self.flat_questions[self.current_question_index]
        self.display_question(question_data)

    def display_question(self, question_data):
        # Header
        if 'category' in question_data:
            tk.Label(self.root, text=question_data['category'], 
                    font=("Arial", 14, "bold"), fg="#2c3e50").pack(pady=10)
        
        # Question text
        tk.Label(self.root, text=question_data['question'], 
                font=("Arial", 12), wraplength=700).pack(pady=15)
        
        # Answer options
        self.selected_answer = tk.IntVar(value=-1)
        answers = question_data['answers']
        
        for idx, answer in enumerate(answers):
            # Handle different answer key names
            score = answer.get('score', answer.get('value', 0))
            text = answer.get('option', answer.get('text', ""))
            
            tk.Radiobutton(
                self.root,
                text=text,
                variable=self.selected_answer,
                value=score,
                font=("Arial", 11),
                wraplength=650,
                justify="left"
            ).pack(anchor="w", padx=20)

        # Navigation
        nav_frame = tk.Frame(self.root)
        nav_frame.pack(pady=20)
        
        if self.current_question_index > 0:
            tk.Button(nav_frame, text="Back", 
                     command=self.prev_question).pack(side="left", padx=10)
            
        tk.Button(nav_frame, text="Next" if self.current_question_index < len(self.flat_questions)-1 else "Submit",
                 command=self.next_question).pack(side="right", padx=10)

    def next_question(self):
        if self.selected_answer.get() == -1:
            messagebox.showwarning("Warning", "Please select an answer")
            return
            
        question_text = self.flat_questions[self.current_question_index]['question']
        self.current_responses[question_text] = self.selected_answer.get()
        self.current_question_index += 1
        self.show_next_question()

    def prev_question(self):
        self.current_question_index -= 1
        self.show_next_question()

    def finish_questionnaire(self):
        # Save responses to appropriate storage
        if self.current_questionnaire == self.employee_questionnaire:
            self.employee_responses = self.current_responses.copy()
            generator = EmployeeFeedbackGenerator(self.employee_responses)
            filename = "employee_feedback.pdf"
            title = "Employee Cybersecurity Report"
        else:
            self.organization_responses = self.current_responses.copy()
            generator = OrganizationFeedbackGenerator(self.organization_responses)
            filename = "organization_feedback.pdf"
            title = "Organization Cybersecurity Report"
        
        # Generate and save PDF
        try:
            feedback = generator.generate_feedback()
            save_feedback_to_pdf(feedback, title, filename)
            messagebox.showinfo("Success", f"PDF report generated:\n{filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate PDF: {str(e)}")
        
        self.create_main_menu()

    def start_employee_assessment(self):
        self.start_questionnaire("employee")

    def start_organization_assessment(self):
        self.start_questionnaire("organization")

    def generate_unified_report(self):
        try:
            if not self.employee_responses or not self.organization_responses:
                raise ValueError("Complete both assessments first")
            
            emp_score = calculate_employee_score(self.employee_responses)
            org_score = calculate_organization_score(self.organization_responses)
            
            generator = UnifiedFeedbackGenerator(org_score, emp_score)
            feedback = generator.generate_feedback()
            
            save_feedback_to_pdf(feedback, "Unified Cybersecurity Report", "unified_report.pdf")
            messagebox.showinfo("Success", "Unified report generated successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate unified report: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FeedbackApp(root)
    root.mainloop()