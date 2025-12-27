import pytest
from wordle.engine import guess_attempt

answer = "chalk"


@pytest.mark.parametrize(
    "guess,expected",
    [
        ("batch", ["miss", "partial", "miss", "partial", "partial"]),
        ("wench", ["miss", "miss", "miss", "partial", "partial"]),
        (
            "chalk",
            ["success", "success", "success", "success", "success"],
        ),
    ],
)
def test_guess_attempt(guess: str, expected: list[str]):
    result = guess_attempt(guess, answer)
    assert result == expected


@pytest.mark.parametrize(
    "guess,expected",
    [
        (
            "Chalk",
            ["success", "success", "success", "success", "success"],
        ),
        (
            "CHaLk",
            ["success", "success", "success", "success", "success"],
        ),
    ],
)
def test_guess_attempt_with_case(guess: str, expected: list[str]):
    result = guess_attempt(guess, answer)
    assert result == expected


@pytest.mark.parametrize(
    "guess,answer,expected",
    [
        (
            "click",
            "black",
            ["miss", "success", "miss", "success", "success"],
        ),
        ("catch", "black", ["miss", "partial", "miss", "success", "miss"]),
        (
            "black",
            "catch",
            ["miss", "miss", "partial", "success", "miss"],
        ),
        (
            "cocky",
            "black",
            ["partial", "miss", "miss", "partial", "miss"],
        ),
    ],
)
def test_duplicate_attempt(guess: str, answer: str, expected: list[str]):

    result = guess_attempt(guess, answer)
    assert result == expected
