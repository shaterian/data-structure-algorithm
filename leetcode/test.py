guess_rep = {}

for index, char in enumerate(guess_rep):
            if char not in guess_rep:
                guess_rep[char] = []
            guess_rep[char].append(index)