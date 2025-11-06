from random import randrange

list = []
found_times = 0

for n in range(10):
    list.append(randrange(1, 51))

print("List: ", end="")
for n in list:
    print(n, end=" ")

print()
to_find = int(input("Value to find: "))

for n in list:
    if to_find == n:
        found_times += 1
        print(f"{to_find} is in the list.")

if found_times == 0:
    print(f"{to_find} is not in the list.")
