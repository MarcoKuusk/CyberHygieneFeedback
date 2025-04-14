import openai
from utils.scoring import calculate_organization_score

class OrganizationFeedbackGenerator:
    def __init__(self, organization_responses):
        self.organization_responses = organization_responses

    def generate_feedback(self):
        # Calculate the overall score
        total_score = calculate_organization_score(self.organization_responses)

        # Summarize findings
        findings = self._summarize_findings()

        # Generate AI-based feedback
        ai_feedback = self._generate_ai_feedback(findings, total_score)

        # Return the AI-generated feedback
        return ai_feedback

    def _summarize_findings(self):
        """
        Summarizes the organization's responses into a structured list of findings.
        """
        findings = []
        for question, response in self.organization_responses.items():
            if response == 0:
                findings.append(f"{question}: Not implemented")
            elif response == 1:
                findings.append(f"{question}: Weak implementation")
            elif response == 2:
                findings.append(f"{question}: Partially implemented")
            elif response == 3:
                findings.append(f"{question}: Mostly implemented")
            elif response == 4:
                findings.append(f"{question}: Fully implemented")
        return findings

    def _generate_ai_feedback(self, findings, total_score):
        """
        Generates feedback using OpenAI's API based on the summarized findings and overall score.
        """
        # Construct the prompt dynamically based on findings
        findings_text = "\n".join(findings)
        prompt = (
            "You are a professional cybersecurity advisor specializing in assisting small and medium-sized enterprises (SMEs) "
            "to improve their cyber hygiene. Your role is to analyze self-assessment findings provided by organizations and "
            "generate professional, actionable, and tailored feedback. The feedback should prioritize critical issues, highlight "
            "key risks, and provide specific, time-bound recommendations to improve their cybersecurity posture. Maintain a "
            "professional and consultative tone in your responses.\n\n"
            f"Overall Cyber Hygiene Score: {total_score:.2f}%\n"
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