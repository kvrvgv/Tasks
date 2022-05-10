# вывод такой же по ключам, но ключи в тексте задачи поменяны местами, наверное не критично =)


import json


file = open("input.txt", "r")
INPUT = file.read().split("\n")
file.close()

output = json.loads(INPUT[1])

for i in INPUT[2:]:
    output["offers"].append(json.loads(i)["offers"][0])

print(output)
