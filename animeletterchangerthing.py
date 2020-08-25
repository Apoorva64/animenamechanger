import string


def load_words():
    with open('words_to_find_in_name.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words


def main(anime_name):
    alphabet = string.ascii_lowercase
    get_anime_name = anime_name.lower()
    name_words = get_anime_name.split(' ')
    english_words = load_words()
    for index, word in enumerate(name_words):
        for n_letter in range(len(word)):
            for _letter in alphabet:
                new_word = list(word)
                new_word[n_letter] = _letter
                word_to_find = ''.join(new_word)
                # print(word_to_find)
                if word_to_find in english_words:
                    new_name = name_words
                    new_name.pop(index)
                    new_name.insert(index, word_to_find)
                    print(' '.join(new_name))
                    # print(word_to_find)
