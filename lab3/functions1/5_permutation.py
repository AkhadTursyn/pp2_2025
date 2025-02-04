from itertools import permutations

def print_permutations(s):
    for p in permutations(s):
        print("".join(p))

print_permutations("abc")
