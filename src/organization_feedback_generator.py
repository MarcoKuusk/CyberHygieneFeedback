from utils.scoring import calculate_organization_score

class OrganizationFeedbackGenerator:
    def __init__(self, organization_responses):
        self.organization_responses = organization_responses
        self.security_domains = {
            "Access Management & Authentication": [],
            "Employee Awareness & Training": [],
            "Incident Response & Reporting": [],
            "Secure Communication & Remote Work": []
        }

    def generate_feedback(self):
        feedback = []
        total_score = calculate_organization_score(self.organization_responses)
        feedback.append(f"Overall Organization Cyber Hygiene Score: {total_score:.2f}% (Moderate Risk – Immediate improvements recommended in key areas)")

        self._categorize_responses()

        feedback.append(self._generate_summary())

        for domain, responses in self.security_domains.items():
            domain_score = self._calculate_domain_score(responses)
            feedback.append(f"\n{domain}\nScore: {domain_score:.2f}%")
            feedback.append(self._generate_domain_feedback(domain, responses))

        return feedback

    def _categorize_responses(self):
        for question, response in self.organization_responses.items():
            if "access" in question.lower() or "authentication" in question.lower():
                self.security_domains["Access Management & Authentication"].append((question, response))
            elif "training" in question.lower() or "awareness" in question.lower():
                self.security_domains["Employee Awareness & Training"].append((question, response))
            elif "incident" in question.lower() or "reporting" in question.lower():
                self.security_domains["Incident Response & Reporting"].append((question, response))
            elif "communication" in question.lower() or "remote" in question.lower():
                self.security_domains["Secure Communication & Remote Work"].append((question, response))

    def _calculate_domain_score(self, responses):
        total_score = sum(response for _, response in responses)
        max_score = len(responses) * 4  # Assuming each question is scored out of 4
        return (total_score / max_score) * 100 if max_score > 0 else 0

    def _generate_summary(self):
        summary = []
        summary.append("Summary of Key Findings:")
        summary.append("The organization has moderate security controls, but significant gaps exist in employee training, incident response planning, and access management. Immediate focus should be placed on strengthening phishing awareness, reporting mechanisms, and authentication methods.")
        summary.append("\nKey Areas of Concern:")
        for domain, responses in self.security_domains.items():
            domain_score = self._calculate_domain_score(responses)
            if domain_score < 50:
                summary.append(f"{domain}: Score {domain_score:.2f}% - Immediate improvements needed.")
        return "\n".join(summary)

    def _generate_domain_feedback(self, domain, responses):
        feedback = []
        high_risk_responses = [resp for resp in responses if resp[1] < 2]
        moderate_risk_responses = [resp for resp in responses if 2 <= resp[1] < 4]
        low_risk_responses = [resp for resp in responses if resp[1] >= 4]

        if high_risk_responses:
            feedback.append("High Risk Areas:")
            for question, response in high_risk_responses:
                feedback.append(self._evaluate_response(question, response, "Critical – Immediate action required within 30 days"))

        if moderate_risk_responses:
            feedback.append("Moderate Risk Areas:")
            for question, response in moderate_risk_responses:
                feedback.append(self._evaluate_response(question, response, "Moderate – Address within 60 days"))

        if low_risk_responses:
            feedback.append("Low Risk Areas:")
            for question, response in low_risk_responses:
                feedback.append(self._evaluate_response(question, response, "Low Priority – Address within 90 days"))

        return "\n".join(feedback)

    def _evaluate_response(self, question, response, priority):
        feedback = []
        feedback.append(f"Assessment of Current Security Posture for '{question}':")
        feedback.append(f"Score: {response}")
        feedback.append(self._interpret_response(response))
        feedback.append("Identified Weaknesses & Risks:")
        feedback.append(self._identify_risks(question, response))
        feedback.append("Recommended Improvements:")
        feedback.extend(self._recommend_improvements(question, response))
        feedback.append(f"Priority Level: {priority}")
        return "\n".join(feedback)

    def _interpret_response(self, response):
        return f"Response {response} suggests strong practices are in place." if response >= 4 else f"Response {response} indicates a need for improvement."

    def _identify_risks(self, question, response):
        if response < 2:
            if "phishing" in question.lower():
                return "Without phishing simulations, employees may be unable to detect social engineering attempts, increasing the risk of credential theft and malware infections."
            elif "incident" in question.lower():
                return "Lack of an incident response plan can lead to delayed detection and response to security breaches, increasing potential damage."
            elif "access" in question.lower():
                return "Weak access controls increase the risk of unauthorized access and credential theft."
            else:
                return "There are significant vulnerabilities that could be exploited by attackers."
        elif response < 4:
            return "Some risks exist that could be mitigated with better practices."
        else:
            return "Minimal risks, but continuous monitoring is recommended."

    def _recommend_improvements(self, question, response):
        recommendations = []
        if response < 2:
            if "phishing" in question.lower():
                recommendations.append("1. Conduct simulated phishing tests quarterly and analyze employee responses to tailor future training.")
                recommendations.append("2. Implement mandatory phishing awareness training within 45 days.")
            elif "incident" in question.lower():
                recommendations.append("1. Develop and implement an incident response plan within 30 days.")
                recommendations.append("2. Conduct security drills for key staff to improve response times.")
                recommendations.append("3. Establish an easy-to-use reporting mechanism for employees.")
            elif "access" in question.lower():
                recommendations.append("1. Implement multi-factor authentication (MFA) for all high-risk accounts within 30 days.")
                recommendations.append("2. Implement a centralized password management policy within 60 days.")
                recommendations.append("3. Enforce strong password complexity requirements within 90 days.")
            else:
                recommendations.append("1. Implement multi-factor authentication (MFA) for all accounts within 30 days.")
                recommendations.append("2. Conduct regular security awareness training for employees within 45 days.")
                recommendations.append("3. Establish a formal incident response plan within 30 days.")
        elif response < 4:
            recommendations.append("1. Review and update access controls regularly within 60 days.")
            recommendations.append("2. Perform regular vulnerability assessments within 60 days.")
            recommendations.append("3. Enhance data encryption practices within 90 days.")
        else:
            recommendations.append("1. Maintain current practices and conduct regular audits within 90 days.")
            recommendations.append("2. Stay updated with the latest cybersecurity trends within 90 days.")
            recommendations.append("3. Encourage a culture of continuous improvement within 90 days.")
        return recommendations