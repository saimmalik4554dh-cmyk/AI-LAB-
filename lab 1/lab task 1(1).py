P1 = ["Accurate delivery", "Safety", "Fast delivery"]
E1 = ["Roads", "Pedestrians", "Buildings"]
A1 = ["Wheels", "Motors", "Brakes"]
S1 = ["Camera", "GPS", "LiDAR"]

P2 = ["Accurate answers", "Fast response", "Privacy"]
E2 = ["Students", "Course materials", "University portal"]
A2 = ["Text responses", "Study guidance", "Support tickets"]
S2 = ["Student queries", "FAQs", "Documents", "Timetable API"]

assumptions = [
    "University FAQs",
    "Course notes",
    "Academic calendar",
    "Read-only timetable API",
    "Enrolment records",
    "Support ticket system"
]

print("Delivery Robot PEAS:", P1, E1, A1, S1)
print("Student Agent PEAS:", P2, E2, A2, S2)
print("Assumptions:", assumptions)
print("Delivery Trade-off: Speed vs Safety")
print("Student Agent Trade-off: Accuracy vs Privacy")