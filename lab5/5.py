import re

pattern = r"a.*b$"
test_strings = ["ab", "acb", "a123b", "a_b", "abc"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")