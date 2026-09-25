# Write your solution here
word = input("Word: ")
size_of_word = len(word)

left_space_size = (28 - size_of_word) // 2
right_space_size = 0

if size_of_word % 2 != 0:
    right_space_size = left_space_size + 1
else:
    right_space_size = left_space_size

left_white_space = " " * left_space_size
right_white_space = " " * right_space_size

print("*" * 30)
print("*" + left_white_space + word + right_white_space + "*")
print("*" * 30)