from datetime import datetime

now = datetime.now()

clean_time = now.replace(microsecond=0)

print("Original:", now)
print("Without Microseconds:", clean_time)