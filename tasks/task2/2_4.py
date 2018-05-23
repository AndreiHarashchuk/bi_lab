"""
You are given a text, which contains different english letters
and punctuation symbols.
You should find the most frequent letter in the text.
The letter returned must be in lower case.
While checking for the most wanted letter,
casing does not matter, so for the purpose of your
search, "A" == "a". Make sure you do not count punctuation symbols,
digits and whitespaces, only letters.
"""


def checkio(text):
    text = text.lower()

    table = {}

    for caracter in text:

        if 'a' <= caracter <= 'z':
            table[caracter] = table.get(caracter, 0) + 1

    max_freq = max(table.values())

    for caracter in sorted(table.keys()):

        if table[caracter] == max_freq:
            return caracter


# These "asserts" using only for self-checking
#  and not necessary for auto-testing

if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"

    assert checkio("How do you do?") == "o", "O is most wanted"

    assert checkio("One") == "e", "All letter only once."
