# main.py
from backend import calculate

def test_calculator():
    """Runs test cases for the calculate function."""

    test_cases = [
        # Case 1: Normal scenario - user can achieve target GPA
        (90, 45, 2.0, 1.5),   # Should return a reasonable GPA

        # Case 2: Already at target GPA
        (90, 90, 2.0, 2.0),   # Should return "Target GPA already achieved!"

        # Case 3: Exceeding max GPA (Not achievable)
        (90, 80, 2.0, 1.0),   # Should return "Not possible to achieve target GPA."

        # Case 4: More credits completed than required (Invalid input)
        (90, 100, 2.0, 2.5),  # Should return error message

        # Case 5: GPA exceeds 4.0 (Invalid input)
        (90, 50, 2.0, 4.5),   # Should return error message

        # Case 6: Current GPA is too low to reach target GPA
        (180, 150, 2.0, 1.0), # Should return "Not possible to achieve target GPA."

        # Case 7: Current GPA is 0, target is 2.0 (should be possible)
        (180, 90, 2.0, 0.0),  # Should return required GPA

        # Case 8: All credits left to take (Target GPA = Required GPA)
        (180, 0, 2.0, 0.0),   # Should return 2.0 exactly

        # Case 9: Only one credit remaining
        (180, 179, 2.0, 1.9), # Should return a slightly higher required GPA

        # Case 10: Perfect GPA scenario (should return 0.0, already above target)
        (90, 50, 2.0, 3.0),   # Should return 0.0, as target GPA is already surpassed
    ]

    for i, (total_credit, current_credit, target_gpa, current_gpa) in enumerate(test_cases, start=1):
        result = calculate(total_credit, current_credit, target_gpa, current_gpa)
        print(f"Test {i}: calculate({total_credit}, {current_credit}, {target_gpa}, {current_gpa}) -> {result}")

if __name__ == "__main__":
    test_calculator()
