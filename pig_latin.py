from string import ascii_uppercase, ascii_lowercase


def append(w, suffix):

    if not w:
        return suffix
    elif w[-1] in ascii_uppercase:
        return w + suffix.upper()
    else:
        return w + suffix.lower()


def piglatin_tranlator(sentence):
    """
    takes a sentence in English and translate
    into Latin pig"""

    # Non string should return an error
    if not isinstance(sentence, str):
        return 'The phrase to translate should be a string'

    output = ''
    for word in sentence.split(' '):
        if word:
            # check for punctuation
            p = 0
            while word[p-1] not in ascii_uppercase+ascii_lowercase:
                p = p-1
            if p:
                punc = word[p:]
                word = word[:p]
            else:
                punc = ''

            # and pre-punc (e.g., parentheses)
            p = 0
            while word[p] not in ascii_uppercase+ascii_lowercase:
                p = p+1
            prepunc = word[:p]
            word = word[p:]

            # note capitalization
            if word[0] in ascii_uppercase:
                caps = 1
            else:
                caps = 0

            # remove up to the first vowel to make suffix
            p = 0
            while p < len(word) and word[p] not in "aoeuiyAOEUIY":
                p = p+1

            if not p:
                word = append(word, "ay")
            else:
                word = append(word[p:], word[:p]+"ay")

            # recapitalize, as appropriate
            if caps:
                word = word[0].upper() + word[1:]

            # restore any punctuation
            word = prepunc + word + punc

        output = output + ' ' + word
    return output[1:]
