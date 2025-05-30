import json
from logic.search import boolean_search
from logic.ai_search import ai_search 

def load_recipes(path="data/resep.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    print("ResepCepat – Cari Resep Berdasarkan Bahan")
    user_input = input("Masukkan bahan yang kamu punya (pisahkan dengan koma):\n> ")
    user_ingredients = [b.strip() for b in user_input.split(",")]

    mode = input("Pilih mode pencarian - Boolean (B) atau AI (A)? [default: B]: ").strip().upper()
    if mode == "A":
        print("\n🔍 Menggunakan pencarian berbasis AI...")
        recipes = load_recipes()
        results = ai_search(recipes, user_ingredients)
    else:
        and_or = input("Gunakan mode Boolean (AND/OR)? [default: OR]: ").strip().upper()
        if and_or not in ["AND", "OR"]:
            and_or = "OR"
        recipes = load_recipes()
        results = boolean_search(recipes, user_ingredients, mode=and_or)

    if not results:
        print("\n❌ Tidak ditemukan resep yang cocok.")
    else:
        print(f"\n✅ Ditemukan {len(results)} resep:")
        for i, recipe in enumerate(results, 1):
            print(f"\n{i}. {recipe['title']}")
            print(f"   Bahan  : {', '.join(recipe['ingredients'])}")

if __name__ == "__main__":
    main()
