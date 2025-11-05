from random import randrange

list1 = []
list2 = []

for n in range(10):
    list1.append(randrange(10, 101))

for i in range(len(list1)):
    num = list1[i]
    list2.append(num)

list1[9] = -7

print("List 1: ", end="")
for i in range(len(list1)):
    print(list1[i], end=" ")

print("\nList 2: ", end="")
for i in range(len(list2)):
    print(list2[i], end=" ")

# This works too:
# list1 = [5, 6, 7, 8]
# list2 = list1
