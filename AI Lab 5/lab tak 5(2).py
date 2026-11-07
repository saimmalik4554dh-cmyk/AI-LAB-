count = 0

def evaluate(value):
    global count
    count += 1
    return value

def minimax():
    A = max(evaluate(3), evaluate(5))
    B = max(evaluate(2), evaluate(9))
    return min(A, B)

result = minimax()

print("Minimax Value:", result)
print("Leaf Evaluations:", count)