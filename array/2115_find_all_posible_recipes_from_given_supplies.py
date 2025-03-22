from collections import defaultdict, deque 

def findAllReceipes(recipes,ingredients,supplies):
    graph = defaultdict(list) 
    in_degree = defaultdict(int) 

    recipes_to_index = {recipe:i for i, recipe in enumerate(recipes)}

    for i, recipe in enumerate(recipes):
        for ingredient in ingredients[i]:
            graph[ingredient].append(recipe)
            in_degree[recipe] += 1 

    queue = deque(supplies)
    result = [] 

    while queue:
        current = queue.popleft()
        if current in recipes_to_index:
            result.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result


recipes = ["bread", "sandwich"]
ingredients = [["flour", "yeast"], ["bread", "ham"]]
supplies = ["flour", "yeast", "ham"]

print(findAllReceipes(recipes, ingredients, supplies))