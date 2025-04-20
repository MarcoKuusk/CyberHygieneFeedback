import openai
from utils.scoring import calculate_organization_score

class OrganizationFeedbackGenerator:
    def __init__(self, organization_responses):
        self.organization_responses = organization_responses

    def generate_feedback(self):
        total_score = calculate_organization_score(self.organization_responses)
        grouped_findings, strengths = self._summarize_findings()
        prompt = self._build_feedback_prompt(grouped_findings, strengths, total_score)
        return self._generate_ai_feedback(prompt)

    def _summarize_findings(self):
        grouped_findings = {
            "Access Control": [],
            "Awareness": [],
            "Backup and Recovery": [],
            "Other": []
        }
        strengths = []

        for question, response in self.organization_responses.items():
            level = [
                "Not implemented",
                "Weak implementation",
                "Partially implemented",
                "Mostly implemented",
                "Fully implemented"
            ][response]

            statement = f"{question}: {level}"

            # Categorize findings (you can customize this logic further)
            if "MFA" in question or "password" in question:
                domain = "Access Control"
            elif "training" in question or "awareness" in question:
                domain = "Awareness"
            elif "backup" in question or "recovery" in question:
                domain = "Backup and Recovery"
            else:
                domain = "Other"

            grouped_findings[domain].append(statement)

            # Track strengths (score of 3 or 4)
            if response >= 3:
                strengths.append(f"{question} ({level})")

        return grouped_findings, strengths

    def _build_feedback_prompt(self, findings, strengths, total_score):
        findings_text = "\n".join(
            [f"### {domain}\n" + "\n".join(f"- {item}" for item in items) 
             for domain, items in findings.items() if items]
        )

        strengths_text = (
            "\n".join(f"- {s}" for s in strengths)
            if strengths else "No notable strengths identified yet."
        )

        # Tailor urgency message
        if total_score < 30:
            urgency = "🔴 **Critical:** Your cyber hygiene posture is weak and urgent action is needed."
        elif total_score < 60:
            urgency = "🟠 **Needs Improvement:** You have made some progress but key gaps remain."
        else:
            urgency = "🟢 **Moderate:** You're on the right track but should continue strengthening security."

        return (
            f"You are a cybersecurity advisor for small and medium-sized enterprises (SMEs).\n"
            f"Based on the cyber hygiene self-assessment, generate friendly, well-structured, and professional feedback.\n\n"
            f"**Score:** {total_score:.2f}%\n"
            f"{urgency}\n\n"
            f"## ✅ What You're Doing Well\n{strengths_text}\n\n"
            f"## ⚠️ Areas to Improve\n{findings_text}\n\n"
            f"## 🔍 Potential Risks\n"
            f"- Credential theft due to weak access controls\n"
            f"- Data loss if backups are unreliable\n"
            f"- Phishing attacks targeting untrained staff\n"
            f"- System compromise from unpatched vulnerabilities\n\n"
            f"## 🛠️ Action Plan\n"
            f"### 🔴 Immediate (0–30 Days)\n"
            f"- Implement MFA for all critical systems\n"
            f"- Start cybersecurity awareness training\n"
            f"- Enforce strong password policies\n\n"
            f"### 🟠 Short-Term (60–90 Days)\n"
            f"- Set up automated backups and test recovery\n"
            f"- Patch outdated systems and software\n\n"
            f"### 🟢 Medium-Term (3–6 Months)\n"
            f"- Review user access privileges regularly\n"
            f"- Encrypt sensitive data at rest and in transit\n\n"
            f"Keep your language clear and accessible. Use headers, bullets, and emojis to aid readability."
        )

    def _generate_ai_feedback(self, prompt):
        client = openai.OpenAI(api_key="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")  # Replace with secure method
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
