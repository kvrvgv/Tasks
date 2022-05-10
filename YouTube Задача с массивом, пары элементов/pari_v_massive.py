# Найти элемент без пары, такой элемент всего 1


import json


file = open("input.txt", "r")
INPUT = json.loads(file.read())
file.close()

while INPUT:
    item = INPUT[0]
    INPUT.remove(item)
    try:
        INPUT.remove(item)
    except:
        print(item)
