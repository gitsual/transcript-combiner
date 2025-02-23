import re

"""
get_substring_without_blank_lines_at_the_beggining_and_at_the_end('    this is a test   ')

    'this is a test'

delete_spaces_tabs_and_newlines('esto   es\\tun  ejemplo\\n')

    'estoesunejemplo'

delete_tilde('árbol')

    'arbol'

clean_text('  This is a test string! ')

    'this is a test string'

find_sentence_of_word('This is a test. This is another.', 'test')

    'This is a test.'

string_package('Hello', 'World')

    ['Hello', 'World']

list_one_to_one_package([1, 2, 3], ['a', 'b', 'c'])

    [[1, 'a'], [2, 'b'], [3, 'c']]

get_nlp_punctuation_marks()

    ['!', '¡', '?', '¿', '%', ',', '...', '.', '…', ':', ';', '<', '>', '"', '·', '$', '%', '&', '/', '(', ')', '=', '\'', '|', '@', '#', '~', '½', '¬', '{', '[' ']', '}', '_', '€', '`', '*', '^', '+', '€', '’', '“', '”', '«', '»', '—']
"""


def get_substring_without_blank_lines_at_the_beggining_and_at_the_end(line):
    """
    This function returns a substring of a given string, without blank lines at the beggining and at the end.

    Parameters:
        line (str): The string to be processed.

    Returns:
        str: The substring of the given string, without blank lines at the beggining and at the end.

    Example:
        >>> get_substring_without_blank_lines_at_the_beggining_and_at_the_end('    this is a test   ')
        'this is a test'
    """
    first_char_index_not_blank = 0
    last_char_index_not_blank = 0
    first = False
    for index, char in enumerate(line):
        if char != ' ' and char != '\n':
            if not first:
                first_char_index_not_blank = index
                first = True
            else:
                last_char_index_not_blank = index
    print('[vanilla_utils] get_substring_without_blank_lines_at_the_beggining_and_at_the_end: ' + str(line[first_char_index_not_blank:last_char_index_not_blank]))
    return line[first_char_index_not_blank:last_char_index_not_blank+1]


def delete_spaces_tabs_and_newlines(word_phrase_type):
    """
    This function takes a word or phrase type as input and returns the same word or phrase type with all spaces, tabs, and newlines removed.

    Parameters:
        word_phrase_type (str): A word or phrase type.

    Returns:
        str: The same word or phrase type with all spaces, tabs, and newlines removed.

    Example:
    >>> delete_spaces_tabs_and_newlines('esto   es\\tun  ejemplo\\n')

        'estoesunejemplo'
    """
    return word_phrase_type[0].replace('\n', '').replace('\t', '').replace(' ', '')


def delete_tilde(text):
    """
    This function takes a string as input and returns the same string with all the tildes removed.
    The tildes are replaced by the corresponding letter without the tilde.
    For example, the string 'árbol' would be returned as 'arbol'.

    Parameters:
    text (str): The string to be processed.

    Returns:
    str: The string with all the tildes removed.

    Example:
    >>> delete_tilde('árbol')
        'arbol'
    """
    return text.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')\
        .replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')


def clean_text(text):
    """
    Cleans text by removing special characters and extra whitespace.
    """
    # Remove special characters and normalize whitespace
    cleaned = ' '.join(text.split())
    return cleaned


def find_sentence_of_word(text, word):
    """
    This function takes two strings as input and returns a string.

    If the input is not a string, it returns the input.
    If the input is a string, it splits the string by '.' and then returns the sentence containing the word.
    If the word is not in the sentence, it returns the sentence.
    If the word is in the sentence, it returns the sentence containing the word.
    If the word is in the sentence and the word contains '.', it returns the sentence containing the word without the '.'.

    Parameters:
        text (str): The text to be split by '.'
        word (str): The word to be searched in the text

    Returns:
        str: The sentence containing the word or the sentence itself.

    Example:
        find_sentence_of_word('This is a test. This is another.', 'test')

            'This is a test.'
    """

    if isinstance(text, str) and isinstance(word, str):
        text = text.split('.')
        for sentence in text:
            if word in sentence:
                return sentence
    else:
        return text


def string_package(string_1, string_2):
    """
    This function takes two strings and returns a list containing them.

    Parameters:
        string_1 (str): The first string.
        string_2 (str): The second string.

    Returns:
        list: A list containing the two strings.

    Example:
        >>> string_package('Hello', 'World')
        ['Hello', 'World']
    """
    result = []

    result.append(string_1)
    result.append(string_2)

    return result


def list_one_to_one_package(list1, list2):
    """
    Takes two lists and returns a dictionary mapping elements from list1 to list2.
    """
    return dict(zip(list1, list2))


def get_nlp_punctuation_marks():
    """
    Returns a list of punctuation marks used in NLP.
    """
    return ['.', ',', ';', ':', '!', '?', '¡', '¿', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '/', '\\', '|', '@', '#', '$', '%', '^', '&', '*', '+', '=', '<', '>', '~', '`']
