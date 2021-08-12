import json
filename='numbers.json'
with open(filename,'r') as f:
    print(json.load(f))