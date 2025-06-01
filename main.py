import json
from logic.search import boolean_search
from logic.ai_search import ai_search

def load_recipes(path="data/resep.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    print("ResepCepat – Temukan Resep Berdasarkan Bahan")
    
    user_input = input("Masukkan bahan yang kamu punya (pisahkan dengan koma):\n> ").strip()
    if not user_input:
        print("Input tidak boleh kosong.")
        return

    user_ingredients = [b.strip().lower() for b in user_input.split(",") if b.strip()]
    if not user_ingredients:
        print("Tidak ada bahan yang valid.")
        return

    print("\nPilih mode pencarian:")
    print("1. Boolean (cocok sebagian atau semua bahan)")
    print("2. AI (berbasis kemiripan konten)")

    mode_input = input("Masukkan pilihan (1/2) [default: 1]: ").strip()
    mode = "A" if mode_input == "2" else "B"

    recipes = load_recipes()

    if mode == "A":
        print("\n🔍 Menggunakan pencarian berbasis AI...")
        threshold_input = input("Masukkan threshold minimal kemiripan (0.0 - 1.0) [default: 0.5]: ").strip()
        try:
            threshold = float(threshold_input) if threshold_input else 0.5
            if not (0 <= threshold <= 1):
                raise ValueError()
        except ValueError:
            print("Threshold tidak valid. Menggunakan nilai default 0.5.")
            threshold = 0.5

        results = ai_search(recipes, user_ingredients, threshold=threshold)
    else:
        and_or = input("Gunakan mode Boolean (AND/OR)? [default: OR]: ").strip().upper()
        if and_or not in ["AND", "OR"]:
            and_or = "OR"
        results = boolean_search(recipes, user_ingredients, mode=and_or)

    if not results:
        print("\n❌ Tidak ditemukan resep yang cocok.")
    else:
        print(f"\n✅ Ditemukan {len(results)} resep yang cocok:\n")
        for i, result in enumerate(results, 1):
            if isinstance(result, tuple):
                recipe, score = result
                print(f"{i}. {recipe['title']} (skor: {score:.3f})")
            else:
                recipe = result
                print(f"{i}. {recipe['title']}")
            print(f"   Bahan  : {', '.join(recipe['ingredients'])}")

if __name__ == "__main__":
    main()
