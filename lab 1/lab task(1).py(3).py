def is_eligible(gpa, income, citizen):
    return gpa >= 3.5 and income < 40000 and citizen

def bot_says_yes(gpa, income, citizen):
    return gpa >= 3.4 and income < 40000

students = [
    (3.4, 38000, True),
    (3.5, 39999, True),
    (3.49, 30000, True),
    (3.6, 40000, True),
    (3.8, 20000, False),
    (3.5, 10000, True),
]

print("Bot reply: Great news! You qualify.")
print("Real answer for 3.4 GPA:", is_eligible(3.4, 38000, True))

right = 0
for s in students:
    if bot_says_yes(*s) == is_eligible(*s):
        right += 1

print("Bot got", right, "out of", len(students), "right")