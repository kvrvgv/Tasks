# todo: это заготовка. доделать!
# это заготовка. доделать!
# https://contest.yandex.ru/contest/32757/problems/E/


import sys


def server_answer(time, UserID):
    pass


file = open("input.txt", "r")
INPUT = file.read().split("\n")
file.close()

userLimit = INPUT[0].split(' ')[0]
serverLimit = INPUT[0].split(' ')[1]
duration = INPUT[0].split(' ')[2]
INPUT = INPUT[1:-2]

for request in INPUT:
    time, UserID = map(int, request.split())
    print(server_answer(time, UserID))
    sys.stdout.flush()
