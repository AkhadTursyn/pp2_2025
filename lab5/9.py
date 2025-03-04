import re

text = "InsertSpacesBetweenWords"

result = re.sub(r"(\w)([A-Z])", r"\1 \2", text)
print(result)
