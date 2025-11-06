from random import randrange

list = []
found_times = 0

print("Array: ", end="")
for i in range(10):
    num = randrange(1, 51)
    list.append(num)
    print(num, end=" ")

print(f"\nThe largest value is {max(list)}")
