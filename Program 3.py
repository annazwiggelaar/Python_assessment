import random

bingo_list = []
random_bingo_list = []

with open("bingo.txt", "r") as myfile:      # add file words to bingo list
    for word in myfile:
        bingo_list.append(word)

for i in range(len(bingo_list)):
    while len(random_bingo_list) < 25:          # while nr of words in random list is under 25
        word = random.choice(bingo_list)        # choose random word from bingo list
        if word in random_bingo_list:           # if word is in random list, do not add and continue
            continue
        else:
            random_bingo_list.append(word)          # if word is not in random list, add to random list

print(random_bingo_list)        # print(random_bingo_list) to show random list

# explain how user should input coordinates

x = random_bingo_list
a = 0

bingo_card = [[x[a], x[a + 1], x[a + 2], x[a + 3], x[a + 4]], [x[a + 5], x[a + 6], x[a + 7], x[a + 8], x[a + 9]],
              [x[a + 10], x[a + 11], x[a + 12], x[a + 13], x[a + 14]],
              [x[a + 15], x[a + 16], x[a + 17], x[a + 18], x[a + 19]],
              [x[a + 20], x[a + 21], x[a + 22], x[a + 23], x[a + 24]]]
print(bingo_card[0], "\n", bingo_card[1], "\n", bingo_card[2], "\n", bingo_card[3], "\n", bingo_card[4])

x_coordinate = int(input("Please enter the first coordinate of the word that was called. (x-axis) "))
y_coordinate = int(input("Please enter the second coordinate of the word that was called. (y-axis) "))

string = bingo_card
part = bingo_card[x_coordinate][y_coordinate]


def red(z):
    return "\033[91m {}\033[00m" .format(z)         # color code found online


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


print(strike("Hello"))


for _ in bingo_card:
    if part in bingo_card:
        print(strike(bingo_card[x_coordinate][y_coordinate]), bingo_card[0], "\n", bingo_card[1], "\n", bingo_card[2],
              "\n", bingo_card[3], "\n", bingo_card[4])


e = bingo_card[x_coordinate][y_coordinate]

print(red(e), bingo_card[0], "\n", bingo_card[1], "\n", bingo_card[2], "\n", bingo_card[3], "\n", bingo_card[4])

print(red(e))
