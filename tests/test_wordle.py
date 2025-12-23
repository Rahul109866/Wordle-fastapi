import pytest
from wordle import guess_attempt

answer = "chalk"


@pytest.mark.parametrize(
    "guess,expected",
    [
        ("batch", {0: "miss", 1: "partial", 2: "miss", 3: "partial", 4: "partial"}),
        ("wench", {0: "miss", 1: "miss", 2: "miss", 3: "partial", 4: "partial"}),
        (
            "chalk",
            {0: "success", 1: "success", 2: "success", 3: "success", 4: "success"},
        ),
    ],
)
def test_guess_attempt(guess: str, expected: str):
    result = guess_attempt(guess, answer)
    assert result == expected


@pytest.mark.parametrize(
    "guess,expected",
    [
        (
            "Chalk",
            {0: "success", 1: "success", 2: "success", 3: "success", 4: "success"},
        ),
        (
            "CHaLk",
            {0: "success", 1: "success", 2: "success", 3: "success", 4: "success"},
        ),
    ],
)
def test_guess_attempt_with_case(guess: str, expected: str):
    result = guess_attempt(guess, answer)
    assert result == expected


@pytest.mark.parametrize(
    "guess,answer,expected",
    [
        (
            "click",
            "black",
            {0: "miss", 1: "success", 2: "miss", 3: "success", 4: "success"},
        ),
        ("catch", "black", {0: "miss", 1: "partial", 2: "miss", 3: "success", 4: "miss"}),
        (
            "black",
            "catch",
            {0: "miss", 1: "miss", 2: "partial", 3: "success", 4: "miss"},
        ),
        (
            "cocky",
            "black",
            {0: "partial", 1: "miss", 2: "miss", 3: "partial", 4: "miss"},
        ),
    ],
)
def test_duplicate_attempt(guess: str, answer: str, expected: dict[int:str]):

    result = guess_attempt(guess, answer)
    assert result == expected
