from random import randrange

list = []
largest = 0
index = 0

print("List: ", end="")
for i in range(10):
    num = randrange(1, 51)
    list.append(num)
    print(num, end=" ")

for i in range(len(list)):
    if largest < list[i]:
        largest = list[i]
        index = i

print(f"\nThe largest value is {largest}\nIt is at index {index}")
