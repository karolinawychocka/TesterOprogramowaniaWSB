#tuple - used for grouping together data, unchangeable


student = ("Kasia", 22, "female")

print(student.count("Kasia"))
print(student.index("female"))

for i in student:
    print(i)

if "Kasia" in student:
    print("Kasia is here!")