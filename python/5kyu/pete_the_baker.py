# https://www.codewars.com/kata/525c65e51bf619685c000059

def cakes(recipe, available):
    return min(available.get(i, 0) // recipe[i] for i in recipe)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available), 2)
