import re

snake_to_camel = ("hello_world_example")
result = re.sub(r"([a-z])(_)([a-z])" , r"\1\3", snake_to_camel)

print(result)