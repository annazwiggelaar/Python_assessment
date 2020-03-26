# Program by Anna Zwiggelaar and Lieke Spoelstra.

list_of_terms = []
words_added = []

while len(list_of_terms) < 35:
    new_word = input("Please enter a word: ")
    words_added.append(new_word)
    if new_word in list_of_terms:
        print("You have already added this word, please add a different one.")
        continue
    else:
        list_of_terms.append(new_word)

print("Thank you! Please proceed to the next program.")

with open("bingo.txt", "a") as bingo_file:
    for word in list_of_terms:
        bingo_file.write(word)
        bingo_file.write("\n")

frequencies = {}
for word in words_added:
    frequencies[word] = frequencies.get(word, 0) + 1

print(frequencies)
