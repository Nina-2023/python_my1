string = input('Введите строку из нескольких слов, разделенных пробелами: ')
words = string.split(' ')

for i, word in enumerate(words):
    if len(word) > 10:
        print(f'{i+1}. {word[:10]}')
    else:
        print(f'{i+1}. {word}')