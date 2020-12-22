from functools import reduce

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

player_count = player + 1

while all(list(map(lambda deck: len(deck) != 0, decks))):
    cards = list(enumerate(list(map(lambda deck: deck[0], decks))))

    decks[0] = decks[0][1:]
    decks[1] = decks[1][1:]

    cards.sort(key=lambda x: -x[1])
    winner = cards[0][0]

    for card in cards:
        decks[winner].append(card[1])

deck = list(filter(lambda d: len(d) != 0, decks))[0]

res = 0
for i, card in enumerate(deck[::-1]):
    res += (i + 1) * card

print(res)
