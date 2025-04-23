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
        self.root.geometry("600x400")

        # UI Elements
        self.label = tk.Label(root, text="Cyber Hygiene Feedback Generator", font=("Arial", 16))
        self.label.pack(pady=10)

        self.employee_feedback_btn = tk.Button(root, text="Take Employee Feedback Questionnaire", command=self.take_employee_feedback)
        self.employee_feedback_btn.pack(pady=5)

        self.organization_feedback_btn = tk.Button(root, text="Take Organization Feedback Questionnaire", command=self.take_organization_feedback)
        self.organization_feedback_btn.pack(pady=5)

        self.unified_feedback_btn = tk.Button(root, text="Take Unified Feedback Questionnaire", command=self.take_unified_feedback)
        self.unified_feedback_btn.pack(pady=20)

        self.employee_questionnaire = None
        self.organization_questionnaire = None
        self.current_question_index = 0
        self.responses = {}
        self.current_questionnaire = None

    def load_questionnaires(self):
        # Automatically load questionnaires from the src/data folder
        base_path = os.path.join(os.path.dirname(__file__), "data")
        employee_file = os.path.join(base_path, "employee_questionnaire.json")
        organization_file = os.path.join(base_path, "organization_questionnaire.json")

        try:
            self.employee_questionnaire = load_questionnaire(employee_file)
            self.organization_questionnaire = load_questionnaire(organization_file)
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Failed to load questionnaires: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def start_questionnaire(self, questionnaire):
        # Flatten the nested structure of categories and questions
        self.current_questionnaire = []
        for category in questionnaire['questions']:
            if 'questions' in category:
                self.current_questionnaire.extend(category['questions'])
            else:
                self.current_questionnaire.append(category)

        self.current_question_index = 0
        self.responses = {}
        self.show_question()

    def show_question(self):
        if self.current_question_index < len(self.current_questionnaire):
            question_data = self.current_questionnaire[self.current_question_index]
            self.display_question(question_data)
        else:
            self.finish_questionnaire()

    def display_question(self, question_data):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display the question
        question_label = tk.Label(self.root, text=question_data['question'], font=("Arial", 14))
        question_label.pack(pady=10)

        # Display the multiple-choice options
        selected_answer = tk.StringVar()
        for answer in question_data['answers']:
            # Handle both 'option' and 'text' keys
            answer_text = answer.get('option') or answer.get('text')
            tk.Radiobutton(self.root, text=answer_text, variable=selected_answer, value=answer_text, font=("Arial", 12)).pack(anchor="w")

        # Next button
        next_button = tk.Button(self.root, text="Next", command=lambda: self.save_response_and_next(question_data['question'], selected_answer))
        next_button.pack(pady=20)

    def save_response_and_next(self, question, selected_answer):
        answer = selected_answer.get()
        if not answer:
            messagebox.showwarning("Warning", "Please select an answer before proceeding.")
            return

        self.responses[question] = answer
        self.current_question_index += 1
        self.show_question()

    def finish_questionnaire(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Display completion message
        tk.Label(self.root, text="Thank you for completing the questionnaire!", font=("Arial", 16)).pack(pady=20)

        # Generate feedback
        if self.current_questionnaire == self.employee_questionnaire:
            feedback_generator = EmployeeFeedbackGenerator(self.responses)
            feedback = feedback_generator.generate_feedback()
            save_feedback_to_pdf(feedback, "Employee Feedback", "employee_feedback_report.pdf")
        elif self.current_questionnaire == self.organization_questionnaire:
            feedback_generator = OrganizationFeedbackGenerator(self.responses)
            feedback = feedback_generator.generate_feedback()
            save_feedback_to_pdf(feedback, "Organization Feedback", "organization_feedback_report.pdf")

        # Back to main menu button
        tk.Button(self.root, text="Back to Main Menu", command=self.reset_ui).pack(pady=20)

    def reset_ui(self):
        # Reset the UI to the main menu
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)

    def take_employee_feedback(self):
        self.load_questionnaires()
        if self.employee_questionnaire:
            self.start_questionnaire(self.employee_questionnaire)

    def take_organization_feedback(self):
        self.load_questionnaires()
        if self.organization_questionnaire:
            self.start_questionnaire(self.organization_questionnaire)

    def take_unified_feedback(self):
        self.load_questionnaires()
        if self.employee_questionnaire and self.organization_questionnaire:
            # Combine both questionnaires for unified feedback
            unified_questions = self.employee_questionnaire['questions'] + self.organization_questionnaire['questions']
            unified_questionnaire = {'questions': unified_questions}
            self.start_questionnaire(unified_questionnaire)

if __name__ == "__main__":
    root = tk.Tk()
    app = FeedbackApp(root)
    root.mainloop()