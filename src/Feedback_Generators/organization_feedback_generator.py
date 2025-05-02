import openai
from utils.scoring import calculate_organization_score

class OrganizationFeedbackGenerator:
    def __init__(self, assessment_data):
        self.assessment_data = assessment_data

    def generate_feedback(self):
        grouped_findings, strengths = self._summarize_findings()
        total_score = self._calculate_total_score()
        prompt = self._build_feedback_prompt(grouped_findings, strengths, total_score)
        return self._generate_ai_feedback(prompt)

    def _summarize_findings(self):
        grouped_findings = {}
        strengths = []

        for question_data in self.assessment_data:
            category = question_data['category']
            selected_answer = question_data.get('selectedAnswer')
            if selected_answer:
                score = selected_answer['score']
                if score >= 3:
                    strengths.append(question_data['feedback']['strength'])
                else:
                    if category not in grouped_findings:
                        grouped_findings[category] = []
                    grouped_findings[category].append(question_data['feedback']['weakness'])

        return grouped_findings, strengths

    def _calculate_total_score(self):
        total_score = 0
        max_score = 0

        for question_data in self.assessment_data:
            selected_answer = question_data.get('selectedAnswer')
            if selected_answer:
                total_score += selected_answer['score']
            max_score += len(question_data['answers']) - 1

        return (total_score / max_score) * 100 if max_score > 0 else 0
    
    def _extract_risks(self, findings):
        risks = []
        # Identity & Access Management
        if findings.get("Multi-Factor Authentication"):
            risks.append("- Account takeover risks due to insufficient MFA enforcement")
        if findings.get("Access Control"):
            risks.append("- Privilege escalation risks from infrequent access reviews")
        if findings.get("Password Policy"):
            risks.append("- Credential compromise vulnerabilities from weak passwords")
        
        # Software & Patch Management
        if findings.get("Patch Management"):
            risks.append("- Exploitable vulnerabilities due to delayed patching")
        if findings.get("Vulnerability Management"):
            risks.append("- Unidentified security gaps from infrequent scanning")
        
        # Data Protection
        if findings.get("Data Encryption"):
            risks.append("- Data breach risks from unencrypted sensitive information")
        
        # Backup & Recovery
        if findings.get("Backup Strategy") or findings.get("Backup Testing"):
            risks.append("- Business continuity risks from inadequate backup processes")
        
        # Security Awareness
        if findings.get("Security Training") or findings.get("Phishing Simulations"):
            risks.append("- Social engineering risks from untrained staff")
        
        return risks if risks else ["- No major risks identified at this time. Maintain current efforts."]

    def _build_action_plan(self, findings):
        immediate = []
        short_term = []
        medium_term = []

        # Critical IAM fixes
        if findings.get("Multi-Factor Authentication"):
            immediate.append("Implement MFA enforcement for all critical systems")
        if findings.get("Password Policy"):
            immediate.append("Enforce strong password policies with 12+ character requirements")
        
        # Access management
        if findings.get("Access Control"):
            short_term.append("Implement quarterly access reviews for privileged accounts")
        
        # Patching urgency
        if findings.get("Patch Management"):
            medium_term.append("Establish automated patch management system")
        
        # Data protection
        if findings.get("Data Encryption"):
            short_term.append("Implement full-disk encryption for sensitive data stores")
        
        # Backup improvements
        if findings.get("Backup Strategy"):
            immediate.append("Implement 3-2-1 backup strategy with offsite storage")
        
        # Training needs
        if findings.get("Security Training"):
            medium_term.append("Launch quarterly security awareness training program")
        
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
            f"Generate friendly, professional, and accessible feedback for the organization\n"
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
