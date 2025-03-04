import re

text = "Hello, world. How are you?"
result = re.sub(r"[\s,.]", ":", text)

print(result)
