from typing import Union, Any

from fastapi import FastAPI
from wordle import guess_attempt
from random import randint
from pydantic import BaseModel


app = FastAPI()


class GuessResponse(BaseModel):
    message: str
    result: list[str]


with open("resources/answer_list.txt", "r") as f:
    answer_list: list[str] = [w.strip() for w in f if w.strip()]

answer = answer_list[randint(0, len(answer_list) - 1)]

print(answer)
@app.get("/")
def main():
    return {"message": "Welcome to Wordle API! Guess using /guess/<your guess word>"}


@app.get("/guess/{guess_word}", response_model=GuessResponse)
def user_guess(guess_word: str):
    guess_word = guess_word.strip().lower()

    if len(guess_word) != 5:
        message = "Please enter a valid 5 letter world"
        result = [""] * 5

    else:
        result = guess_attempt(guess_input=guess_word, answer=answer)
        result_state = result.count("success")
        if result_state == 5:
            message = "Congrats. You have solved the wordle puzzle"

        elif result_state in (3, 4):
            message = "oof. Close. You're almost there"

        elif result_state in (1, 2):
            message = "Come on dawg. Lock in!"

        else:
            message = "Yea pack it up lil bro!"

    return {"message": message, "result": result}
