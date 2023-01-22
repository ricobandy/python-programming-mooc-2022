# Write your solution here
num_of_students = int(input("How many students on the course? "))
grp_size = int(input("Desired group size? "))
num_of_grp = (num_of_students + grp_size - 1) // grp_size
print(f"Number of groups formed: {num_of_grp}")