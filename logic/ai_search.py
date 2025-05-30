from sentence_transformers import SentenceTransformer, util

# Load model NLP (sekali)
model = SentenceTransformer('all-MiniLM-L6-v2')

def ai_search(recipes, user_ingredients):
    user_query = ", ".join(user_ingredients)
    user_embedding = model.encode(user_query, convert_to_tensor=True)

    results = []

    for recipe in recipes:
        recipe_ingredients_text = ", ".join(recipe["ingredients"])
        recipe_embedding = model.encode(recipe_ingredients_text, convert_to_tensor=True)

        similarity = util.cos_sim(user_embedding, recipe_embedding)[0][0].item()
        results.append((recipe, similarity))

    # Urutkan berdasarkan skor kemiripan
    results.sort(key=lambda x: x[1], reverse=True)

    # Threshold opsional (0.5 bisa disesuaikan)
    return [r[0] for r in results if r[1] > 0.5]
