def check_eligibility(score, complete, attendance, approved):
    if score < 70:
        return False, "Score below 70"
    if not complete:
        return False, "Documents incomplete"
    if attendance < 75:
        return False, "Attendance below 75%"
    if not approved:
        return False, "Approval condition not met"
    return True, "All conditions passed"


tests = [
    (85, True, 90, True, True),    # Pass
    (80, True, 60, True, False),   # Attendance failure
    (90, True, 85, False, False),  # Approval failure
    (70, True, 80, True, True)     # Boundary score
]

for i, (score, complete, attendance, approved, expected) in enumerate(tests, 1):
    actual, reason = check_eligibility(score, complete, attendance, approved)

    print(f"\nTest Case {i}")
    print("Input:", score, complete, attendance, approved)
    print("Expected:", expected)
    print("Actual:", actual)
    print("Reason:", reason)