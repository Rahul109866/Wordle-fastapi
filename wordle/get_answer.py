from random import randint

answer = []
with open(r"resources\answer_list.txt", "r") as f:
    for line in f:
        for word in line.split():
            answer.append(word.strip())


def get_answer() -> str:
    return answer[randint(0, len(answer) - 1)]
