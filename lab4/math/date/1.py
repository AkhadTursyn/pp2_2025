import datetime


x = datetime.datetime.now().date()
y = x - datetime.timedelta(days=5)
print(y)
