from utils.scoring import calculate_employee_score

class EmployeeFeedbackGenerator:
    def __init__(self, employee_responses):
        self.employee_responses = employee_responses

    def generate_feedback(self):
        feedback = []
        total_score = calculate_employee_score(self.employee_responses)
        feedback.append(f"Overall Employee Cyber Hygiene Score: {total_score:.2f}%")
        for question, response in self.employee_responses.items():
            feedback.append(self._evaluate_response(question, response))
        return feedback

    def _evaluate_response(self, question, response):
        feedback = []
        feedback.append(f"Assessment of Current Security Posture for '{question}':")
        feedback.append(f"Score: {response}")
        feedback.append(self._interpret_response(response))
        feedback.append("Identified Weaknesses & Risks:")
        feedback.append(self._identify_risks(response))
        feedback.append("Recommended Improvements:")
        feedback.extend(self._recommend_improvements(response))
        feedback.append("Urgency & Next Steps:")
        feedback.append(self._determine_urgency(response))
        return "\n".join(feedback)

    def _interpret_response(self, response):
        return f"Response {response} indicates a need for improvement."

    def _identify_risks(self, response):
        if response < 2:
            return "There are significant vulnerabilities that could be exploited by attackers."
        elif response < 4:
            return "Some risks exist that could be mitigated with better practices."
        else:
            return "Minimal risks, but continuous monitoring is recommended."

    def _recommend_improvements(self, response):
        recommendations = []
        if response < 2:
            recommendations.append("1. Implement multi-factor authentication (MFA) for all accounts.")
            recommendations.append("2. Conduct regular security awareness training for employees.")
            recommendations.append("3. Establish a formal incident response plan.")
        elif response < 4:
            recommendations.append("1. Review and update access controls regularly.")
            recommendations.append("2. Perform regular vulnerability assessments.")
            recommendations.append("3. Enhance data encryption practices.")
        else:
            recommendations.append("1. Maintain current practices and conduct regular audits.")
            recommendations.append("2. Stay updated with the latest cybersecurity trends.")
            recommendations.append("3. Encourage a culture of continuous improvement.")
        return recommendations

    def _determine_urgency(self, response):
        if response < 2:
            return "Critical: Immediate action required to address significant vulnerabilities."
        elif response < 4:
            return "Moderate: Address identified risks within the next quarter."
        else:
            return "Low Priority: Continue monitoring and improving practices."