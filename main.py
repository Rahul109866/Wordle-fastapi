from typing import Union

from fastapi import FastAPI
from wordle import guess_attempt

app = FastAPI()


@app.get("/{guess}")
def guess(guess: str):
    answer = "chalk"
    return guess_attempt(guess.lower(), answer)
