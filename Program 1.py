list_of_terms = []

for _ in range(35):
    new_word = input("Please enter a word: ")
    list_of_terms.append(new_word)

print(list_of_terms)

with open("bingo.txt", "w") as bingo_file:
    for word in list_of_terms:
        bingo_file.write(word)
        bingo_file.write("\n")

