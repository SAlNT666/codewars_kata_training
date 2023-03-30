# https://www.codewars.com/kata/550f22f4d758534c1100025a

def dirReduc(arr):
    dir1 = ' '.join(arr)
    dir2 = dir1.replace('NORTH SOUTH', '').replace('SOUTH NORTH', '').replace('EAST WEST', '').replace('WEST EAST', '')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ["WEST"])
