import openai
from utils.scoring import calculate_employee_score

class EmployeeFeedbackGenerator:
    def __init__(self, assessment_data):
        self.assessment_data = assessment_data

    def generate_feedback(self):
        findings, strengths = self._summarize_findings()
        total_score = self._calculate_total_score()
        prompt = self._build_feedback_prompt(findings, strengths, total_score)
        return self._generate_ai_feedback(prompt)

    def _summarize_findings(self):
        findings = []
        strengths = []

        for question_data in self.assessment_data:
            selected_answer = question_data.get('selectedAnswer')
            if selected_answer:
                score = selected_answer['score']
                question = question_data['question']
                if score >= 3:
                    strengths.append(f"Good practice: {question}")
                else:
                    findings.append(f"Needs improvement: {question}")

        return findings, strengths

    def _calculate_total_score(self):
        total_score = 0
        max_score = 0

        for question_data in self.assessment_data:
            selected_answer = question_data.get('selectedAnswer')
            if selected_answer:
                total_score += selected_answer['score']
            max_score += len(question_data['answers']) - 1

        return (total_score / max_score) * 100 if max_score > 0 else 0

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