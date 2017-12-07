words_number = 0

with open('referat.txt', 'r', encoding='utf-8') as myfile:
    for line in myfile:
        words = line.split()
        words_number = words_number + len(words)
        
print(words_number)