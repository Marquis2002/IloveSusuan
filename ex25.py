
def break_words(stuff):
    """This function will break up words for us."""
    print(">>>>stuff = ", stuff)
    words = stuff.split(' ')
    print(">>>>stuff = ", stuff, ">>>>words = ", words)
    return words

def sort_words(words):
    """Sorts the words."""
    print(">>>>words = ", words)
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    print(">>>>words = ", words)
    word = words.pop(0)
    print(word)
    print(">>>>words = ", words, ">>>>word = ", word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    print(">>>>words = ", words)
    word = words.pop(-1)
    print(">>>>words = ", words, ">>>>word = ", word)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    print(">>>>words = ", words)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorted the words and then print the first and the last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
