import re

pattern = r"^[a-z]+_[a-z]+$"
test_strings = ["hello_world", "helloWorld", "test_data", "Test_Data"]

for i in test_strings:
    if re.fullmatch(pattern, i):
        print(f"Matched: {i}")