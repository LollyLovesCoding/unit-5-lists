from random import randrange

list = []

for i in range(1000):
    list.append(randrange(10, 100))

for i in range(len(list)):
    print(list[i], end="  ")
