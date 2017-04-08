import re

ALLOWED_SYMBOLS = list("abcdefghijklmnopqrstuvwxyz1234567890 \n.,():;-!?'\"")
CHARACTERS_TO_SPLIT = """.,():;-!?\n\""""
REPLACEMENTS = {
    "\x05": " ",
    "&": "and"
}


def tokenize_strip_non_words(raw):
    """
    Same as tokenize_words, but also removes non-word characters
    """
    return [t for t in tokenize_words(raw) if t not in
            CHARACTERS_TO_SPLIT + "\n"]


def normalise(s):
    """
    Basic string normalisation

    :param s: input string
    :return: normalised string
    """
    s = s.encode("ascii", "ignore").decode("ascii")
    s = s.lower()
    s = s.strip()
    s = re.sub(r"\n\n+", "\n\n", s)
    s = re.sub(r"\.\.\.+", "...", s)

    for k, v in REPLACEMENTS.items():
        s = s.replace(k, v)

    symbols = set(s)
    for c in symbols:
        if c not in ALLOWED_SYMBOLS:
            s = s.replace(c, "")

    return s


def tokenize_words(raw):
    """
    Tokenizes strings by splitting them on spaces, line breaks or characters
    in CHARACTERS_TO_SPLIT.

    :param raw: string to split
    :return: list of tokens
    """
    tokenized = []
    temp_string = ""
    raw = normalise(raw)

    for cc in raw:
        c = cc
        
        if c == " ":
            if temp_string != "":
                tokenized.append(temp_string)
                temp_string = ""
        elif c in CHARACTERS_TO_SPLIT:
            if temp_string != "":
                tokenized.append(temp_string)
            tokenized.append(c)
            temp_string = ""
        else:
            temp_string += c

    if temp_string != "":
        tokenized.append(temp_string)

    return tokenized


def tokenized_pretty_print(tokens):
    """"
    Pretty print function for strings tokenized by tokenize_words

    :param tokens: list of tokens
    :return: string
    """
    out = ""
    for t in tokens:
        if t in ".,):!?":
            if out[-1] == " ":
                out = out[:-1]
            out += t + " "
        elif t in "(":
            out += t
        elif t in "-\n":
            if out[-1] == " ":
                out = out[:-1]
            out += t
        else:
            out += t + " "
    return out
