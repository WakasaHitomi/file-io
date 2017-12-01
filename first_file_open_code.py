with open('words_alpha.txt', 'r') as f:
    words = f.read().splitlines()
    
    word_count = 0
    for w in words:
        word_count += 1
    print(word_count)
    print("this is the number of words")
    print()
# 370099 words

    five_letters = 0
    for w in words:
        if len(w) == 5:
            five_letters += 1
    print(five_letters)
    print("Words with only 5 letters")
    print()
# 15918 five letter words

    over_seven_letters = 0
    for w in words:
        if len(w) > 7:
            over_seven_letters += 1
    print(over_seven_letters)
    print(" words that have more 7 letters")
    print()
# 272543 more than 7 letters

    total_letters = 0
    for w in words:
        for letter in w:
            total_letters += 1
    print(total_letters)
    print("Number of characters.")
    print()
# 3494678 total characters

    words_without_e = 0
    for letters in words:
        if letter != "e":
            words_without_e += 1
    print(words_without_e)
    print("words witout the letter e")
    print()
# 

