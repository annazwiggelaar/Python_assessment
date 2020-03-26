# Program by Anna Zwiggelaar and Lieke Spoelstra.

import random

print("This program will draw words at random. The next program contains "
      "your bingo card.\nIf one of the words drawn here is on your bingo "
      "card, you can cross it off in the next program.\nPlease answer "
      "'yes' when you are ready to see the word.")

bingo_list = []
random_bingo_list = []
terms_drawn = 0

with open("bingo.txt", "r") as myfile:      # add words from file to bingo list
    for word in myfile:
        bingo_list.append(word)

while terms_drawn < 35:            # add words from bingo list to random bingo list if not in random list yet
    word = random.choice(bingo_list)        # choose random word from bingo list
    if word in random_bingo_list:           # if word is in random list, do not add and continue
        continue
    else:
        random_bingo_list.append(word)          # if word is not in random list, add to random list
        terms_drawn += 1
        answer = input("Are you ready to see the word? ")
        if answer == "yes":
            print(word)










