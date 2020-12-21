from copy import deepcopy

all_ingredients = []
rules = []
mapping = {}


with open('file.in', 'rt') as fin:
    lines = list(map(lambda line: line.strip(), fin.readlines()))


def get_rules(rules):
    new_rules = []
    for i in range(len(rules) - 1):
        for j in range(i + 1, len(rules)):
            ingredients_i, allergens_i = rules[i]
            ingredients_j, allergens_j = rules[j]

            ingredients = ingredients_i.intersection(ingredients_j)
            allergens = allergens_i.intersection(allergens_j)

            if len(allergens) != 0 and len(ingredients) != 0:
                if (ingredients, allergens) not in rules and (ingredients, allergens) not in new_rules:
                    new_rules.append((ingredients, allergens))
    print(len(new_rules))
    if len(new_rules) == 0:
        return new_rules

    return rules + new_rules + get_rules(new_rules)


for line in lines:
    left, right = line.split('(contains')
    ingredients = set(left.strip().split(' '))
    allergens = set((map(lambda x: x.strip(), right[:-1].split(','))))

    rules.append((ingredients, allergens))

    for ingredient in ingredients:
        all_ingredients.append(ingredient)

rules = get_rules(rules)

while len(rules) != 0:
    for ingredients, allergens in rules:
        if len(ingredients) == 1:
            ingredient = list(ingredients)[0]
            allergen = list(allergens)[0]

            mapping[ingredient] = allergen

    for ingredient, allergen in mapping.items():
        for i in range(len(rules)):
            ingredients, allergens = rules[i]

            if ingredient in ingredients:
                ingredients.remove(ingredient)
                allergens.discard(allergen)

    new_rules = []
    for ingredients, allergens in rules:
        if len(ingredients) != 0 and len(allergens) != 0:
            new_rules.append((ingredients, allergens))
    rules = new_rules

res = 0
for ingredient in set(all_ingredients):
    if ingredient not in mapping:
        res += all_ingredients.count(ingredient)

dangerous_ingredients = []
for k, v in mapping.items():
    dangerous_ingredients.append((k, v))

dangerous_ingredients.sort(key=lambda x: x[1])

print(','.join(list(map(lambda x: x[0], dangerous_ingredients))))
