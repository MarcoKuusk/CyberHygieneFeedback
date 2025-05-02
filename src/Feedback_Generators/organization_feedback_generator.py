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
                question = question_data['question']
                if score >= 3:
                    # Dynamically generate strength based on the question
                    strengths.append(f"Good practice: {question}")
                else:
                    # Dynamically generate weakness based on the question
                    if category not in grouped_findings:
                        grouped_findings[category] = []
                    grouped_findings[category].append(f"Needs improvement: {question}")

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
            f"**{category}**\n" + "\n".join(f"- {item}" for item in items)
            for category, items in findings.items()
        )

        strengths_text = "\n".join(f"- {s}" for s in strengths) if strengths else "- No specific strengths identified yet."

        risks = self._extract_risks(findings)
        immediate, short_term, medium_term = self._build_action_plan(findings)
        tone = self._determine_urgency_tone(total_score)

        prompt = f"""
        You are a cybersecurity advisor helping small and medium-sized enterprises (SMEs) improve their security posture.

        Generate a clear, structured, and accessible feedback report based on the following assessment data. Your audience is SME business leaders who may not be technical, so use plain language and actionable advice.

        Use the following format:

        ## Cyber Hygiene Score
        {total_score:.2f}%  
        {tone}

        ## Introduction
        Write a short paragraph summarizing the organization's current cybersecurity hygiene based on the score. Mention whether it's strong, moderate, or weak, and emphasize the importance of continuous improvement.

        ## What You're Doing Well
        Highlight areas where the organization is following good practices. Use bullet points and explain why each practice is important.

        {strengths_text}

        ## Areas to Improve
        Break down weaknesses by category. Clearly explain what needs improvement and why it matters. Use plain language.

        {findings_text}

        ## Potential Risks and Risk Scenarios
        Describe the potential threats based on weaknesses. Write short, scenario-based risk statements (e.g., “Without MFA, an attacker could take over email accounts.”)

        {chr(10).join(risks)}

        ## Action Plan

        Provide a prioritized and **concrete cybersecurity action plan** for the organization. Break actions into timeframes based on effort and urgency. Ensure **each timeframe has at least 4–6 specific, actionable tasks** the organization can execute.

        ### Immediate (0–30 Days)
        These should be quick wins or critical issues. Phrase them as direct, clear steps:
        {chr(10).join(f"- {item}" for item in immediate) if immediate else "- No urgent actions identified."}

        ### Short-Term (60–90 Days)
        Mid-term improvements requiring some planning:
        {chr(10).join(f"- {item}" for item in short_term) if short_term else "- No short-term actions identified."}

        ### Medium-Term (3–6 Months)
        Strategic actions for sustained cybersecurity maturity:
        {chr(10).join(f"- {item}" for item in medium_term) if medium_term else "- No medium-term actions identified."}


        ## Conclusion
        Encourage the organization to continue improving its cybersecurity posture. Recommend reassessing in 6–12 months. Reinforce that even small steps can significantly reduce risk.

        Return the feedback as if you were delivering it to a real SME client.
        """

        return prompt.strip()

    def _generate_ai_feedback(self, prompt):
        client = openai.OpenAI(api_key="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")  # Replace with secure method
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
