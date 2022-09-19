stuff = input('> ')

dict = {
    'north':'direction',
    'south':'direction',
    'east':'direction',
    'go':'verb',
    'kill':'verb',
    'eat':'verb',
    'in':'stop',
    'the':'stop',
    'of':'stop',
    'bear':'noun',
    'princess':'noun',
}

def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(stuff):
    words = stuff.split()
    scanned_words = []
    for word in words:
        num = convert_numbers(word)

        if num:
            scanned_words.append(('number', num))
        else:
            if word in dict:
                scanned_words.append((dict.get(word), word))
            else:
                scanned_words.append(('error', word))

    return scanned_words


# def scan(words):
#     scanned_words = []
#     for word in words:
#         num = convert_numbers(word)
        
#         if num:
#             scanned_words.append(('number',num))
#         elif word == 'north':
#             scanned_words.append(('direction', 'north'))
#         elif word == 'south':
#             scanned_words.append(('direction', 'south'))
#         elif word == 'east':
#             scanned_words.append(('direction', 'east'))
#         elif word == 'go':
#             scanned_words.append(('verb', 'go'))
#         elif word == 'kill':
#             scanned_words.append(('verb', 'kill'))
#         elif word == 'eat':
#             scanned_words.append(('verb', 'eat'))
#         elif word == 'the':
#             scanned_words.append(('stop', 'the'))
#         elif word == 'in':
#             scanned_words.append(('stop', 'in'))
#         elif word == 'of':
#             scanned_words.append(('stop', 'of'))
#         elif word == 'bear':
#             scanned_words.append(('noun', 'bear'))
#         elif word == 'princess':
#             scanned_words.append(('noun', 'princess'))
#         else:
#             scanned_words.append(('error', word))

#         return scanned_words
        



