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
            urgency = "🔴 **Critical:** Your current cyber hygiene practices need serious improvement."
        elif total_score < 60:
            urgency = "🟠 **Needs Improvement:** You're doing okay, but there are key risks to address."
        else:
            urgency = "🟢 **Good Start:** You're showing strong awareness, but some areas still need attention."

        return (
            "You are a cybersecurity advisor who helps individual employees improve their digital hygiene.\n"
            "Based on their self-assessment results, write clear, positive, and constructive feedback.\n"
            "Structure the feedback with bullet points, emojis, and headers to make it easy to understand.\n\n"
            f"**Cyber Hygiene Score:** {total_score:.2f}%\n"
            f"{urgency}\n\n"
            f"## ✅ What You're Doing Well\n{strengths_text}\n\n"
            f"## ⚠️ Areas to Improve\n{findings_text}\n\n"
            f"## 🔍 Potential Risks\n"
            f"- Phishing emails may trick you into revealing passwords or clicking dangerous links.\n"
            f"- Weak password habits can lead to unauthorized access to sensitive information.\n"
            f"- Not updating software can leave devices vulnerable to malware and attacks.\n\n"
            f"## 🛠️ Action Plan\n"
            f"### 🔴 Immediate\n"
            f"- Always check email senders and avoid clicking suspicious links.\n"
            f"- Use long, unique passwords and enable multi-factor authentication.\n"
            f"- Keep work devices up to date and restart them regularly.\n\n"
            f"### 🟠 Next 2–3 Months\n"
            f"- Take part in cybersecurity training sessions.\n"
            f"- Practice identifying social engineering tricks like fake tech support calls.\n\n"
            f"Keep the tone friendly, motivational, and helpful — you’re coaching them to be a cyber-safe employee."
        )

    def _generate_ai_feedback(self, prompt):
        client = openai.OpenAI(api_key="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")  # Secure this key
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
