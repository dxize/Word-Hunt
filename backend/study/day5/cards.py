def _is_added_word(word: str, added_words: set[str]) -> bool:
    return word.lower() in added_words


def _write_while_correct_data_card(key: str, added_words: set[str] | None = None) -> str:
    while True:
        text: str = input(f"Enter {key}: ").strip()

        if text == "": 
            print(f"{key.capitalize()} cannot be empty")
            continue

        if key == "word" and added_words:
            if _is_added_word(text, added_words):
                print("Card already exists")
                continue

        break

    return text  


def _get_added_words(cards: list[dict[str, str]]) -> set[str]:
    return {card["word"].lower() for card in cards}


def create_data_card(cards: list[dict[str, str]]) -> dict[str, str]:
    dictionary: dict[str, str] = {}
    added_words: set[str] = _get_added_words(cards)

    dictionary["word"] = _write_while_correct_data_card("word", added_words)
    dictionary["translation"] = _write_while_correct_data_card("translation")
    dictionary["example"] = _write_while_correct_data_card("example")
    
    return dictionary


def show_card(card: dict[str, str]) -> None:
    print("----- Word Hunt -----")
    print(f"Word: {card['word']}")
    print(f"Translation: {card['translation']}")
    print(f"Example: {card['example']}")
    print(f"Length word: {len(card['word'])}")
    print("---------------------")


def show_all_cards(cards: list[dict[str, str]]) -> None:
    if not cards:
        print("No cards found")
        return

    for card in cards:
        show_card(card)


def search_card(cards: list[dict[str, str]]) -> None:
    word: str = input("Enter word: ").strip()
    is_found: bool = False

    for card in cards:
        if word.lower() == card["word"].lower():
            show_card(card)
            is_found = True
            break

    if not is_found:
        print("Card not found")


def delete_card(cards: list[dict[str, str]]) -> None:
    text = _write_while_correct_data_card("delete word")

    for i, card in enumerate(cards):
        if card["word"].lower() == text.lower():
            del cards[i]
            print("Card deleted")
            return

    print("Card not found")