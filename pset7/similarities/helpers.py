from nltk.tokenize import sent_tokenize


# finds common lines in inputs
def lines(a, b):
    """Return lines in both a and b"""

    a_lines = set(a.split("\n"))
    b_lines = set(b.split("\n"))

    return a_lines & b_lines


# finds common sentences in inputs
def sentences(a, b):
    """Return sentences in both a and b"""

    a_sentences = set(sent_tokenize(a))
    b_sentences = set(sent_tokenize(b))

    return a_sentences & b_sentences


# finds common substrings in inputs
def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    a_substrings = set(substring_tokenize(a, n))
    b_substrings = set(substring_tokenize(b, n))

    return a_substrings & b_substrings


# tokenizes substrings
def substring_tokenize(str, n):
    substrings = []

    for i in range(len(str) - n + 1):
        substrings.append(str[i:i + n])

    return substrings