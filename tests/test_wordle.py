import pytest
from wordle import guess_attempt

answer = "chalk"

@pytest.mark.parametrize("guess,expected", [
    ("batch", {0: 'miss', 1: 'partial', 2: 'miss', 3: 'partial', 4: 'partial'}),
    ("wench", {0: 'miss', 1: 'miss', 2: 'miss', 3: 'partial', 4: 'partial'}),
    ("chalk", {0: 'success', 1: 'success', 2: 'success', 3: 'success', 4: 'success'}),
    ("Chalk", {0: 'success', 1: 'success', 2: 'success', 3: 'success', 4: 'success'})
])
def test_guess_attempt(guess: str, expected: str):
    result = guess_attempt(guess, answer)
    assert result == expected