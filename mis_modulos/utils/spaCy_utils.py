# pip3 install spacy
import spacy
import spacy.tokens

from utils.vanilla_utils import list_one_to_one_package, clean_text

"""
string_tokenizer('Hello, world!', get_nlp_punctuation_marks(), False)

    ['Hello', ',', 'world', '!']

join_sentence(['This', 'is', 'a', 'sentence'])
    
    'This is a sentence'
        
get_pos_list_from_string('This is a test.', get_nlp_punctuation_marks(), False)

    ['POS_A', 'POS_B', 'POS_C', 'POS_D', 'POS_E']
        
get_tag_list_from_string('This is a test.', get_nlp_punctuation_marks(), False)

    ['TAG_A', 'TAG_B', 'TAG_C', 'TAG_D', 'TAG_E']

tokenize_string_and_analyze_sintactically("Hola, ¿cómo estás?", False)

    ['Hola', ',', '¿', 'cómo', 'estás', '?']
    ['INTJ', 'PUNCT', 'PUNCT', 'ADV', 'VERB', 'PUNCT']


string_tokens_and_sintactical_analysis_package('Hello World', get_nlp_punctuation_marks(), False)

    [['Hello', 'World'], ['VERB', 'NOUN']]

find_word_pos_and_surroundings('Esto es una prueba.', 'una')

    [['es', 'VERB'], ['una', 'DET'], ['prueba', 'NOUN']]

unpack_word_pos_and_surroundings(("hello", "NOUN"), ("my", "PROPN"), ("friend", "NOUN")))

    ("hello", "NOUN", "my", "PROPN", "friend", "NOUN")

get_universal_pos_tags()

    ['ADJ', 'ADP', 'ADV', 'AUX', 'CONJ', 'CCONJ', 'DET', 'INTJ', 'NOUN', 'NUM', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X', 'EOL', 'SPACE']
"""


def string_tokenizer(text, word_delimiters, debug_mode):
    """
    This function takes a string and a list of delimiters as inputs.
    It returns a list of strings, each string being a token of the input string.

    Inputs:
        text: a string
        word_delimiters: a list of strings
        debug_mode: a boolean

    Output:
        tokenized_sentence: a list of strings

    Example:
        text = "Hello, world!"
        word_delimiters = [' ', ',', '!']
        debug_mode = False
        tokenized_sentence = string_tokenizer(text, word_delimiters, debug_mode)
        print(tokenized_sentence)
    """

    # Returning list initialization
    tokenized_sentence = []

    doc = private_common_lvl_1__initialize_spacy_doc(text, word_delimiters, debug_mode)

    # Text printing in debug mode
    if debug_mode:
        print("\nANALYSIS\n")

    # Going through the list
    for token in doc:
        # Text printing in debug mode
        if debug_mode:
            print("\t", token.text, token.pos_, token.dep_, token.head.text)

        if token.text != '' or token.text != ' ':
            # Push each token inside a list
            tokenized_sentence.append(str(token.text))

    return tokenized_sentence


def join_sentence(tokenized_sentence):
    """
    This function joins a list of strings into a sentence.

    Parameters:
        tokenized_sentence (list): A list of strings.

    Returns:
        joined_sentence (str): A sentence made up of the strings in the list.

    Example:
        >>> join_sentence(['This', 'is', 'a', 'sentence'])
        'This is a sentence'
    """
    count = 0
    length = len(tokenized_sentence)

    joined_sentence = ''

    for element in tokenized_sentence:
        if count != length - 1:
            joined_sentence += str(element) + ' '
        else:
            joined_sentence += str(element)

        count += 1

    return joined_sentence


def get_pos_list_from_string(text, word_delimiters, debug_mode):
    """
    This function takes a string and returns a list of the part of speech tags for each word in the string.
    The function uses the spacy library to do this.
    The function also takes a list of word delimiters, which are characters that are used to separate words.
    The function uses the word delimiters to split the string into a list of words.
    The function then uses the spacy library to get the part of speech tags for each word in the list.
    The function then returns a list of the part of speech tags for each word in the string.
    The function also takes a debug mode parameter, which is a boolean value.
    If the debug mode parameter is set to True, the function will print out the list of words and the list of part of speech tags.
    If the debug mode parameter is set to False, the function will not print out the list of words and the list of part of speech tags.
    The function returns a list of the part of speech tags for each word in the string.

    Parameters:
    text (str): The string to get the part of speech tags for.
    word_delimiters (list): A list of characters that are used to separate words.
    debug_mode (bool): A boolean value that determines whether or not the function will print out the list of words and the list of part of speech tags.

    Returns:
    list: A list of the part of speech tags for each word in the string.

    Example:
    >>> get_pos_list_from_string('The quick brown fox jumped over the lazy dog.', [' ', '.', ','], True)

    ['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog', '.']
    ['DET', 'ADJ', 'ADJ', 'NOUN', 'VERB', 'ADP', 'DET', 'ADJ', 'NOUN', 'PUNCT']

        ['DET', 'ADJ', 'ADJ', 'NOUN', 'VERB', 'ADP', 'DET', 'ADJ', 'NOUN', 'PUNCT']
    """
    return private_supra_lvl_1__get_spacy_attributes_list_from_string(text, word_delimiters, 'pos_', debug_mode)


def get_tag_list_from_string(text, word_delimiters, debug_mode):
    """
    This function takes a string and returns a list of the tags of the words in the string.
    The tags are the part of speech tags.
    The tags are returned as a list of strings.
    The tags are returned in the same order as the words in the string.
    The tags are returned as lowercase strings.
    The tags are returned without the '_' character.
    The tags are returned without the 'B-' and 'I-' prefixes.
    The tags are returned without the '-' character.
    The tags are returned without the '.' character.
    The tags are returned without the '$' character.
    The tags are returned without the ',' character.
    The tags are returned without the ':' character.
    The tags are returned without the '(' character.
    The tags are returned without the ')' character.
    The tags are returned without the '"' character.
    The tags are returned without the '``' character.
    The tags are returned without the '`' character.
    The tags are returned without the ''' character.

    Parameters:
    text (str): The string to be processed.
    word_delimiters (str): The characters that are used to separate words in the string.
    debug_mode (bool): If True, then the function will print out the text and the list of tags.

    Returns:
    list: The list of tags of the words in the string.

    Example:
    >>> get_tag_list_from_string('The quick brown fox jumped over the lazy dog.', ' ', True)
    The quick brown fox jumped over the lazy dog.
    ['det', 'adj', 'adj', 'noun', 'verb', 'prep', 'det', 'adj', 'noun', 'punct']

        ['det', 'adj', 'adj', 'noun', 'verb', 'prep', 'det', 'adj', 'noun', 'punct']
    """
    return private_supra_lvl_1__get_spacy_attributes_list_from_string(text, word_delimiters, 'tag_', debug_mode)


def get_morph_list_from_string(text, word_delimiters, debug_mode):
    """
    This function takes a string and returns a list of the morph attribute of the tokenized words in the string.

    Parameters:
        text (str): The string to be processed.
        word_delimiters (str): The characters that are used to separate words in the string.
        debug_mode (bool): If True, then the function will print out the text and the list of tags.

    Returns:
        list: The list of tags of the words in the string.
    """
    return private_supra_lvl_1__get_spacy_attributes_list_from_string(text, word_delimiters, 'morph', debug_mode)


def private_supra_lvl_1__get_spacy_attributes_list_from_string(text, word_delimiters, attribute, debug_mode):
    """
    This function takes a string and returns a list of strings, each string being a token of the input string.

    Parameters:
        text (string): The string to be analyzed.
        word_delimiters (string): A string containing all the characters that will be considered as word delimiters.
        attribute (string): A string indicating the spaCy attribute to be extracted
        debug_mode (boolean): A boolean indicating if the function should print the analysis in the console.

    Returns:
        tagged_phrase (list): A list of strings, each string being a token of the input string.

    Example:
        string_pos("This is a test.", "", <TAG>, True)

            ANALYSIS
                This TAG_A
                is TAG_B
                a TAG_C
                test TAG_D
                . TAG_E

            ['TAG_A', 'TAG_B', 'TAG_C', 'TAG_D', 'TAG_E']
    """
    # Returning list initialization
    tagged_phrase = []

    doc = private_common_lvl_1__initialize_spacy_doc(text, word_delimiters, debug_mode)

    tagged_phrase = private_common_lvl_1__get_spacy_attribute(debug_mode, doc, attribute)

    return tagged_phrase


def private_common_lvl_1__get_spacy_attribute(debug_mode, doc, attribute):

    attributes = []

    # Text printing in debug mode
    if debug_mode:
        print("\nANALYSIS\n")

    # Going through the list
    for token in doc:
        # Text printing in debug mode
        if debug_mode:
            print("\t", token.text, token.__getattribute__(attribute))

        if token.text != '' or token.text != ' ':
            # Push each token inside a list
            attributes.append(str(token.__getattribute__(attribute)))

    return attributes


def private_common_lvl_1__initialize_spacy_doc(text, word_delimiters, debug_mode):
    """
    Initializes a spacy doc object from a text.

    Example:
        initialize_spacy_doc('Hola, ¿cómo estás?', ' ', True)

    :param text: The text to be processed.
    :param word_delimiters: The word delimiters to be used.
    :param debug_mode: Boolean that turns on the code comments
    :return: A spacy doc object.
    """
    # Load the model and create an nlp object
    nlp = spacy.load("es_core_news_md")

    if isinstance(text, list):
        new_text = ''
        last = 0
        for phrase in text:
            if last == (len(phrase) - 1):
                new_text += phrase
            else:
                new_text += phrase + ' '
            last += 1

        text = new_text

    tokens = text.split(word_delimiters)
    words_t = list(filter(None, [t.strip() for t in tokens]))

    # Text printing in debug mode
    if debug_mode:
        print(str(words_t))

    doc_feed = private_common_lvl_2__get_doc_feed(nlp, words_t)

    # Process the text passed to this method as a parameter
    doc = nlp(doc_feed)

    return doc


def private_common_lvl_2__get_doc_feed(nlp, words_t):
    """
    This function takes a list of words and returns a string of those words
    concatenated together with spaces.

    Parameters:
        nlp: A spaCy Language object.
        words_t: A list of strings.

    Returns:
        A string of the words in the list concatenated with spaces.

    Example:
        get_doc_feed(nlp, ['hello', 'world'])

            'hello world'
    """
    doc_feed = ''
    doc_raw_feed = spacy.tokens.Doc(nlp.vocab, words=words_t)
    doc_feed_count = 0
    doc_feed_length = len(doc_raw_feed)

    for element in doc_raw_feed:
        if doc_feed_count != doc_feed_length - 1:
            doc_feed += str(element) + ' '
        else:
            doc_feed += str(element)

        doc_feed_count += 1

    return doc_feed


def tokenize_string_and_analyze_sintactically(text, debug_mode):
    """
    This function takes a string as a parameter and returns a list of tokens.
    The string is processed by the spacy library.
    The function also returns a list of the analysis of each token.
    The analysis is done by the spacy library.
    The function also takes a boolean as a parameter to enable debug mode.
    The debug mode prints the analysis of each token.

    Parameters:
        text (str): The string to be tokenized.
        debug_mode (bool): The debug mode.

    Returns:
        tokenized_sentence (list): The list of tokens.
        token_analysis (list): The list of the analysis of each token.

    Example:
        >>> tokenize_string_and_analyze_sintactically("Hola, ¿cómo estás?", True)

        ['Hola', ',', '¿', 'cómo', 'estás', '?']
        ['INTJ', 'PUNCT', 'PUNCT', 'ADV', 'VERB', 'PUNCT']
    """
    # Returning list initialization
    tokenized_sentence = []
    token_analysis = []

    # Load the model and create an nlp object
    nlp = spacy.load("es_core_news_md")

    if debug_mode:
        print('\nSTRING TOKENIZER')

    if isinstance(text, list):
        new_text = ''
        last = 0
        for phrase in text:
            if last == (len(phrase) - 1):
                new_text += phrase
            else:
                new_text += phrase + ' '
            last += 1

        text = new_text

    tokens = text.split(' ')
    words_t = list(filter(None, [t.strip() for t in tokens]))

    if debug_mode:
        print('\t' + str(words_t))

    doc_raw_feed = spacy.tokens.Doc(nlp.vocab, words=words_t)

    doc_feed = ''

    doc_feed_count = 0
    doc_feed_length = len(doc_raw_feed)

    for element in doc_raw_feed:
        if doc_feed_count != doc_feed_length - 1:
            doc_feed += str(element) + ' '
        else:
            doc_feed += str(element)

        doc_feed_count += 1

    # Process the text passed to this method as a parameter
    doc = nlp(doc_feed)

    if debug_mode:
        print("\nANALYSIS\n")

    # Going through the list
    for token in doc:

        if debug_mode:
            print("\t", token.text, token.pos_, token.dep_, token.head.text)

        if token.text != '' or token.text != ' ':
            # Push each token inside a list
            tokenized_sentence.append(str(token.text))
            token_analysis.append(str(token.pos_))

    if debug_mode:
        print('\t' + str(tokenized_sentence))
        print('\t' + str(token_analysis))

    return tokenized_sentence, token_analysis


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


def unpack_word_pos_and_surroundings(word_pos_and_surroundings):
    """
    This function takes a word_pos_and_surroundings tuple and returns the
    word, pos, and the surrounding words.

    Parameters:
        word_pos_and_surroundings: A tuple of the form (word, pos,
                                   (left_word, left_pos),
                                   (right_word, right_pos))

    Returns:
        word: The word
        pos: The part of speech
        left_word: The word to the left of the word
        left_pos: The part of speech of the word to the left of the word
        right_word: The word to the right of the word
        right_pos: The part of speech of the word to the right of the word

    Example:
        unpack_word_pos_and_surroundings(("hello", "NOUN"), ("my", "PROPN"), ("friend", "NOUN")))

            ("hello", "NOUN", "my", "PROPN", "friend", "NOUN")
    """
    return word_pos_and_surroundings[0][0], word_pos_and_surroundings[0][1], \
           word_pos_and_surroundings[1][0], word_pos_and_surroundings[1][1], \
           word_pos_and_surroundings[2][0], word_pos_and_surroundings[2][1]


def string_tokens_and_sintactical_analysis_package(text, word_delimiters, debug_mode):
    """
    This function takes a string and returns a list of tokens and a list of sintactical analysis.
    The string is tokenized and the tokens are returned.
    The sintactical analysis is performed on the tokens and the result is returned.
    The function returns a list of two lists.
    The first list is the list of tokens.
    The second list is the list of sintactical analysis.
    The function takes a string and a list of delimiters as input.
    The string is tokenized using the list of delimiters.
    The function returns a list of two lists.

    Parameters:
        text: a string
        word_delimiters: a list of strings
        debug_mode: a boolean

    Returns:
        A list of two lists.
        The first list is the list of tokens.
        The second list is the list of sintactical analysis.

    Example:
        text = "Hello, World!"
        word_delimiters = [","]
        debug_mode = True

        string_tokens_and_sintactical_analysis_package(text, word_delimiters, debug_mode)

        Output:
            [['Hello', 'World'], [['VERB', 'NOUN']]
    """
    tokens = tokenize_string_and_analyze_sintactically(text, word_delimiters, debug_mode)
    sintactical_analysis = get_pos_list_from_string(text, word_delimiters, debug_mode)

    return list_one_to_one_package(tokens, sintactical_analysis)


def find_word_pos_and_surroundings(text, word):
    """

        This function takes a text and a word and returns the previous, actual and next words of the text.

        Parameters:
        text (str): The text to be analysed.
        word (str): The word to be found in the text.

        Returns:
        list: A list with the previous, actual and next words of the text.

        Example:

            find_word_pos_and_surroundings('Esto es una prueba', 'prueba')

            [['una', 'DET'], ['prueba', 'NOUN'], ['', '']]
    """
    nlp = spacy.load("es_core_news_md")

    if isinstance(text, str):
        text = clean_text(text)
        text = nlp(text)

    previous_token_text = ''
    actual_token_text = ''
    next_token_text = ''

    previous_token_pos = ''
    actual_token_pos = ''
    next_token_pos = ''

    found = False

    if isinstance(text, str) or (text != '' and text is not None):
        for token in text:
            if found:
                next_token_text = token.text
                next_token_pos = token.pos_
                break
            if token.text == word:
                actual_token_text = token.text
                actual_token_pos = token.pos_
                found = True
            if not found:
                previous_token_text = token.text
                previous_token_pos = token.pos_

    return [[previous_token_text, previous_token_pos], [actual_token_text, actual_token_pos],
            [next_token_text, next_token_pos]]


def unpack_word_pos_and_surroundings(word_pos_and_surroundings):
    """
        This function takes a word_pos_and_surroundings tuple and returns the
        word, pos, and the surrounding words.

        Parameters:
            word_pos_and_surroundings: A tuple of the form (word, pos,
                                       (left_word, left_pos),
                                       (right_word, right_pos))

        Returns:
            word: The word
            pos: The part of speech
            left_word: The word to the left of the word
            left_pos: The part of speech of the word to the left of the word
            right_word: The word to the right of the word
            right_pos: The part of speech of the word to the right of the word

        Example:
            unpack_word_pos_and_surroundings(("hello", "NOUN"), ("my", "PROPN"), ("friend", "NOUN")))

                ("hello", "NOUN", "my", "PROPN", "friend", "NOUN")
    """
    return word_pos_and_surroundings[0][0], word_pos_and_surroundings[0][1], \
           word_pos_and_surroundings[1][0], word_pos_and_surroundings[1][1], \
           word_pos_and_surroundings[2][0], word_pos_and_surroundings[2][1]


def get_universal_pos_tags():
    """
        This function returns a list of all the universal POS tags.

    Parameters
    ----------
    None

    Returns
    -------
    list
        A list of all the universal POS tags.

    Examples
    --------
    >>> get_universal_pos_tags()

        ['ADJ', 'ADP', 'ADV', 'AUX', 'CONJ', 'CCONJ', 'DET', 'INTJ', 'NOUN', 'NUM', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X', 'EOL', 'SPACE']
    """

    glossary = {
        "ADJ": "adjective",
        "ADP": "adposition",
        "ADV": "adverb",
        "AUX": "auxiliary",
        "CONJ": "conjunction",
        "CCONJ": "coordinating conjunction",
        "DET": "determiner",
        "INTJ": "interjection",
        "NOUN": "noun",
        "NUM": "numeral",
        "PART": "particle",
        "PRON": "pronoun",
        "PROPN": "proper noun",
        "PUNCT": "punctuation",
        "SCONJ": "subordinating conjunction",
        "SYM": "symbol",
        "VERB": "verb",
        "X": "other",
        "EOL": "end of line",
        "SPACE": "space",
    }

    return glossary.keys()
