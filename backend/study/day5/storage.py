import json

def save_cards(cards: list[dict[str, str]]) -> None:
    with open("cards_day4.json", "w", encoding="utf-8") as file:
        json.dump(cards, file, ensure_ascii=False, indent=4)


def load_cards() -> list[dict[str, str]]:
    try:
        with open("cards_day4.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []