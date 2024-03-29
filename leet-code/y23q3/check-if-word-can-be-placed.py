def place(board, word):
    for x in board, zip(*board):
        for row in x:
            for token in ''.join(row).split('#'):
                for letters in word, word[::-1]:
                    if len(token) == len(letters):
                        if all(c in (' ', letter) for c, letter in zip(token, letters)):
                            return True
    return False
