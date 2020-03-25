import random

bingo_list = []
grid_size = 5
bingo_card = []
random_bingo_list = []

with open("bingo.txt", "r") as myfile:      # add file words to bingo list
    for word in myfile:
        bingo_list.append(word)

while len(random_bingo_list) < 25:
    for i in range(len(bingo_list)):            # add words from bingo list to random bingo list
        word = random.choice(bingo_list)        # choose random word from bingo list
        if word in random_bingo_list:           # if word is in random list, do not add and continue
            continue
        else:
            random_bingo_list.append(word)          # if word is not in random list, add to random list

print(random_bingo_list)        # print(random_bingo_list) to show random list

for i in range(len(random_bingo_list)):
    bingo_card = random.choice(random_bingo_list)
    print(str(bingo_card))
