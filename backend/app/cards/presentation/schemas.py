from pydantic import BaseModel, Field

class CardCreate(BaseModel):
    word: str = Field(min_length=1, max_length=100)
    translation: str = Field(min_length=1, max_length=200)
    example: str = Field(min_length=1, max_length=500)

class CardResponse(BaseModel):
    id: str
    word: str
    translation: str
    example: str

class CardUpdate(BaseModel):
    word: str | None = Field(default=None, min_length=1, max_length=100)
    translation: str | None = Field(default=None, min_length=1, max_length=200)
    example: str | None = Field(default=None, min_length=1, max_length=500)