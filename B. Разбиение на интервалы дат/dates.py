# todo: сделать нормально, выяснить что за ошибка в TYPE == QUARTER вроде
# сделать нормально, выяснить что за ошибка в TYPE == QUARTER вроде


import datetime


file = open("input.txt", "r")
INPUT = file.read().split("\n")
file.close()

TYPE = INPUT[0]
DATES = INPUT[1].split(" ")

START_DATE = datetime.datetime.strptime(DATES[0], "%Y-%m-%d")
FINISH_DATE = datetime.datetime.strptime(DATES[1], "%Y-%m-%d")

OUTPUT = DATES[0]

while START_DATE < FINISH_DATE:
    if TYPE == "MONTH":
        MONTH = str(START_DATE).split("-")[1]
        while str(START_DATE).split("-")[1] == MONTH and START_DATE <= FINISH_DATE:
            START_DATE += datetime.timedelta(1)
        OUTPUT += f" {str(START_DATE - datetime.timedelta(1))[:-9]}\n"
        if START_DATE < FINISH_DATE:
            OUTPUT += str(START_DATE)[:-9]
        else:
            OUTPUT = OUTPUT[:-1]

    elif TYPE == "WEEK":
        while START_DATE.weekday() != 6:
            START_DATE += datetime.timedelta(1)
        OUTPUT += f" {str(START_DATE)[:-9]}\n"
        START_DATE += datetime.timedelta(1)
        if START_DATE <= FINISH_DATE:
            OUTPUT += str(START_DATE)[:-9]
            if START_DATE == FINISH_DATE:
                OUTPUT += f" {str(START_DATE)[:-9]}"

    elif TYPE == "REVIEW":
        while str(START_DATE)[5:-9] != "09-30" and str(START_DATE)[5:-9] != "03-31" and START_DATE < FINISH_DATE:
            START_DATE += datetime.timedelta(1)
        OUTPUT += f" {str(START_DATE)[:-9]}\n"
        START_DATE += datetime.timedelta(1)
        if START_DATE < FINISH_DATE:
            OUTPUT += str(START_DATE)[:-9]
        else:
            OUTPUT = OUTPUT[:-1]

    elif TYPE == "YEAR":
        CUR_YEAR = int(str(START_DATE)[:4])
        while int(str(START_DATE)[:4]) <= CUR_YEAR:
            START_DATE += datetime.timedelta(1)
        if START_DATE <= FINISH_DATE:
            OUTPUT += f" {str(START_DATE - datetime.timedelta(1))[:-9]}\n"
            OUTPUT += str(START_DATE)[:-9]
        else:
            OUTPUT += f" {str(FINISH_DATE)[:-9]}"

    elif TYPE == "QUARTER":
        while str(START_DATE)[5:-9] != "01-01" and str(START_DATE)[5:-9] != "04-01" \
                and str(START_DATE)[5:-9] != "07-01" and str(START_DATE)[5:-9] != "10-01":
            START_DATE += datetime.timedelta(1)
        if START_DATE - datetime.timedelta(1) < FINISH_DATE:
            OUTPUT += f" {str(START_DATE - datetime.timedelta(1))[:-9]}\n"
        else:
            OUTPUT += f" {str(FINISH_DATE)[:-9]}"
        if START_DATE < FINISH_DATE:
            OUTPUT += str(START_DATE)[:-9]
        if START_DATE == FINISH_DATE:
            OUTPUT += str(START_DATE)[:-9]
            while str(START_DATE)[5:-9] != "01-01" and str(START_DATE)[5:-9] != "04-01" \
                    and str(START_DATE)[5:-9] != "07-01" and str(START_DATE)[5:-9] != "10-01" or str(FINISH_DATE)[5:-9] == str(START_DATE)[5:-9]:
                START_DATE += datetime.timedelta(1)
            START_DATE -= datetime.timedelta(1)
            OUTPUT += f" {str(START_DATE)[:-9]}"
        START_DATE += datetime.timedelta(1)

COUNT = len(OUTPUT.split("\n"))
print(f"{COUNT}\n{OUTPUT}")
