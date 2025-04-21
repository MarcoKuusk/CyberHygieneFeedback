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
            urgency = "🔴 **Critical Risk:** There are major weaknesses across both employee and organizational levels."
        elif unified_score < 60:
            urgency = "🟠 **Needs Improvement:** The cybersecurity foundation exists, but critical issues remain."
        else:
            urgency = "🟢 **Promising Start:** The overall posture is solid, though improvement is still needed."

        gap_comment = (
            f"There's a significant gap between the organizational score ({self.org_score:.2f}%) and employee score ({self.emp_score:.2f}%). "
            "This suggests a disconnect between policy and practice, which can expose the organization to risk."
            if score_gap >= 15 else
            f"Employee and organizational scores are well-aligned ({self.org_score:.2f}% vs. {self.emp_score:.2f}%), indicating cohesive efforts."
        )

        return (
            "You are a cybersecurity advisor conducting a unified assessment of a small or medium-sized enterprise (SME). "
            "You've received two scores: one based on organizational practices and policies, and another based on employee behavior. "
            "Generate clear, structured, and actionable feedback that includes an overall summary, risk interpretation, and joint improvement steps.\n\n"
            f"### Unified Cyber Hygiene Score: {unified_score:.2f}%\n"
            f"{urgency}\n"
            f"{gap_comment}\n\n"
            "## 🔎 Summary\n"
            "- Organizational Score: {org_score:.2f}%\n"
            "- Employee Score: {emp_score:.2f}%\n\n"
            "## ✅ Strengths\n"
            "- Strong password and access management policies (if org score is high)\n"
            "- Employees showing good awareness of phishing and safe browsing (if employee score is high)\n"
            "- Alignment between policy and practice (if scores are close)\n\n"
            "## ⚠️ Risks\n"
            "- Policies not translating into practice (if employee score is much lower)\n"
            "- Lack of policy guidance (if org score is much lower)\n"
            "- Fragmented communication and inconsistent security culture\n\n"
            "## 🛠️ Joint Action Plan\n"
            "### 🔴 Immediate\n"
            "- Ensure cybersecurity policies are actively communicated and enforced.\n"
            "- Require all employees to complete security training within the next month.\n"
            "- Review internal access controls and employee onboarding/offboarding processes.\n\n"
            "### 🟠 Next 60–90 Days\n"
            "- Hold joint policy-practice workshops to bridge gaps.\n"
            "- Implement monitoring and internal audits to reinforce behavior change.\n\n"
            "Write in a professional tone that is consultative and supportive. Emphasize alignment and collaboration between IT leaders and staff."
        ).format(
            unified_score=unified_score,
            org_score=self.org_score,
            emp_score=self.emp_score
        )

    def _generate_ai_feedback(self, prompt):
        client = openai.OpenAI(api_key="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")  # Secure your key
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
