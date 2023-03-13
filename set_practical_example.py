import requests

frankenstein = "https://www.gutenberg.org/cache/epub/84/pg84.txt"
dracula = "https://www.gutenbers.org/cache/epub/345/pg345.txt"


def count_words_in_book(book_url, book_name):
    """
    Save a local copy of the book
    :param book_url:
    :param book_name:
    :return:
    """
    r = requests.get(book_url)
    f = open(book_name, "wb")
    f.write(r.content)
    f.close()

count_words_in_book(frankenstein, "frankenstein.txt")

def count_unique_words(book):
    unique_words = set()
    punctuation = ",.;:'!?_-"
    f = open(book)
    for line in f:
        line = line.lower()
        for p in punctuation:
            line = line.replace(p, "")  # replace any punctuation with nothing
        words = line.split()
        unique_words_in_line = set(words) # this makes a set of all the words - only unique
        unique_words = unique_words.union(unique_words_in_line)
    return len(unique_words)

wordscount = count_unique_words("frankenstein.txt")
print(f"The book has {wordscount} of unique words")



