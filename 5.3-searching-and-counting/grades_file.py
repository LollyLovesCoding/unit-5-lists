from random import randrange

grades = []

name = input("Name (first last): ")
print("Filename: marks.txt\n")

print("Here are your randomly-selected grades (hope you pass):")
for i in range(5):
    grade = randrange(1, 101)
    grades.append(grade)
    print(f"Grade {i + 1}: {grade}")

with open("marks.txt", "w") as file:
    file.write(f"{name}\n")
    for grade in grades:
        file.write(f"{grade}")
        file.write(" ")

print('Data saved in "marks.txt".')
