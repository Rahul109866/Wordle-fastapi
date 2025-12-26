from enum import Enum


class Answer(Enum):
    GREY_COMPLETE_MISS = "miss"
    YELLOW_PARTIAL_GUESS = "partial"
    GREEN_CORRECT_GUESS = "success"


def get_word_map(word: str) -> tuple[dict[int, str], dict[int, str]]:

    count_map = {}
    position_map = {}
    # word_map = {index: char for index, char in enumerate(word)}

    for index, char in enumerate(word):
        if char not in count_map.keys():
            count_map[char] = 1
        else:
            count_map[char] += 1
        position_map[index] = char

    return count_map, position_map


def guess_attempt(guess_input: str, answer: str) -> list[str]:
    # ignore the return type. WIP still

    result: list[None] = [None, None, None, None, None]
    guess_count_map, guess_position_map = get_word_map(guess_input.lower())
    answer_count_map, answer_position_map = get_word_map(answer)
    # print(answer_count_map)

    # pass 1: greens check
    for index, char in guess_position_map.items():
        if answer_position_map[index] == char:
            result[index] = Answer.GREEN_CORRECT_GUESS.value
            answer_count_map[char] -= 1


    #pass 2: check for yellows and greys
    for index, char in guess_position_map.items():
        if result[index] is not None:
            continue
        elif answer_count_map.get(char, 0) > 0:
            result[index] = Answer.YELLOW_PARTIAL_GUESS.value
            answer_count_map[char] -= 1
        else:
            result[index] = Answer.GREY_COMPLETE_MISS.value
    return result
    


if __name__ == "__main__":#
    print(guess_attempt("brock", "black"))
