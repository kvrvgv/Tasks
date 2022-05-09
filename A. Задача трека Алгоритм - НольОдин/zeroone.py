file = open("input.txt", "r")
input = file.read()[:-1].replace("zero", "0").replace("one", "1").split("\n")
file.close()

if int(input[0], 2) > int(input[1], 2):
    print(">")
elif int(input[0], 2) == int(input[1], 2):
    print("=")
else:
    print("<")
