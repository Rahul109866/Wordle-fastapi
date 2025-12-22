from enum import Enum


class Answer(Enum):
    GREY_COMPLETE_MISS = "miss"
    YELLOW_PARTIAL_GUESS = "partial"
    GREEN_CORRECT_GUESS = "success"


def get_word_map(word: str) -> dict[int, str]:
    # assuming we are not doing repetition for now
    word_map = {index: char for index, char in enumerate(word)}

    return word_map


def guess_attempt(guess_word: str, answer: str) -> dict[int, str]:
    # ignore the return type. WIP still
    guess_map = get_word_map(guess_word.lower())
    answer_map = get_word_map(answer)
    guess_result: dict[int, str] = {}
    for guess_position, guess_letter in guess_map.items():
        if guess_letter not in answer_map.values():
            guess_result[guess_position] = Answer.GREY_COMPLETE_MISS.value
        elif guess_map[guess_position] != answer_map[guess_position]:
            guess_result[guess_position] = Answer.YELLOW_PARTIAL_GUESS.value
        else:
            guess_result[guess_position] = Answer.GREEN_CORRECT_GUESS.value
    return guess_result

    # return guess_map, answer_map


if __name__ == "__main__":
    print(guess_attempt("click", "brick"))
