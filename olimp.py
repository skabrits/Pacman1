from sys import stdin

train = ""
n = int(input())
for line in stdin:
    commands = line.split(" ")
    if commands[0] == "add":
        for i in range(int(commands[1])):
            train.append(commands[2])
    elif commands[0] == "delete":
        train = train[:len(train)-int(commands[1])]
    elif commands[0] == "get":
        n = 0
        for j in train:
            if j == commands[1]:
                n += 1
        print(n)