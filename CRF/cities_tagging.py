import Vocabulary
import sys


def is_city(word):
    for c in Vocabulary.cities:
        if c.lower() == word.lower():
            return True
    return False

def is_airport(word):
    for c in Vocabulary.airports:
        if c.lower() == word.lower():
            return True
    return False

def is_airline(word):
    for c in Vocabulary.airlines:
        if c.lower() == word.lower():
            return True
    return False

if __name__ == '__main__':
    """print('sys.argv: '), sys.argv
    if len(sys.argv) != 1:
        print('trop d\'arguments !')
    else:"""
    with open("atis.train", "r+") as f:   #sys.argv[0]
        tab = []
        for lign in f.readlines():
            words = lign.split("\t")
            if is_city(words[0]):
                words.append(words[1])
                words[1] = "CITY"
                lign = words[0] + "\t" + words[1] + "\t" + words[2] + "\n"
                tab.append(lign)
            elif is_airport(words[0]):
                words.append(words[1])
                words[1] = "AIRPORT"
                lign = words[0] + "\t" + words[1] + "\t" + words[2] + "\n"
                tab.append(lign)
            elif is_airline(words[0]):
                words.append(words[1])
                words[1] = "AIRLINE"
                lign = words[0] + "\t" + words[1] + "\t" + words[2] + "\n"
                tab.append(lign)
            elif lign != "\t\n":
                    words.append(words[1])
                    words[1] = "trash"
                    lign = words[0] + "\t" + words[1] + "\t" + words[2] + "\n"
                    tab.append(lign)

    with open("new_atis.train", "w") as f:
        for l in tab:
            f.write(l)


