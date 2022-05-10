# не загружал в яндекс (нет тестов), но вроде должно работать так


import requests


file = open("input.txt", "r")
INPUT = file.read().split("\n")
file.close()

for i in sorted(requests.get(f"{INPUT[0]}:{INPUT[1]}/?a={INPUT[2]}&b={INPUT[3]}").json()):
    print(i)
