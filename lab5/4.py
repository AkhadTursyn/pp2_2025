import re

pattern = r"^[A-Z][a-z]+"
test_strings = ["Hello", "hello", "Test", "TEST", "Python"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")
        