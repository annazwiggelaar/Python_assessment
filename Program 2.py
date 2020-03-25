import random
rwg = random.Random()
bingo_list = []
random_bingo_list = []

with open("bingo.txt", "r") as myfile:      # add words from file to bingo list
    for word in myfile:
        bingo_list.append(word)

for i in range(len(bingo_list)):            # add words from bingo list to random bingo list if not in random list yet
    word = random.choice(bingo_list)        # choose random word from bingo list
    if word in random_bingo_list:           # if word is in random list, do not add and continue
        continue
    else:
        random_bingo_list.append(word)          # if word is not in random list, add to random list
        answer = input("Are you ready to see the word? ")
        if answer == "yes":
            print(word)










