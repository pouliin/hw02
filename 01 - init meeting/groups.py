import random

members = [
    'Андрей',
    'Дмитрий',
    'Кирилл',
    'Лилия',
    'Ринат',
    'Сергей',
    'Александр',
    'Резеда'
]

random.shuffle(members)

groups = []
for i in  range(0, len(members), 2):
    groups.append(members[i:i+2])

# print(groups)
pros = [pair[1] for pair in groups]
# print(pros)


while True:
    random.shuffle(pros)
    groups_with_review = list(zip(groups, pros))
    for pair, pro in groups_with_review:
        if pro in pair:
            break
    else:
        break

print(*groups_with_review, sep='\n')

(['Дмитрий', 'Резеда'], 'Ринат')
(['Андрей', 'Сергей'], 'Александр')
(['Лилия', 'Ринат'], 'Резеда')
(['Кирилл', 'Александр'], 'Сергей')
