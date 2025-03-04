import re

text = "SplitThisString"
result = re.split(r"(?=[A-Z])", text)
print(result)
