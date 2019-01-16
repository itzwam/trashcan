import json
import os

f = open("/tmp/json", "r")
data=f.read()
print(json.loads(data))
