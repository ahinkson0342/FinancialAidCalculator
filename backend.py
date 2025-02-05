# backend.py

def calculate(total_credit, current_credit, target_gpa, current_gpa):
    """
    Calculates the required GPA for remaining credits to achieve the target GPA.

    :param total_credit: Total credits needed for graduation
    :param current_credit: Credits already completed
    :param target_gpa: The desired GPA upon graduation
    :param current_gpa: The current GPA based on completed credits
    :return: Required GPA for remaining credits or a message if not possible
    """
    if current_credit > total_credit:
        return "Error: Current credits cannot exceed total credits."

    if current_gpa > 4.0 or target_gpa > 4.0 or current_gpa < 0 or target_gpa < 0:
        return "Error: GPA must be between 0 and 4.0."

    remaining_credit = total_credit - current_credit

    # If no remaining credits, check if the target GPA is already achieved
    if remaining_credit == 0:
        return "Target GPA already achieved!" if current_gpa >= target_gpa else "Target GPA not achievable."

    # Calculate the required GPA for remaining credits
    required_gpa = ((target_gpa * total_credit) - (current_gpa * current_credit)) / remaining_credit

    # Ensure GPA is within possible bounds
    if required_gpa > 4.0:
        return "Not possible to achieve target GPA."

    return max(0.0, required_gpa)  # GPA should not be negative
