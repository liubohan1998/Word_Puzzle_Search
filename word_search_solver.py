
def str_word(word):
    word = list(word)
    return (word)

def row_left_right(row_num, col_num, word, wordsearch):
    for x_a in range(row_num):
        for y_a in range(col_num - len(word) + 1):
            if wordsearch[x_a][y_a] == word[0]:
                sum = 0
                for i in range(len(word)):
                    if wordsearch[x_a][y_a + i] == word[i]:
                        sum += 1
                if sum == len(word):
                    print("%s starts at (%d, %d) and ends at (%d, %d)" % (word, x_a, y_a, x_a, y_a + len(word) - 1))

def row_right_left(row_num, col_num, word, wordsearch):
    for x_a in range(row_num):
        for y_a in range(col_num - len(word) + 1):
            if wordsearch[x_a][y_a] == word[0]:
                sum = 0
                for i in range(len(word)):
                    if wordsearch[x_a][y_a - i] == word[i]:
                        sum += 1
                if sum == len(word):
                    print("%s starts at (%d, %d) and ends at (%d, %d)" % (word, x_a, y_a, x_a, y_a - len(word) + 1))

def col_up_bot(row_num, col_num, word, wordsearch):
    for x_a in range(row_num - len(word) + 1):
        for y_a in range(col_num):
            if wordsearch[x_a][y_a] == word[0]:
                sum = 0
                for i in range(len(word)):
                    if wordsearch[x_a + i][y_a] == word[i]:
                        sum += 1
                if sum == len(word):
                    print("%s starts at (%d, %d) and ends at (%d, %d)" % (word, x_a, y_a, x_a + len(word) - 1, y_a))

def col_bot_up(row_num, col_num, word, wordsearch):
    for x_a in range(row_num):
        for y_a in range(col_num):
            if wordsearch[x_a][y_a] == word[0]:
                sum = 0
                for i in range(len(word)):
                    if wordsearch[x_a - i][y_a] == word[i]:
                        sum += 1
                if sum == len(word):
                    print("%s starts at (%d, %d) and ends at (%d, %d)" % (word, x_a, y_a, x_a - len(word) + 1, y_a))

def left_up__right_bot(row_num, col_num, word, wordsearch):
    for x_a in range(row_num - len(word) + 1):
        for y_a in range(col_num - len(word) + 1):
            if wordsearch[x_a][y_a] == word[0]:
                sum = 0
                for i in range(len(word)):
                    if wordsearch[x_a + i][y_a + i] == word[i]:
                        sum += 1
                if sum == len(word):
                    print("%s starts at (%d, %d) and ends at (%d, %d)" % (word, x_a, y_a, x_a + len(word) - 1, y_a + len(word) - 1))

def right_bot__left_up(row_num, col_num, word, wordsearch):
    for x_a in range(row_num):
        for y_a in range(col_num):
            if wordsearch[x_a][y_a] == word[0]:
                sum = 0
                for i in range(len(word)):
                    if wordsearch[x_a - i][y_a - i] == word[i]:
                        sum += 1
                if sum == len(word):
                    print("%s starts at (%d, %d) and ends at (%d, %d)" % (word, x_a, y_a, x_a - len(word) + 1, y_a - len(word) + 1))

def right_up__left_bot(row_num, col_num, word, wordsearch):
    for x_a in range(row_num - len(word) + 1):
        for y_a in range(col_num):
            if wordsearch[x_a][y_a] == word[0]:
                sum = 0
                for i in range(len(word)):
                    if wordsearch[x_a + i][y_a - i] == word[i]:
                        sum += 1
                if sum == len(word):
                    print("%s starts at (%d, %d) and ends at (%d, %d)" % (word, x_a, y_a, x_a + len(word) - 1, y_a - len(word) + 1))

def left_bot__right_up(row_num, col_num, word, wordsearch):
    for x_a in range(row_num):
        for y_a in range(col_num - len(word) + 1):
            if wordsearch[x_a][y_a] == word[0]:
                sum = 0
                for i in range(len(word)):
                    if wordsearch[x_a - i][y_a + i] == word[i]:
                        sum += 1
                if sum == len(word):
                    print("%s starts at (%d, %d) and ends at (%d, %d)" % (word, x_a, y_a, x_a - len(word) + 1, y_a + len(word) - 1))

def main():
    user_input = input('Enter the name of the file that contains the word search: ')

    with open(user_input) as file:
        content = file.readlines()  # content->List

    for num in range(len(content)):
        content[num] = content[num].replace('\n', '')

    row_col_num = content[0].split()
    row_num = int(row_col_num[0])
    col_num = int(row_col_num[1])

    wordsearch = []
    for lines in range(1, row_num + 1):
        wordsearch.append(content[lines].upper().split())

    worduse = []
    for lines in range(row_num + 2, len(content)):
        worduse.append(content[lines].upper())
    worduse.sort()

    for word in worduse:
        str_word(word)
        row_left_right(row_num, col_num, word, wordsearch)
        row_right_left(row_num, col_num, word, wordsearch)
        col_up_bot(row_num, col_num, word, wordsearch)
        col_bot_up(row_num, col_num, word, wordsearch)
        left_up__right_bot(row_num, col_num, word, wordsearch)
        right_bot__left_up(row_num, col_num, word, wordsearch)
        right_up__left_bot(row_num, col_num, word, wordsearch)
        left_bot__right_up(row_num, col_num, word, wordsearch)
main()
