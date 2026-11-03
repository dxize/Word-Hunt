def show_menu() -> None:
    print("Select command:")
    print("[1] - create card")
    print("[2] - exit")


def get_selected_command() -> str:
    command: str = input().strip()

    if command == '1':
        return "start"
    elif command == '2':
        return "exit"
    else:
        return "Invalid command"


def set_data_card() -> list[str]:
    is_finished = False

    while not is_finished:
        word: str = input("Enter word: ").strip()
        if word == "": 
            print("Word cannot be empty")
            continue

        translation: str = input("Enter translation: ").strip()
        if translation == "":
            print("translation cannot be empty") 
            continue

        example: str = input("Enter example: ").strip()
        if example == "": 
            print("Example cannot be empty")
            continue

        is_finished  = True
        
    return [word, translation, example]


def show_card(word: str, translation: str, example: str) -> None:
    print("----- Word Hunt -----")
    print(f"Word: {word}")
    print(f"Translation: {translation}")
    print(f"Example: {example}")
    print(f"Length word: {len(word)}")
    print("---------------------")



is_processing: bool = True

while is_processing:

    show_menu()
    result = get_selected_command()

    if result == "exit":
        is_processing = False
    elif result == "start":
        card_info: list[str] = set_data_card()
        show_card(card_info[0], card_info[1], card_info[2])
    else:
        print(result, '\n')

print("Program finished.")