# Write your solution here
story = ""
prev_word = ""

while True:
    word = input("Please type in a word: ")

    if word == "end" or word == prev_word:
        break
    else:
        story = story + word + " "
        prev_word = word

print(story)