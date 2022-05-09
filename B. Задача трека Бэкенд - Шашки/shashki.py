# todo: сделать нормально
# сделать нормально


def test():
    file = open("input.txt", "r")
    input = file.read()[:-1].split("\n")
    file.close()
    SIZEX, SIZEY = map(int, input[0].split())
    WHITE_COUNT = int(input[1])
    BLACK_COUNT = int(input[2 + WHITE_COUNT])
    if input[-1] == "white":
        for i in range(2, 2 + WHITE_COUNT):
            x = int(input[i].split(" ")[0])
            y = int(input[i].split(" ")[1])
            ALL_BLACK = input[3 + WHITE_COUNT:-1]
            if x + 2 <= SIZEX and y + 2 <= SIZEY:
                if f"{x + 1} {y + 1}" in ALL_BLACK:
                    if f"{x + 2} {y + 2}" not in input[1:]:
                        return "Yes"

            if x - 2 > 0 and y - 2 > 0:
                if f"{x - 1} {y - 1}" in ALL_BLACK:
                    if f"{x - 2} {y - 2}" not in input[1:]:
                        return "Yes"

            if x - 2 > 0 and y + 2 <= SIZEY:
                if f"{x - 1} {y + 1}" in ALL_BLACK:
                    if f"{x - 2} {y + 2}" not in input[1:]:
                        return "Yes"

            if y - 2 > 0 and x + 2 <= SIZEX:
                if f"{x + 1} {y - 1}" in ALL_BLACK:
                    if f"{x + 2} {y - 2}" not in input[1:]:
                        return "Yes"

    elif input[-1] == "black":
        for i in range(3 + WHITE_COUNT, 3 + WHITE_COUNT + BLACK_COUNT):
            x = int(input[i].split(" ")[0])
            y = int(input[i].split(" ")[1])
            ALL_WHITE = input[2:2 + WHITE_COUNT]

            if x + 2 <= SIZEX and y + 2 <= SIZEY:
                if f"{x + 1} {y + 1}" in ALL_WHITE:
                    if f"{x + 2} {y + 2}" not in input[1:]:
                        return "Yes"

            if x - 2 > 0 and y - 2 > 0:
                if f"{x - 1} {y - 1}" in ALL_WHITE:
                    if f"{x - 2} {y - 2}" not in input[1:]:
                        return "Yes"

            if x - 2 > 0 and y + 2 <= SIZEY:
                if f"{x - 1} {y + 1}" in ALL_WHITE:
                    if f"{x - 2} {y + 2}" not in input[1:]:
                        return "Yes"

            if y - 2 > 0 and x + 2 <= SIZEX:
                if f"{x + 1} {y - 1}" in ALL_WHITE:
                    if f"{x + 2} {y - 2}" not in input[1:]:
                        return "Yes"
    return "No"


print(test())
