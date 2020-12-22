from copy import deepcopy
import sys

sys.setrecursionlimit(15000)


def hash_deck(decks):
    return ':'.join(list(map(lambda deck: ','.join(list(map(lambda card: str(card), deck))), decks)))


def recursive_combat(decks, history):
    hashed_deck = hash_deck(decks)

    if hashed_deck in history:
        return 0

    history.add(hashed_deck)

    if len(decks[0]) == 0:
        return 1
    if len(decks[1]) == 0:
        return 0

    player_0_card = decks[0][0]
    player_1_card = decks[1][0]
    decks[0] = decks[0][1:]
    decks[1] = decks[1][1:]

    if len(decks[0]) >= player_0_card and len(decks[1]) >= player_1_card:
        new_decks = deepcopy(
            [decks[0][:player_0_card], decks[1][:player_1_card]])
        winner = recursive_combat(new_decks, set())
    else:
        winner = 1

        if player_0_card > player_1_card:
            winner = 0

    if winner == 0:
        decks[0] += [player_0_card, player_1_card]
    else:
        decks[1] += [player_1_card, player_0_card]

    return recursive_combat(decks, history)


with open('file.in', 'rt') as fin:
    lines = list(filter(lambda e: e != '', list(
        map(lambda line: line.strip(), fin.readlines()))))

decks = []
player = -1
i = 0

while i < len(lines):
    line = lines[i]

    if line.split(' ')[0] == 'Player':
        player += 1
        decks.append([])
    else:
        decks[player].append(int(line))

    i += 1

recursive_combat(decks, set())
deck = list(filter(lambda d: len(d) != 0, decks))[0]

res = 0
for i, card in enumerate(deck[::-1]):
    res += (i + 1) * card

print(res)
