# https://www.codewars.com/kata/550f22f4d758534c1100025a

def dirReduc(arr):
    opposites = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST",
    }

    reduced = []
    for d in arr:
        if reduced and reduced[-1] == opposites[d]:
            reduced.pop()
        else:
            reduced.append(d)

    return reduced


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ["WEST"])
