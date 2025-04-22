import openai
from utils.scoring import calculate_employee_score

class EmployeeFeedbackGenerator:
    def __init__(self, employee_responses):
        self.employee_responses = employee_responses

    def generate_feedback(self):
        total_score = calculate_employee_score(self.employee_responses)
        findings, strengths = self._summarize_findings()
        prompt = self._build_feedback_prompt(findings, strengths, total_score)
        return self._generate_ai_feedback(prompt)

    def _summarize_findings(self):
        """
        Summarizes employee responses into strengths and improvement areas.
        """
        findings = []
        strengths = []

        for question, response in self.employee_responses.items():
            label = [
                "Not practiced",
                "Weak practice",
                "Moderate practice",
                "Strong practice",
                "Excellent practice"
            ][response]

            statement = f"{question}: {label}"

            if response >= 3:
                strengths.append(statement)
            else:
                findings.append(statement)

        return findings, strengths

    def _build_feedback_prompt(self, findings, strengths, total_score):
        findings_text = "\n".join(f"- {f}" for f in findings) if findings else "- None"
        strengths_text = "\n".join(f"- {s}" for s in strengths) if strengths else "- None"

        if total_score < 30:
            urgency = "**Critical:** Your cyber hygiene practices need urgent improvement."
        elif total_score < 60:
            urgency = "**Needs Improvement:** You're making progress, but there are significant gaps."
        else:
            urgency = "**Good Start:** You're doing well, but there's room for improvement."

        return (
            f"You are a cybersecurity advisor helping employees improve their digital hygiene.\n"
            f"Based on the self-assessment, provide structured and actionable feedback.\n\n"
            f"**Score:** {total_score:.2f}%\n"
            f"{urgency}\n\n"
            f"**What You're Doing Well**\n{strengths_text}\n\n"
            f"**Areas to Improve**\n{findings_text}\n\n"
            f"**Potential Risks**\n"
            f"- Falling for phishing emails\n"
            f"- Weak password habits\n"
            f"- Outdated software vulnerabilities\n\n"
            f"**Action Plan**\n"
            f"**Immediate (0–30 Days)**\n"
            f"- Avoid clicking on suspicious links.\n"
            f"- Use strong, unique passwords and enable multi-factor authentication.\n"
            f"- Keep devices updated and restart them regularly.\n\n"
            f"**Short-Term (60–90 Days)**\n"
            f"- Participate in cybersecurity training.\n"
            f"- Practice identifying social engineering attempts.\n\n"
            f"Keep the tone friendly and motivational to encourage improvement."
        )

    def _generate_ai_feedback(self, prompt):
        client = openai.OpenAI(api_key="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")  # Secure this key
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content