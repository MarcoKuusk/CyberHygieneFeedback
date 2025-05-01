import openai
from utils.scoring import calculate_organization_score

class OrganizationFeedbackGenerator:
    def __init__(self, organization_responses, organization_name="the organization"):
        self.organization_responses = organization_responses
        self.organization_name = organization_name

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

            if "MFA" in question or "password" in question:
                domain = "Access Control"
            elif "training" in question or "awareness" in question:
                domain = "Awareness"
            elif "backup" in question or "recovery" in question:
                domain = "Backup and Recovery"
            else:
                domain = "Other"

            grouped_findings[domain].append(statement)

            if response >= 3:
                strengths.append(f"{question} ({level})")

        return grouped_findings, strengths

    def _extract_risks(self, findings):
        risks = []
        if findings["Access Control"]:
            risks.append("- Unauthorized access and credential theft due to weak access controls.")
        if findings["Awareness"]:
            risks.append("- Higher likelihood of phishing attacks due to low cybersecurity awareness.")
        if findings["Backup and Recovery"]:
            risks.append("- Risk of permanent data loss from insufficient backups and recovery plans.")
        if findings["Other"]:
            risks.append("- Exposure to various cyber threats due to general security weaknesses.")
        return risks if risks else ["- No major risks identified at this time. Maintain current efforts."]

    def _build_action_plan(self, findings):
        immediate = []
        short_term = []
        medium_term = []

        if findings["Access Control"]:
            immediate.append("Implement multi-factor authentication (MFA) on all critical accounts.")
            immediate.append("Enforce strong password policies (complexity, rotation, minimum length).")
        if findings["Awareness"]:
            immediate.append("Launch mandatory cybersecurity awareness training for all employees.")
        if findings["Backup and Recovery"]:
            short_term.append("Establish regular automated backups and test data recovery processes.")
        if findings["Other"]:
            medium_term.append("Conduct a comprehensive cybersecurity assessment and patch known vulnerabilities.")

        return immediate, short_term, medium_term

    def _determine_urgency_tone(self, total_score):
        if total_score < 20:
            return "**Severe:** Immediate and decisive cybersecurity action is required."
        elif total_score < 40:
            return "**Critical:** Significant weaknesses pose serious risks to the organization."
        elif total_score < 60:
            return "**Concerning:** Notable gaps need prompt attention to avoid vulnerabilities."
        elif total_score < 80:
            return "**Improving:** A good foundation exists; targeted improvements will strengthen security."
        elif total_score < 95:
            return "**Strong:** Solid practices are in place, with minor enhancements recommended."
        else:
            return "**Excellent:** Outstanding cybersecurity hygiene. Keep maintaining and refining your efforts."

    def _build_feedback_prompt(self, findings, strengths, total_score):
        findings_text = "\n\n".join(
            [f"**{domain}**\n" + "\n".join(f"- {item}" for item in items) 
            for domain, items in findings.items() if items]
        )

        strengths_text = (
            "\n".join(f"- {s}" for s in strengths)
            if strengths else "No notable strengths identified yet."
        )

        risks = self._extract_risks(findings)
        immediate, short_term, medium_term = self._build_action_plan(findings)
        tone = self._determine_urgency_tone(total_score)

        prompt = (
            f"You are a cybersecurity advisor for small and medium-sized enterprises (SMEs).\n"
            f"Generate friendly, professional, and accessible feedback for {self.organization_name}.\n"
            f"Use clear headers, bullet points, and concise explanations.\n\n"
            f"Example style:\n"
            f"**What You're Doing Well:** You have strong password policies. Regular staff training is a key strength.\n"
            f"**Areas to Improve:** Multi-factor authentication adoption is incomplete, exposing vulnerabilities.\n\n"
            f"Feedback based on self-assessment:\n\n"
            f"**Cyber Hygiene Score:** {total_score:.2f}%\n"
            f"{tone}\n\n"
            f"**What You're Doing Well**\n{strengths_text}\n\n"
            f"**Areas to Improve**\n{findings_text}\n\n"
            f"**Potential Risks**\n" + "\n".join(risks) + "\n\n"
            f"**Action Plan**\n"
            f"**Immediate (0–30 Days)**\n" + ("\n".join(f"- {a}" for a in immediate) if immediate else "- Maintain existing strong practices.") + "\n\n"
            f"**Short-Term (60–90 Days)**\n" + ("\n".join(f"- {a}" for a in short_term) if short_term else "- Continue monitoring and improvement.") + "\n\n"
            f"**Medium-Term (3–6 Months)**\n" + ("\n".join(f"- {a}" for a in medium_term) if medium_term else "- Plan for regular cybersecurity reassessments.")
        )

        return prompt

    def _generate_ai_feedback(self, prompt):
        client = openai.OpenAI(api_key="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")  # Replace with secure method
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
