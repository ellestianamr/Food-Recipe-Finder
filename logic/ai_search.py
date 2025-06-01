from sentence_transformers import SentenceTransformer, util

# Load model NLP (sekali)
model = SentenceTransformer('all-MiniLM-L6-v2')

def ai_search(recipes, user_ingredients, threshold=0.5):
    user_query = ", ".join(user_ingredients)
    user_embedding = model.encode(user_query, convert_to_tensor=True)

    results = []

    for recipe in recipes:
        recipe_text = ", ".join(recipe["ingredients"])
        recipe_embedding = model.encode(recipe_text, convert_to_tensor=True)

        similarity = util.cos_sim(user_embedding, recipe_embedding)[0][0].item()
        results.append((recipe, similarity))

    # Urutkan berdasarkan skor kemiripan (descending)
    results.sort(key=lambda x: x[1], reverse=True)

    # Filter berdasarkan threshold minimum similarity
    filtered_results = [(r[0], r[1]) for r in results if r[1] >= threshold]

    return filtered_results
