# https://www.codewars.com/kata/626d691649cb3c7acd63457b


def champion_rank(pilot, events):
    places = list(range(1, 21))
    for p, event in zip(*([iter(events.split())] * 2)):
        if event == 'I':
            places.pop(places.index(int(p)))
        else:
            places.insert(places.index(int(p)) - 1, places.pop(places.index(int(p))))
    if pilot not in places:
        return -1

    return places.index(pilot) + 1


print(champion_rank(3, ""), 3)
print(champion_rank(11, "1 I 12 O 11 I"), -1)
print(champion_rank(8, "8 O 14 O 18 I 7 O 14 O 8 O 20 O 20 I 10 O 10 I"), 7)
print(champion_rank(11, "1 I 12 O 13 O 14 O 15 O"), 14)
