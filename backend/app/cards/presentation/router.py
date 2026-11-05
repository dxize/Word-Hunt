from fastapi import APIRouter

cards_for_tests: list[dict[str, str]] = [
    {
        "id": "1",
        "word": "apple",
        "translation": "яблоко",
        "example": "I eat an apple"
    },
    {
        "id": "2",
        "word": "book",
        "translation": "книга",
        "example": "I read book"    
    },
    {
        "id": "3",
        "word": "chair",
        "translation": "стул",
        "example": "I sit on chair"
    },
    {
        "id": "4",
        "word": "app",
        "translation": "приложение",
        "example": "I open app"
    }
]


router = APIRouter(
    prefix="/cards",
    tags=["Cards"]
)


@router.get("")
def get_cards(word: str | None = None) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []

    if word:
        for card in cards_for_tests:
            if card["word"].lower().startswith(word.lower()):
                result.append(card)

        return result
    
    return cards_for_tests
