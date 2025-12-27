with open(r"resources\source.txt", 'r') as f, open(r"resources\answer_list.txt", 'w') as out:
    
    while line := f.readline():
        for word in line.split():
            if len(word) == 5:
                print(word)
                out.write(word + '\n')
            else:
                print(f"'{word}' is not 5 letters long")


def foo():
    pass