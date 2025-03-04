
import os
import string

with open("/Users/ahadtursyn/VS CODE/pp2/lab6/smth.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()