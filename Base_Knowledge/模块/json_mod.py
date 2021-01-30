import json

dic = {
    'name': 'Hong',
    'age': 18,
}

f = open("info.json", "w")
json.dump(dic, f)

f = open("info.json", "r")
print(json.load(f))