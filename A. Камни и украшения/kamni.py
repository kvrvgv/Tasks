file = open("input.txt", "r")
input = file.read().split("\n")
file.close()

count = 0
for i in input[1]:
    if i in input[0]:
        count += 1
print(count)
