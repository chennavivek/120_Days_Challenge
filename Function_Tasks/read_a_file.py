def count_word_frequency(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip("',.!?:;\\")
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

filepath = '/Users/vivekchenna/Library/Mobile Documents/com~apple~CloudDocs/DataAnalyst/120_Days_challenge/Functions/Function_Tasks/sample.txt'
word_frequency = count_word_frequency(filepath)
print(word_frequency)