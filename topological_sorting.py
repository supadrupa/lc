# Topological sorting - Kahn's algorithm
# Input: recipes = ["bread","sandwich","burger"], 
#   ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], 
#   supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich","burger"]


from collections import defaultdict, deque


def find_all_recipes(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
    in_degree = {}  # "bread" : 2 (yeast, flour)
    g = defaultdict(list) # "meat": ["sandwich", "burger"]

    for recipe, components in zip(recipes, ingredients):
        in_degree[recipe] = len(components)

        for component in components:
            g[component].append(recipe)

    
    q = deque(supplies)
    res = []

    while q:
        supplie = q.popleft()
        for recipe in g[supplie]:
            in_degree[recipe] -= 1
            if in_degree[recipe] == 0:
                q.append(recipe)
                res.append(recipe)

    return res
