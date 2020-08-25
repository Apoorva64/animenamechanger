import animeletterchangerthing as yes


def load_words(textfile):
    words = open(textfile).readlines()
    for index, word in enumerate(words):
        words[index] = word.split('\n')[0]
    return words


anime_list = load_words('anime_list.txt')
for word in anime_list:
    yes.main(word)
