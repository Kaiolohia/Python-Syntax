def print_upper_words(words, letters = ""):
    valid_words = []
    for x in range(len(words)):
        for letter in letters:
            if words[x][0].upper() == letter.upper():
                valid_words.append(words[x])

    for x in range(len(valid_words)):
        print(valid_words[x].upper())

print_upper_words(["Over there", 'That', 'This'], {'t'})