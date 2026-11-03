import json
from cards import *
from storage import *

def _show_menu() -> None:
    print("Select command:")
    print("[1] - Create card")
    print("[2] - Show all cards")
    print("[3] - Search card")
    print("[4] - Delete card")
    print("[5] - Exit")


def _run_command(command: str, cards: list[dict[str, str]]) -> bool:
    if command == "1":
        new_card: dict[str, str] = create_data_card(cards)
        cards.append(new_card)
        save_cards(cards)
    elif command == "2":
        show_all_cards(cards)
    elif command == "3":
        search_card(cards)
    elif command == "4":
        delete_card(cards)
        save_cards(cards)
    elif command == "5":
        return False

    return True


def _is_correct_selected_command(command: str) -> bool:
    return command in ("1", "2", "3", "4", "5")


def _main() -> None:
    try:
        cards: list[dict[str, str]] = load_cards()
    except json.JSONDecodeError:
        print("Invalid file")
        return

    is_processing: bool = True

    while is_processing:
        _show_menu()
        command: str = input().strip()

        if _is_correct_selected_command(command):
            is_processing = _run_command(command, cards)
        else:
            print("Invalid command")

    print("Program finished.")


if __name__ == "__main__":
    _main()