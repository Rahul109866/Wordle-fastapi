from typing import Union

from fastapi import FastAPI
from wordle import guess_attempt
from random import randint


app = FastAPI()


with open("resources/answer_list.txt", "r") as f:
    answer_list: list[str] = [w.strip() for w in f if w.strip()]

answer = answer_list[randint(0, len(answer_list) - 1)]

@app.get("/")
def main():
    return {"message": "Welcome to Wordle API! Guess using /guess/<your guess word>"}

@app.get("/guess/{guess_word}")
def user_guess(guess_word: str) -> list[str]:
    if len(guess_word) != 5:
        return {"message": "Please enter a valid 5 letter world"}
    result = guess_attempt(guess_input=guess_word, answer=answer)
    return result