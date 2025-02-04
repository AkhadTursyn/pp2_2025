def calculator_animal(head, leg):
    x = (4 * head - leg) // 2
    y = head - x

    if x < 0 or y < 0 or (2 * x + 4 * y) != leg:
        return "No solution"
    
    return f"Chickens: {x}, Rabbits: {y}"

head = int(input("How many heads: "))
leg = int(input("How many legs: "))

print(calculator_animal(head, leg))