def boolean_search(recipes, user_ingredients, mode="OR"):
    results = []

    for recipe in recipes:
        recipe_ingredients = set(map(str.lower, recipe["ingredients"]))
        user_ingredients_set = set(map(str.lower, user_ingredients))

        match_count = len(recipe_ingredients.intersection(user_ingredients_set))

        if mode == "OR" and match_count > 0:
            results.append((recipe, match_count))
        elif mode == "AND" and user_ingredients_set.issubset(recipe_ingredients):
            results.append((recipe, match_count))

    # Optional: sort by match count (skoring)
    results.sort(key=lambda x: x[1], reverse=True)

    return [r[0] for r in results]
