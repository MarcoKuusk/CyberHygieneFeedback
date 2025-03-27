from utils.scoring import calculate_unified_score

class UnifiedFeedbackGenerator:
    def __init__(self, org_score, emp_score):
        self.org_score = org_score
        self.emp_score = emp_score

    def generate_feedback(self):
        unified_score = calculate_unified_score(self.org_score, self.emp_score)
        feedback = {
            "Organization Score": self.org_score,
            "Employee Score": self.emp_score,
            "Unified Score": unified_score,
            "Feedback": self._generate_feedback(unified_score)
        }
        return feedback

    def _generate_feedback(self, unified_score):
        feedback = []
        feedback.append(f"Unified Cyber Hygiene Score: {unified_score:.2f}%")
        feedback.append(self._interpret_score(unified_score))
        return "\n".join(feedback)

    def _interpret_score(self, score):
        if score >= 90:
            return "Excellent (Highly secure and aware organization)"
        elif score >= 75:
            return "Strong (Good security policies and employee awareness)"
        elif score >= 50:
            return "Moderate (Some security gaps or behavioral risks)"
        elif score >= 25:
            return "Weak (Significant cybersecurity weaknesses, urgent improvements needed)"
        else:
            return "Critical (Severe risks from both technical and human factors)"