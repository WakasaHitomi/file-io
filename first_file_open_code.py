with open('scrabble_list.txt', 'r') as f:
    words = f.read().splitlines()
    
    count = 0
    for w in words:
        count += 1
    print(count)
#84009 words
