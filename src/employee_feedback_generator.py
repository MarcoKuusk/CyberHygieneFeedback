import openai
from utils.scoring import calculate_employee_score

class EmployeeFeedbackGenerator:
    def __init__(self, employee_responses):
        self.employee_responses = employee_responses

    def generate_feedback(self):
        # Calculate the overall employee score
        total_score = calculate_employee_score(self.employee_responses)

        # Summarize findings
        findings = self._summarize_findings()

        # Generate AI-based feedback
        ai_feedback = self._generate_ai_feedback(findings, total_score)

        # Return the AI-generated feedback
        return ai_feedback

    def _summarize_findings(self):
        """
        Summarizes the employee's responses into a structured list of findings.
        """
        findings = []
        for question, response in self.employee_responses.items():
            if response == 0:
                findings.append(f"{question}: Not practiced")
            elif response == 1:
                findings.append(f"{question}: Weak practice")
            elif response == 2:
                findings.append(f"{question}: Moderate practice")
            elif response == 3:
                findings.append(f"{question}: Strong practice")
            elif response == 4:
                findings.append(f"{question}: Excellent practice")
        return findings

    def _generate_ai_feedback(self, findings, total_score):
        """
        Generates feedback using OpenAI's API based on the summarized findings and overall score.
        """
        findings_text = "\n".join(findings)
        prompt = (
            "You are a cybersecurity advisor specializing in employee-level cyber hygiene. "
            "Your role is to analyze self-assessment findings provided by employees and generate professional, actionable, and tailored feedback. "
            "The feedback should highlight key risks, prioritize critical issues, and provide specific recommendations to improve their cybersecurity practices. "
            "Maintain a professional and consultative tone in your responses.\n\n"
            f"Overall Employee Cyber Hygiene Score: {total_score:.2f}%\n"
            f"Findings:\n{findings_text}\n\n"
            "Provide your feedback in two paragraphs."
        )

        # Call OpenAI API to generate feedback
        client = openai.OpenAI(api_key="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")  # Replace with your actual API key
        response = client.responses.create(
            model="gpt-4o",
            input=prompt
        )

        # Extract and return the generated feedback
        return response.output_text