import json
from logic.search import boolean_search

def load_recipes(path="data/resep.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    print("ResepCepat – Cari Resep Berdasarkan Bahan")
    user_input = input("Masukkan bahan yang kamu punya (pisahkan dengan koma):\n> ")
    user_ingredients = [b.strip() for b in user_input.split(",")]

    mode = input("Gunakan mode pencarian (AND/OR)? [default: OR]: ").strip().upper()
    if mode not in ["AND", "OR"]:
        mode = "OR"

    recipes = load_recipes()
    results = boolean_search(recipes, user_ingredients, mode=mode)

    if not results:
        print("\n❌ Tidak ditemukan resep yang cocok.")
    else:
        print(f"\n✅ Ditemukan {len(results)} resep:")
        for i, recipe in enumerate(results, 1):
            print(f"\n{i}. {recipe['title']}")
            print(f"   Bahan  : {', '.join(recipe['ingredients'])}")

if __name__ == "__main__":
    main()
