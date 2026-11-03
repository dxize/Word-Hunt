def show_menu() -> None:
    print("Select command:")
    print("[1] - Create card")
    print("[2] - Show all cards")
    print("[3] - Search card")
    print("[4] - Exit")


def is_correct_selected_command(command: str) -> bool:
    return command in ("1", "2", "3", "4")


def write_while_correct_data_card(input_text: str, empty_data_text: str) -> str:
    while True:
        text: str = input(input_text).strip()

        if text == "": 
            print(empty_data_text)
            continue

        break

    return text  

def set_data_card() -> dict[str, str]:
    dictionary: dict[str, str] = {}

    dictionary["word"] = write_while_correct_data_card("Enter word: ", "Word cannot be empty")
    dictionary["translation"] = write_while_correct_data_card("Enter translation: ", "Translation cannot be empty")
    dictionary["example"] = write_while_correct_data_card("Enter example: ", "Example cannot be empty")
    
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


def run_command(command: str, cards: list[dict[str, str]]) -> bool:
    if command == "1":
        cards.append(set_data_card())
    elif command == "2":
        show_all_cards(cards)
    elif command == "3":
        search_card(cards)
    elif command == "4":
        return False

    return True


cards: list[dict[str, str]] = []
is_processing: bool = True

while is_processing:
    show_menu()
    command: str = input().strip()

    if is_correct_selected_command(command):
        is_processing = run_command(command, cards)
    else:
        print("Invalid command")

print("Program finished.")