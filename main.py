from fastapi import FastAPI
from wordle.engine import guess_attempt
from pydantic import BaseModel
from wordle.get_answer import get_answer
from wordle.rules import response_builder, validate_guess


app = FastAPI()


class GuessResponse(BaseModel):
    message: str
    result: list[str]


answer = get_answer()

print(answer)


@app.get("/")
def main():
    return {"message": "Welcome to Wordle API! Guess using /guess/<your guess word>"}


@app.get("/guess/{guess_word}", response_model=GuessResponse)
def user_guess(guess_word: str):
    guess_word = guess_word.strip().lower()

    if not validate_guess(guess_word):
        message = "Please enter a valid 5 letter word"
        result = [""] * 5

    else:
        result = guess_attempt(guess_input=guess_word, answer=answer)
        message = response_builder(result)

    return {"message": message, "result": result}
