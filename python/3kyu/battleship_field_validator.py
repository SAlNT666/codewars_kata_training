# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

def validate_battlefield(battleField):

    ships_dict = {1: [], 2: [], 3: [], 4: []}
    units = set()

    for i, row in enumerate(battleField):
        for j, elem in enumerate(row):
            if elem:
                units.add((i, j))

    for unit in units:
        if (unit[0] + 1, unit[1]) in units:

            if (unit[0] + 2, unit[1]) in units:

                if (unit[0] + 3, unit[1]) in units:
                    ships_dict[4].append(((unit[0], unit[1]), (unit[0] + 1, unit[1]),
                                          (unit[0] + 2, unit[1]), (unit[0] + 3, unit[1])))
                    continue

                if not {(unit[0] - 1, unit[1]),
                        (unit[0] - 1, unit[1] - 1), (unit[0] - 1, unit[1] + 1), (unit[0] + 1, unit[1] - 1), (unit[0] + 1, unit[1] + 1)}.intersection(units):
                    ships_dict[3].append(((unit[0], unit[1]), (unit[0] + 1, unit[1]), (unit[0] + 2, unit[1])))
                continue

            if not {(unit[0] - 1, unit[1]),
                    (unit[0] - 1, unit[1] - 1), (unit[0] - 1, unit[1] + 1), (unit[0] + 1, unit[1] - 1), (unit[0] + 1, unit[1] + 1)}.intersection(units):
                ships_dict[2].append(((unit[0], unit[1]), (unit[0] + 1, unit[1])))

            continue

        if (unit[0], unit[1] + 1) in units:

            if (unit[0], unit[1] + 2) in units:

                if (unit[0], unit[1] + 3) in units:

                    ships_dict[4].append(((unit[0], unit[1]), (unit[0], unit[1] + 1),
                                          (unit[0], unit[1] + 2), (unit[0], unit[1] + 3)))
                    continue

                if not {(unit[0] - 1, unit[1]), (unit[0], unit[1] - 1),
                        (unit[0] - 1, unit[1] - 1), (unit[0] - 1, unit[1] + 1), (unit[0] + 1, unit[1] - 1), (unit[0] + 1, unit[1] + 1)}.intersection(units):
                    ships_dict[3].append(((unit[0], unit[1]), (unit[0], unit[1] + 1), (unit[0], unit[1] + 2)))
                continue

            if not {(unit[0], unit[1] - 1),
                    (unit[0] - 1, unit[1] - 1), (unit[0] - 1, unit[1] + 1), (unit[0] + 1, unit[1] - 1), (unit[0] + 1, unit[1] + 1)}.intersection(units):
                ships_dict[2].append(((unit[0], unit[1]), (unit[0], unit[1] + 1)))
                continue

        if not {(unit[0] - 1, unit[1]), (unit[0], unit[1] - 1), (unit[0] + 1, unit[1]), (unit[0], unit[1] + 1),
                (unit[0] - 1, unit[1] - 1), (unit[0] - 1, unit[1] + 1), (unit[0] + 1, unit[1] - 1), (unit[0] + 1, unit[1] + 1)}.intersection(units):
            ships_dict[1].append((unit[0], unit[1]))
            continue

    if [len(ships_dict[i]) for i in range(1, 5)] == [4, 3, 2, 1]:
        return True
    else:
        return False


battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(validate_battlefield(battleField), True)
