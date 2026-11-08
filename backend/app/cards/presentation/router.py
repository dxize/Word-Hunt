from fastapi import APIRouter, HTTPException
from app.cards.presentation.schemas import CardCreate, CardResponse, CardUpdate

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


def _find_cards(word: str | None) -> list[dict[str, str]]:
    if not word:
        return cards_for_tests

    result: list[dict[str, str]] = []

    for card in cards_for_tests:
        if card["word"].lower().startswith(word.lower()):
            result.append(card)

    return result

@router.get("")
def get_cards(word: str | None = None) -> list[dict[str, str]]:
    return _find_cards(word)




def _validate_card_is_unique(new_card: CardCreate) -> None:
    for card in cards_for_tests:
        if card["word"].lower() == new_card.word.lower():
            raise HTTPException(
                status_code=409,
                detail="Card already exists"
            )


def _create_card(new_card: CardCreate) -> CardResponse:
    result_card = CardResponse(
        id=str(len(cards_for_tests) + 1),
        word=new_card.word,
        translation=new_card.translation,
        example=new_card.example
    )

    cards_for_tests.append(result_card.model_dump())

    return result_card


@router.post("", response_model=CardResponse, status_code=201)
def create_card(new_card: CardCreate) -> CardResponse:
    _validate_card_is_unique(new_card)

    return _create_card(new_card)




def _validate_update_data(update_data: dict[str, str | None]) -> None:
    if not update_data:
        raise HTTPException(
            status_code=422,
            detail="Empty request body"
        )
    
    if any(value is None for value in update_data.values()):
        raise HTTPException(
            status_code=422,
            detail="Fields cannot be null"
        )


def _find_card_with_id(id: str) -> dict[str, str]:
    for card in cards_for_tests:
        if card["id"] == id:
            return card

    raise HTTPException(
        status_code=404,
        detail="Card not found"
    )

def _check_card_already_exists_during_update(update_data: dict[str, str], id: str) -> None:
    if "word" in update_data:
        for card in cards_for_tests:
            if card["id"] != id and card["word"].lower() == update_data["word"].lower():
                raise HTTPException(
                    status_code=409,
                    detail="Card already exists"
                )

    
@router.patch("/{id}", response_model=CardResponse)
def update_card(id: str, updated_card: CardUpdate) -> dict[str, str]:
    update_data = updated_card.model_dump(exclude_unset=True)

    _validate_update_data(update_data)

    target_card: dict[str, str] = _find_card_with_id(id)

    _check_card_already_exists_during_update(update_data, id)

    target_card.update(update_data)

    return target_card


@router.delete("/{id}", status_code=204)
def delete_card(id: str) -> None:
    target_card: dict[str, str] = _find_card_with_id(id)
    cards_for_tests.remove(target_card)    