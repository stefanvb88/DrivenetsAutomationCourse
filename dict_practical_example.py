# find the 10 most used words in Dracula!
import requests

def word_frequency(book):
    """
    Construct a dictionary with all the word frequencies in the book
    :param book: the local filename
    :return: a dict where the key is the unique word, value is the number the word shows up in the book
    """

    f = open(book)
    punctuation = ".,;'?!_-:\"<>="
    freq = {}
    for line in f:
        line = line.lower()
        for p in punctuation:
            line = line.replace(p, " ")
        words = line.split()
        for word in words:
            if word in freq:
                freq[word] = freq[word] + 1
            else:
                freq[word] = 1
            #freq[word] = freq[word] + 1
            #freq.setdefault(word, 0) + 1
            #freq[word] = freq.setdefault(word, 0) + 1
        #print(freq)
    return freq

#word_frequency("frankenstein.txt")


def get_max(freq: dict, top: int=10):
    result_list = []
    top_freq = list(freq.values())
    top_freq.sort(reverse=True)
    top_freq = top_freq[:top]
    print(top_freq)

    for f in top_freq:
        for k, v in freq.items():
            if v == top_freq:
                result_list.append((k, v))# add the word / freq tuple in the result list
                del freq[k]
                break

freq = word_frequency("frankenstein.txt")
print(get_max(freq))