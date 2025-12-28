from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from wordle.engine import guess_attempt
from pydantic import BaseModel
from wordle.get_answer import get_answer
from wordle.rules import response_builder, validate_guess

templates = Jinja2Templates("templates")
app = FastAPI()


class GuessResponse(BaseModel):
    message: str
    result: list[str]


answer = get_answer()


@app.get("/")
def main(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request
        }

    )


@app.get("/guess", response_class=HTMLResponse)
def guess_page(request: Request):
    return templates.TemplateResponse(name="guess.html", context={"request": request})


@app.post("/guess", response_class=HTMLResponse)
def guess_word_attempt(request: Request, guess_word: str = Form(alias="guess")):
    guess_word = guess_word.strip().lower()

    if not validate_guess(guess_word):
        return templates.TemplateResponse(
            name="guess.html",
            context={
                "request": request,
                "message": "Invalid Guess. Please enter a valid 5 letter word",
                "guess": guess_word,
            },
        )

    result = guess_attempt(guess_word, answer)
    message = response_builder(result)

    return templates.TemplateResponse(
        name="guess.html",
        context={
            "request": request,
            "message": message,
            "result": result,
            "guess": guess_word,
        },
    )
