def validate_guess(input: str) -> bool:
    return len(input) == 5 and input.isalpha()


def response_builder(result: list[str]) -> str:

    success_count = result.count("success")
    if success_count == 5:
        message = "Congrats. You have solved the wordle puzzle"

    elif success_count in (3, 4):
        message = "oof. Close. You're almost there"

    elif success_count in (1, 2):
        message = "Come on dawg. Lock in!"

    else:
        message = "Yea pack it up lil bro!"

    return message
