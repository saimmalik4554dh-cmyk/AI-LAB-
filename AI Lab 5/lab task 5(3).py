def alphabeta(tree, alpha, beta):
    global count

    if isinstance(tree, int):
        count += 1
        return tree

    value = float('-inf')

    for child in tree:
        value = max(value, -alphabeta(child, -beta, -alpha))
        alpha = max(alpha, value)

        if alpha >= beta:
            break

    return value

count = 0
tree = [[3, 5], [2, 9]]

result = alphabeta(tree, float('-inf'), float('inf'))

print("Minimax Value:", result)
print("Leaf Evaluations:", count)

count = 0
tree = [[9, 2], [5, 3]]

result = alphabeta(tree, float('-inf'), float('inf'))

print("Reordered Value:", result)
print("Leaf Evaluations:", count)