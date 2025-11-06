from random import randrange

list = []

for n in range(10):
    list.append(randrange(1, 51))

print("List: ", end="")
for n in list:
    print(n, end=" ")

print()
to_find = int(input("Value to find: "))

for i in range(len(list)):
    if to_find == list[i]:
        print(f"{to_find} is in the list.")
