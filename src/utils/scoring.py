def calculate_employee_score(responses):
    total_score = 0
    max_score = 0

    for score in responses.values():
        total_score += score
        max_score += 4  # Assuming each question is scored out of 4

    return (total_score / max_score) * 100 if max_score > 0 else 0


def calculate_organization_score(responses):
    total_score = 0
    max_score = 0

    for score in responses.values():
        total_score += score
        max_score += 4  # Assuming each question is scored out of 4

    return (total_score / max_score) * 100 if max_score > 0 else 0

def calculate_unified_score(org_score, emp_score, org_weight=0.5, emp_weight=0.5):
    return (org_score * org_weight) + (emp_score * emp_weight)