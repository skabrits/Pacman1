from sys import stdin

towns = list()
n,k = tuple(map(int, input().split(" ")))
for line in stdin:
    commands = line.split(" ")
    if commands[0] == "+":
        for i in range(int(commands[1])):
            train.append(commands[2])
    elif commands[0] == "-":
        train = train[:len(train)-int(commands[1])]
    elif commands[0] == "?":
        n = 0
        for j in train:
            if j == commands[1]:
                n += 1
        print(n)