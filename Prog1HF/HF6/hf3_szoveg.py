"""
Implementáld az alábbi függvényeket, és lásd el őket típusinformációkkal.
Ellenőrzéshez: python -m mypy --strict hf3_szoveg.py
Készíthetsz további segédfüggvényeket is.
"""


def get_sentences(filename):
    """Beolvassa a megadott fájlt, és visszaadja a mondatainak listáját.

    A mondatvégi írásjelek (., !, ?) után szóköz van, kivéve a fájl végén.
    Feltételezzük, hogy ezek az írásjelek csak a mondatok végén szerepelnek, és a
    mondatok nem tartalmaznak sortörést.
    A visszaadott listában a mondatok elején és végén nincs szóköz.

    >>> get_sentences("hf3_pelda.txt")
    ['This is a sentence.', 'Wow, another one, is it?', 'Okay, enough now!', 'This is a sentence of the second paragraph.']
    """
    # tipp: először minden mondatvégi írásjel után szúrj be egy # jelet a szövegbe,
    # majd ezek mentén darabold fel
    new_list = []
    with open("hf3_pelda.txt", "r") as f:
        for line in f:
            help = line.replace("!","!#").replace(".",".#").replace("?","?#")
            new_list += help.split("#")
        while "\n" in new_list:
            new_list.remove("\n")
    f.close()
    del new_list[-1]
    return new_list


def get_longest_sentence(filename):
    """Beolvassa a megadott fájlt, és visszaadja az első leghosszabb mondatot.

    >>> get_longest_sentence("hf3_pelda.txt")
    'This is a sentence of the second paragraph.'
    """
    sentences = get_sentences(filename)
    longest = ""
    max = 0
    for sentence in sentences:
        if len(sentence) > max:
            max = len(sentence)
            longest = sentence
    return longest


def get_shortest_sentence(filename):
    """Beolvassa a megadott fájlt, és visszaadja az első legrövidebb mondatot.

    >>> get_shortest_sentence("hf3_pelda.txt")
    'Okay, enough now!'
    """
    sentences = get_sentences(filename)
    shortest = ""
    min = 0
    for sentence in sentences:
        if min == 0:
            min = len(sentence)
        if len(sentence) < min:
            min = len(sentence)
            shortest = sentence
    return shortest


def count_questions(filename):
    """Beolvassa a megadott fájlt, és visszaadja a kérdőmondatok számát.

    >>> count_questions("hf3_pelda.txt")
    1
    """
    counter = 0
    sentences = get_sentences(filename)
    for sentence in sentences:
        if sentence[-1] == "?":
            counter +=1
    return counter

def count_word(filename, word):
    """Beolvassa a megadott fájlt, és visszaadja, hogy az adott szó hány alkalommal
    fordul elő benne.

    A kis- és nagybetűket nem különbözteti meg.
    A szavak után álló írásjelek (.!?,;:) nem tartoznak a szóhoz!

    >>> count_word("hf3_pelda.txt", "is")
    3
    >>> count_word("hf3_pelda.txt", "this")
    2
    >>> count_word("hf3_pelda.txt", "wow")
    1
    >>> count_word("hf3_pelda.txt", "missing")
    0
    """
    counter = 0
    sentences = get_sentences(filename)
    for sentence in sentences:
        words = sentence.split()
        for w in words: #w=word, csak már argban létezik ilyen elnevezés
            w = w.lower().rstrip('.!?,;:')
            if w == word.lower():
                counter += 1
    return counter

print(count_word("hf3_pelda.txt", "wow"))
def most_frequent_word(filename, min_length=1):
    """Beolvassa a megadott fájlt, és visszaadja az első leggyakoribb szót.

    A 2. paraméter megadja, hogy legalább milyen hosszú szavakat vegyen figyelembe.
    Ha nincs ilyen szó, akkor üres stringet ad vissza.

    A kis- és nagybetűket nem különbözteti meg.
    A szavak után álló írásjeleket (.!?,;:) nem veszi figyelembe.

    >>> most_frequent_word("hf3_pelda.txt")
    'is'
    >>> most_frequent_word("hf3_pelda.txt", 3)
    'this'
    """
    word_counts = {}
    sentences = get_sentences(filename)
    
    for sentence in sentences:
        words = sentence.split()
        for w in words: #w=word, csak már argban létezik ilyen elnevezés
            w = w.lower().rstrip('.!?,;:')
            word_counts[w] = word_counts.get(w, 0) + 1

    max_count = 0
    most_used_word = " "
    for word, count in word_counts.items():
        if count > max_count and len(word) > min_length:
            max_count = count
            most_used_word = word
    return most_used_word