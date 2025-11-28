# Q1
animals = "monkey bat cat dog"
for animal in animals.split():
    print(animal)

# Q2
integers_str = "65, 75, 32, 22"
integers_list = integers_str.split(", ")
for i in range(len(integers_list)):
    print(f"{i}: {integers_list[i]}")

# Q3
num_str = "one,two,three,four"
num_list = num_str.split(",")
num_list2 = []
for num in num_list:
    if num == "one":
        num_list2.append(1)
    elif num == "two":
        num_list2.append(2)
    elif num == "three":
        num_list2.append(3)
    else:
        num_list2.append(4)

print(num_list2)

# Q4
unrefined_str = "W W L T T W"
refined_list = []

for stat in unrefined_str.split():
    if stat == "W":
        refined_list.append(2)
    elif stat == "L":
        refined_list.append(0)
    else:
        refined_list.append(1)

print(refined_list)

# Q5
unrefined_str = "x:3,x:6,x:14,x:22"
refined_list = []

for n in unrefined_str.split(","):
    num = n.split(":")[1]
    refined_list.append(int(num))

print(refined_list)

# Q6
unrefined_str = "x:2,y:5 - x:5,y:11 - x:7,y:14"
unrefined_list = unrefined_str.split(" - ")
refined_list = []

for n in unrefined_list:
    parts = n.split(",")
    x = parts[0].split(":")[1]
    y = parts[1].split(":")[1]
    refined_list.append([int(x), int(y)])

print(refined_list)

