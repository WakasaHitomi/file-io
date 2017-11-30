with open('scrabble_list.txt', 'r') as f:
    words = f.read().splitlines()
    
    word_count = 0
    for w in words:
        word_count += 1
    print(word_count)
    print("this is the number of words")
#84009 words

    five_letters = 0
    for w in words:
        if len(w) == 5:
            five_letters += 1
    print(five_letters)
    print("Words with only 5 letters")
#8939
