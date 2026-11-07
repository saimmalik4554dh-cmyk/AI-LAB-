P1 = ["Accurate delivery", "Safety", "Fast delivery"]
E1 = ["Roads", "Pedestrians", "Buildings"]
A1 = ["Wheels", "Motors", "Brakes"]
S1 = ["Camera", "GPS", "LiDAR"]

print("Delivery Robot PEAS")

P2 = ["Accurate answers", "Fast response", "Privacy"]
E2 = ["Students", "Course materials", "University portal"]
A2 = ["Text responses", "Study guidance", "Support tickets"]
S2 = ["Student queries", "FAQs", "Documents", "Timetable API"]

print("Student Support Agent PEAS")

assumptions = [
    "Access to university FAQs",
    "Access to course notes",
    "Access to academic calendar",
    "Read-only timetable and enrolment APIs",
    "Can create support tickets",
    "Cannot change student grades"
]

print("Operational Assumptions:", assumptions)

print("Delivery Robot Trade-off: Speed vs Safety")
print("Student Agent Trade-off: Accuracy vs Privacy")