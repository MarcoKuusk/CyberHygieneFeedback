import openai
from utils.scoring import calculate_unified_score

class UnifiedFeedbackGenerator:
    def __init__(self, org_score, emp_score):
        self.org_score = org_score
        self.emp_score = emp_score

    def generate_feedback(self):
        unified_score = calculate_unified_score(self.org_score, self.emp_score)
        prompt = self._build_feedback_prompt(unified_score)
        return self._generate_ai_feedback(prompt)

    def _build_feedback_prompt(self, unified_score):
        score_gap = abs(self.org_score - self.emp_score)

        if unified_score < 30:
            urgency = "**Critical Risk:** Major weaknesses exist across both organizational and employee levels."
        elif unified_score < 60:
            urgency = "**Needs Improvement:** The foundation is there, but critical gaps remain."
        else:
            urgency = "**Promising Start:** The overall posture is solid, but further improvement is needed."

        gap_comment = (
            f"There's a significant gap between the organizational score ({self.org_score:.2f}%) and employee score ({self.emp_score:.2f}%). "
            "This indicates a disconnect between policy and practice, which could expose the organization to risks."
            if score_gap >= 15 else
            f"Employee and organizational scores are well-aligned ({self.org_score:.2f}% vs. {self.emp_score:.2f}%), indicating cohesive efforts."
        )

        return (
            f"You are a cybersecurity advisor conducting a unified assessment for an SME.\n"
            f"Based on the scores, provide structured and actionable feedback.\n\n"
            f"**Unified Score:** {unified_score:.2f}%\n"
            f"{urgency}\n"
            f"{gap_comment}\n\n"
            f"**What You're Doing Well**\n"
            f"- Organizational Score: {self.org_score:.2f}%\n"
            f"- Employee Score: {self.emp_score:.2f}%\n\n"
            f"**Areas to Improve**\n"
            f"- Address gaps between policy and practice.\n"
            f"- Strengthen communication and training efforts.\n\n"
            f"**Potential Risks**\n"
            f"- Misalignment between organizational policies and employee behavior.\n"
            f"- Inconsistent security practices across teams.\n\n"
            f"**Action Plan**\n"
            f"**Immediate (0–30 Days)**\n"
            f"- Communicate cybersecurity policies clearly.\n"
            f"- Ensure all employees complete security training.\n"
            f"- Review access controls and onboarding processes.\n\n"
            f"**Short-Term (60–90 Days)**\n"
            f"- Conduct workshops to align policies and practices.\n"
            f"- Implement monitoring to reinforce behavior changes.\n\n"
            f"Write in a professional and supportive tone, emphasizing collaboration."
        )

    def _generate_ai_feedback(self, prompt):
        client = openai.OpenAI(api_key="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")  # Secure your key
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content