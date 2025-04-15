import openai
from utils.scoring import calculate_unified_score

class UnifiedFeedbackGenerator:
    def __init__(self, org_score, emp_score):
        self.org_score = org_score
        self.emp_score = emp_score

    def generate_feedback(self):
        # Calculate the unified score
        unified_score = calculate_unified_score(self.org_score, self.emp_score)

        # Generate AI-based feedback
        ai_feedback = self._generate_ai_feedback(unified_score)

        # Return the AI-generated feedback
        return ai_feedback

    def _generate_ai_feedback(self, unified_score):
        """
        Generates feedback using OpenAI's API based on the unified score.
        """
        prompt = (
            "You are a cybersecurity advisor specializing in holistic cyber hygiene assessments. "
            "Your role is to analyze combined organizational and employee-level cyber hygiene scores and generate professional, actionable, and tailored feedback. "
            "The feedback should highlight key risks, prioritize critical issues, and provide specific recommendations to improve the organization's overall cybersecurity posture. "
            "Maintain a professional and consultative tone in your responses.\n\n"
            f"Unified Cyber Hygiene Score: {unified_score:.2f}%\n"
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