from datetime import datetime

date1 = datetime(2025, 2, 13, 12, 0, 0)
date2 = datetime(2025, 2, 10, 8, 30, 0)

difference = (date1 - date2).total_seconds()

print("Difference in seconds:", difference)
