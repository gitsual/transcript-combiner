import re
import sys
from pathlib import Path

sys.setrecursionlimit(15000)

from src.utils.spacy_utils import string_tokenizer
from src.utils.text_utils import get_nlp_punctuation_marks
from src.config import OUTPUT_DIR


def process_files(pixel_6_file, youtube_subtitles_file, output_dir=None):
    """
    Combina dos archivos de transcripción en una transcripción coherente.
    """
    file_name = str(pixel_6_file).split('/')[-1]
    
    # Leer archivos
    with open(pixel_6_file, 'r') as f:
        pixel_text = f.read()
    with open(youtube_subtitles_file, 'r') as f:
        youtube_text = f.read()
        
    # Combinar transcripciones usando el nuevo procesador
    from src.transcript_processor import combine_transcripts
    combined_text = combine_transcripts(youtube_text, pixel_text)
    
    # Formatear título
    title = f"# {file_name.split('.')[0].capitalize().replace('_', ' ')}"
    final_text = f"{title}\n\n{combined_text}"
    
    # Escribir archivo
    write_file(file_name, final_text, output_dir)
    
    return file_name, final_text


def format_transcript(word_sequence):
    """Format the word sequence into a proper transcript with timestamps and paragraphs."""
    # Iniciar con el timestamp
    formatted_lines = ["[00:05]"]
    
    current_sentence = []
    for word in word_sequence:
        # Ignorar palabras vacías
        if not word.strip():
            continue
            
        # Si es un signo de puntuación que termina oración
        if word in ['.', '!', '?']:
            if current_sentence:
                current_sentence.append(word)
                sentence = ' '.join(current_sentence).strip()
                # Eliminar espacios antes de puntuación
                sentence = sentence.replace(' .', '.').replace(' !', '!').replace(' ?', '?')
                formatted_lines.append(sentence)
                current_sentence = []
        # Si es otro tipo de puntuación
        elif word in [',', ';', ':', '-']:
            if current_sentence:
                current_sentence[-1] = current_sentence[-1] + word
            else:
                current_sentence.append(word)
        # Si es una palabra normal
        else:
            if not current_sentence:
                # Capitalizar primera palabra de cada oración
                word = word[0].upper() + word[1:] if len(word) > 1 else word.upper()
            current_sentence.append(word)
    
    # Agregar última oración si existe
    if current_sentence:
        formatted_lines.append(' '.join(current_sentence).strip())
    
    # Agrupar en párrafos basados en puntos finales
    paragraphs = []
    current_paragraph = []
    
    for line in formatted_lines:
        if line.startswith('['):
            if current_paragraph:
                paragraphs.append(' '.join(current_paragraph))
            current_paragraph = [line]
        else:
            current_paragraph.append(line)
            # Crear nuevo párrafo después de ciertos signos de puntuación
            if line.endswith(('.', '!', '?')) and len(current_paragraph) > 3:
                paragraphs.append(' '.join(current_paragraph))
                current_paragraph = []
    
    if current_paragraph:
        paragraphs.append(' '.join(current_paragraph))
    
    # Unir párrafos con doble salto de línea
    return '\n\n'.join(paragraphs)


def format_final_output(file_name, content):
    """Format the final output with title and proper structure."""
    # Crear título
    title = '# ' + str(file_name.split('.')[0].capitalize().replace('_', ' '))
    
    # Limpiar espacios extra y puntuación
    content = content.replace(' .', '.').replace(' ,', ',').replace(' !', '!').replace(' ?', '?')
    content = content.replace('..', '.').replace(',,', ',').replace('!!', '!').replace('??', '?')
    content = content.replace('  ', ' ').strip()
    
    # Asegurar que hay un espacio después de cada signo de puntuación
    for punct in ['.', ',', '!', '?']:
        content = content.replace(f"{punct}", f"{punct} ")
        content = content.replace(f"{punct}  ", f"{punct} ")
    
    # Unir todo con el formato correcto
    return f"{title}\n\n{content}"


def read_file_content(file):
    """
    Reads the content of a file and returns it as a list of strings.

    Parameters
    ----------
    file : str
        The path to the file to read.

    Returns
    -------
    list
        A list of strings, each string being a line from the file.

    Examples
    --------
    >>> read_file_content('test.txt')
        ['This is a test file.', 'It has two lines.']
    """
    file_content = []

    with open(file, 'r') as f:
        file_content = f.readlines()

    return file_content


def get_files_content(pixel_6_file, youtube_subtitles_file):
    """
    This function reads the content of the files and returns the content of the files.
    :param pixel_6_file: The file containing the Pixel 6 subtitles.
    :param youtube_subtitles_file: The file containing the YouTube subtitles.
    :return: The content of the files.

    Example:
    >>> get_files_content('pixel_6.txt', 'youtube_subtitles.txt')
        ('Pixel 6. The phone that helps you do more.\n', 'Youtube test.\n')
    """
    pixel_6_file_content = read_file_content(pixel_6_file)
    youtube_subtitles_file = read_file_content(youtube_subtitles_file)

    return pixel_6_file_content, youtube_subtitles_file


def clean_file_content(list_of_strings):
    """
    This function takes a list of strings as input and returns a new list of strings.
    The new list contains only the strings that are not empty, do not contain only
    digits and colons, and do not contain only a newline character.

    Parameters:
    list_of_strings (list): A list of strings.

    Returns:
    list: A list of strings.

    Examples:
    >>> clean_file_content(['', '\\n']
        []
    >>> clean_file_content(['', '\\n', '12 00\\n', '\\n', '[12:00]']
        ['12 00']
    """
    new_list = []
    for string in list_of_strings:
        if not re.match(r'^\d{2}:\d{2}$', string) and string != '\n' and string != '':
            new_list.append(string.replace('\n', ''))
    return new_list


def clean_files_content(pixel_6_file_content, youtube_subtitles_file_content):
    """
        This function takes in two file contents and returns two cleaned file contents.
        The cleaning process is as follows:
            1. Remove all punctuation
            2. Remove all numbers
            3. Remove all special characters
            4. Remove all whitespace
            5. Convert all characters to lowercase
            6. Remove all words that are not in the English dictionary
        The function returns two cleaned file contents.

        Example:
            >>> clean_files_content("Hello, world!", "Hello, world!")
            ("helloworld", "helloworld")
    """
    pixel_6_file_content_clean = clean_file_content(pixel_6_file_content)
    youtube_subtitles_file_content_clean = clean_file_content(youtube_subtitles_file_content)

    return pixel_6_file_content_clean, youtube_subtitles_file_content_clean


def create_dictionaries(list1, list2):
    """
    This function takes two lists of strings and returns two dictionaries.
    The first dictionary has the word number as the key and the word as the value.
    The second dictionary has the word number as the key and the word as the value.
    The word number is the position of the word in the string.
    The word is the token.
    The string is the concatenation of the list of strings.
    The concatenation of the list of strings is the list of strings joined together with a space.
    The list of strings is the list of strings in the list of strings.

    Parameters:
    list1 (list): A list of strings.
    list2 (list): A list of strings.

    Returns:
    dictionary1 (dict): A dictionary where the key is the word number and the value is the token.
    dictionary2 (dict): A dictionary where the key is the word number and the value is the token.

    Example:
    >>> create_dictionaries(['This is a sentence.', 'This is another sentence.'], ['Another sentence apart.', 'Another sentence already.'])
        ({0: 'This', 1: 'is', 2: 'a', 3: 'sentence', 4: 'This', 5: 'is', 6: 'another', 7: 'sentence'}, {0: 'Another', 1: 'sentence', 2: 'apart', 3: 'Another', 4: 'sentence', 5: 'already'})
    """
    # Convert list1 into a string
    list1_string = ' '.join(list1)

    # Convert list2 into a string
    list2_string = ' '.join(list2)

    # Create a list of all the words in list1
    list1_words = string_tokenizer(list1_string, ' '.join(get_nlp_punctuation_marks()), False)

    # Create a list of all the words in list2
    list2_words = string_tokenizer(list2_string, ' '.join(get_nlp_punctuation_marks()), False)

    # Create a dictionary where key is the word number and value is the token
    dictionary1 = {i: list1_words[i] for i in range(len(list1_words))}

    # Create a dictionary where key is the word number and value is the token
    dictionary2 = {i: list2_words[i] for i in range(len(list2_words))}

    return dictionary1, dictionary2


def get_numbered_words_of_files(pixel_6_file, youtube_subtitles_file):
    """
    This function takes two files as input, one is the Pixel 6 recorder file and
    the other is the YouTube subtitles file.

    It returns two dictionaries, one for each file.

    The keys of the dictionaries are the words of the files and the values are the
    number of times the words appear in the files.

    The words are in lower case and the punctuation marks are removed.

    Parameters
    ----------------
    pixel_6_file: str
        The name of the Pixel 6 file.
    youtube_subtitles_file: str
        The name of the YouTube subtitles file.

    Returns
    ----------------
    pixel_6_file_content_clean_dictionary: dict
        The dictionary of the Pixel 6 file.
    youtube_subtitles_file_content_clean_dictionary: dict
        The dictionary of the YouTube subtitles file.

    Examples
    ----------------
    >>> pixel_6_file_content_clean_dictionary, youtube_subtitles_file_content_clean_dictionary = get_numbered_words_of_files('pixel_6.txt', 'youtube_subtitles.txt')
    >>> pixel_6_file_content_clean_dictionary
        {'google': 1, 'pixel': 1, '6': 1, 'the': 1, 'phone': 1, 'that': 1, 'helps': 1, 'you': 1, 'get': 1, 'things': 1, 'done': 1, 'fast': 1, 'and': 1, 'keeps': 1, 'you': 1, 'safe': 1, 'with': 1, 'the': 1, 'google': 1, 'assistant': 1, 'built': 1, 'in': 1, 'learn': 1, 'more': 1, 'at': 1, 'google': 1, 'com': 1, 'pixel': 1}
    >>> youtube_subtitles_file_content_clean_dictionary
        {'hello': 1, 'world': 1, 'this': 1, 'is': 1, 'a': 1, 'test': 1, 'of': 1, 'the': 1, 'youtube': 1, 'subtitles': 1, 'system': 1, 'please': 1, 'ignore': 1, 'this': 1, 'video': 1, 'thank': 1, 'you': 1}
    """
    pixel_6_file_content, youtube_subtitles_file_content = get_files_content(pixel_6_file, youtube_subtitles_file)
    pixel_6_file_content_clean, youtube_subtitles_file_content_clean = clean_files_content(pixel_6_file_content,
                                                                                           youtube_subtitles_file_content)
    pixel_6_file_content_clean_dictionary, youtube_subtitles_file_content_clean_dictionary = create_dictionaries(
        pixel_6_file_content_clean,
        youtube_subtitles_file_content_clean)
    return pixel_6_file_content_clean_dictionary, youtube_subtitles_file_content_clean_dictionary


def ordered_word_dicts(dict1, dict2):
    """
    This function takes two dictionaries as input and returns two dictionaries as output.
    The first output dictionary has the keys of the first input dictionary and the values of the second input dictionary.
    The second output dictionary has the keys of the second input dictionary and the values of the first input dictionary.
    The keys and values of the output dictionaries are ordered in the same way as the input dictionaries.
    The values of the output dictionaries are lowercase.
    If a value of the first input dictionary is not in the second input dictionary, it is not in the first output dictionary.
    If a value of the second input dictionary is not in the first input dictionary, it is not in the second output dictionary.
    If a value of the first input dictionary is in the second input dictionary, it is in the first output dictionary.
    If a value of the second input dictionary is in the first input dictionary, it is in the second output dictionary.
    If a value of the first input dictionary is in the second input dictionary more than once, it is in the first output dictionary more than once.
    If a value of the second input dictionary is in the first input dictionary more than once, it is in the second output dictionary more than once.
    If a value of the first input dictionary is in the second input dictionary more than once, it is in the first output dictionary more than once.

    Parameters:
    dict1 (dict): The first input dictionary.
    dict2 (dict): The second input dictionary.

    Returns:
    result1 (dict): The first output dictionary.
    result2 (dict): The second output dictionary.

    Example:
    >>> ordered_word_dicts({'a': 'apple', 'b': 'banana', 'c': 'cherry'}, {'d': 'apple', 'e': 'eggplant', 'f': 'fig'})
        ({'apple': ['a', 'd'], 'banana': ['b'], 'cherry': ['c']}, {'apple': ['a', 'd'], 'eggplant': ['e'], 'fig': ['f']})
    """
    result1 = {}
    dict2_values_lower = []
    for value in dict2.values():
        dict2_values_lower.append(value.lower())

    for key in dict1:
        if dict1[key] in dict2_values_lower:
            if not result1.get(dict1[key]):
                result1[dict1[key]] = []
            result1[dict1[key]].append(key)

    result2 = {}
    for key in dict2:
        if dict2[key].lower() in dict1.values():
            if not result2.get(dict2[key]):
                result2[dict2[key]] = []
            result2[dict2[key]].append(key)
    return result1, result2


def get_common_words(dict_1, dict_2):
    """
    This function takes two dictionaries as input and returns a dictionary
    containing the common words between the two dictionaries.
    The keys of the returned dictionary are the common words and the values
    are lists of the line numbers where the words appear.
    The line numbers are represented as strings in the format 'x-y' where x
    is the line number in the first dictionary and y is the line number in
    the second dictionary.
    The line numbers are sorted in ascending order.
    The words are case insensitive.
    The words are sorted in ascending order.

    Parameters:
        dict_1 (dict): The first dictionary.
        dict_2 (dict): The second dictionary.

    Returns:
        dict: A dictionary containing the common words between the two dictionaries.

    Example:
    >>> get_common_words({'hello': [1, 2, 3], 'world': [1, 2, 3]}, {'hello': [1, 2, 3], 'world': [1, 2, 3]})
        {'hello': ['1-1', '2-2', '3-3'], 'world': ['1-1', '2-2', '3-3']}
    """
    result_dict = {}
    for word in dict_2:
        if word.lower() in dict_1:
            result = []
            for digit_1 in dict_1[word.lower()]:
                for digit_2 in dict_2[word]:
                    result.append(str(str(digit_1) + '-' + str(digit_2)))
            result_dict[word] = result
    return result_dict


def get_lowest_index(d):
    """
    This function takes a dictionary as an argument.
    The dictionary has keys that are strings and values that are lists of strings.
    The strings in the lists are in the format of 'first_index-second_index'.
    The function returns the key of the dictionary that has the lowest first_index.
    If there are multiple keys with the same lowest first_index, the function returns the key with the lowest second_index.
    If there are multiple keys with the same lowest first_index and second_index, the function returns the first key it finds.

    Parameters:
        d (dict): A dictionary with keys that are strings and values that are lists of strings.

    Returns:
        lowest_key (str): The key of the dictionary that has the lowest first_index.
        lowest_index (int): The lowest first_index.
        lowest_second_index (int): The lowest second_index.

    Example:
    >>> d = {'a': ['1-2', '3-4'], 'b': ['5-6', '7-8'], 'c': ['9-10', '11-12']}
    >>> get_lowest_index(d)
        ('a', 1, 2)
    """
    lowest_index = None
    lowest_second_index = None
    lowest_key = ''
    for key, value in d.items():
        for i in value:
            first_index, second_index = i.split('-')
            if lowest_index is None or lowest_index > int(first_index):
                lowest_index = int(first_index)
                lowest_second_index = int(second_index)
                lowest_key = key
            elif lowest_index == int(first_index) and lowest_second_index > int(second_index):
                lowest_second_index = int(second_index)
                lowest_key = key
    return lowest_key, lowest_index, lowest_second_index


def get_first_word(longest_common_words_path):
    """
    This function takes in a dictionary of words and their corresponding index pairs.
    It then returns the word with the lowest index pair.

    Parameters:
        longest_common_words_path (dict): A dictionary of words and their corresponding index pairs.

    Returns:
        str: The word with the lowest index pair.

    Example:
    >>> get_first_word({'hello': ['1-1', '2-2', '3-3'], 'world': ['0-0', '1-1', '2-2']})
        'world'
    """
    i = 0
    candidates = {}
    while i < 5:
        for word in longest_common_words_path.keys():
            for index_pair in longest_common_words_path[word]:
                if index_pair.split('-')[1] == str(i):
                    if word not in candidates:
                        candidates[word] = [index_pair]
                    else:
                        candidates[word].append(index_pair)
        i += 1

    final_candidate_dict = {}

    for candidate in candidates.keys():
        for index_pair in candidates[candidate]:
            if abs(int(index_pair.split('-')[0]) - int(index_pair.split('-')[0])) <= 20:
                if candidate not in final_candidate_dict:
                    final_candidate_dict[candidate] = [index_pair]
                else:
                    final_candidate_dict[candidate].append(index_pair)

    return get_lowest_index(final_candidate_dict)


def delete_inferiors(longest_common_words_path, filter_first_index, filter_last_index):
    """
    This function takes in a dictionary of longest common words paths and two integers.
    It returns a dictionary of longest common words paths with all the paths that have
    first index greater than the first integer and second index greater than the second
    integer.

    Parameters:
        longest_common_words_path (dict): A dictionary of longest common words paths.
        filter_first_index (int): An integer to filter the first index of the paths.
        filter_last_index (int): An integer to filter the second index of the paths.

    Returns:
        filtered_longest_common_words_path (dict): A dictionary of longest common words paths
        with all the paths that have first index greater than the first integer and second
        index greater than the second integer.

    Example:
    >>> delete_inferiors({'a': ['1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22', '22-23', '23-24', '24-25', '25-26', '26-27', '27-28', '28-29', '29-30', '30-31', '31-32', '32-33', '33-34', '34-35', '35-36', '36-37', '37-38', '38-39', '39-40']}, 9, 11)
        {'a': ['12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22', '22-23', '23-24', '24-25', '25-26', '26-27', '27-28', '28-29', '29-30', '30-31', '31-32', '32-33', '33-34', '34-35', '35-36', '36-37', '37-38', '38-39', '39-40']}
    """
    filtered_longest_common_words_path = {}

    for key in longest_common_words_path:
        for i in longest_common_words_path[key]:
            first_index, second_index = i.split('-')
            if int(first_index) > int(filter_first_index) and int(second_index) > int(filter_last_index):
                if key not in filtered_longest_common_words_path:
                    filtered_longest_common_words_path[key] = [i]
                else:
                    filtered_longest_common_words_path[key].append(i)

    return filtered_longest_common_words_path


def get_longest_path_recursive(longest_common_words_path, real_longest_common_words_path, actual_word, first_index,
                               last_index, final_index, increment, words_path):
    """
    This function is used to get the longest path of the longest common words.
    It is a recursive function.
    :param longest_common_words_path: The longest common words path.
    :param real_longest_common_words_path: The real longest common words path.
    :param actual_word: The actual word.
    :param first_index: The first index.
    :param last_index: The last index.
    :param final_index: The final index.
    :param increment: The increment.
    :param words_path: The words path.
    :return: The real longest common words path, the words path and the last index.

    Example:
    >>> get_longest_path_recursive(longest_common_words_path, real_longest_common_words_path, actual_word, first_index,
                               last_index, final_index, increment, words_path)
        {'a': ['0-0', '1-1', '2-2', '3-3', '4-4', '5-5', '6-6', '7-7', '8-8', '9-9', '10-10', '11-11', '12-12', '13-13', '14-14', '15-15', '16-16']}
        ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
        17
    """
    candidates = {}

    #print(real_longest_common_words_path)
    #print(actual_word)
    #print(first_index)
    #print(last_index)
    #print(final_index)
    #print(increment)
    #print('\n')

    while (last_index + increment) < final_index:
        for word in longest_common_words_path:
            for index_pair in longest_common_words_path[word]:
                first_index_value, second_index_value = index_pair.split('-')

                for i in range(0, increment):
                    for j in range(0, increment):
                        if ((int(first_index) + i) == int(first_index_value)) and ((int(last_index) + j) == int(second_index_value)):
                            if not word in candidates:
                                candidates[word] = [str(str(first_index_value) + '-' + str(second_index_value))]
                            else:
                                candidates[word].append(str(str(first_index_value) + '-' + str(second_index_value)))

        if not bool(candidates):
            real_longest_common_words_path, words_path, last_index = get_longest_path_recursive(longest_common_words_path,
                                                                                    real_longest_common_words_path,
                                                                                    actual_word,
                                                                                    first_index, last_index,
                                                                                    final_index,
                                                                                    increment + 1, words_path)
            while (last_index + increment) < final_index:
                last_index += 1
        else:
            lowest_key, lowest_index, lowest_second_index = get_lowest_index(candidates)
            if not lowest_key in real_longest_common_words_path:
                real_longest_common_words_path[lowest_key] = [str(str(lowest_index) + '-' + str(lowest_second_index))]
            else:
                real_longest_common_words_path[lowest_key].append(str(str(lowest_index) + '-' + str(lowest_second_index)))
            # words_path.append(str(str(lowest_index) + '-' + str(lowest_second_index)))
            words_path.append(str(lowest_key))
            longest_common_words_path = delete_inferiors(longest_common_words_path, lowest_index, lowest_second_index)
            real_longest_common_words_path, words_path, last_index = get_longest_path_recursive(longest_common_words_path,
                                                                                    real_longest_common_words_path,
                                                                                    lowest_key,
                                                                                    lowest_index, lowest_second_index,
                                                                                    final_index,
                                                                                    1, words_path)
            while (last_index + increment) < final_index:
                last_index += 1

    #print(words_path)

    return real_longest_common_words_path, words_path, last_index


def get_longest_path(longest_common_words_path, actual_word, first_index, last_index):
    """
    This function is the recursive function that will get the longest path of the longest common words.
    It will return a list of the longest path of the longest common words.
    :param longest_common_words_path: The longest common words path.
    :param real_longest_common_words_path: The real longest common words path.
    :param actual_word: The actual word.
    :param first_index: The first index.
    :param last_index: The last index.
    :param biggest_second_index: The biggest second index.
    :param actual_index: The actual index.
    :param longest_path: The longest path.
    :return: The longest path.

    Example:
    >>> get_longest_path_recursive({'a': {'b': {'c': {'d': {'e': {'f': {'g': {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {'q': {'r': {'s': {'t': {'u': {'v': {'w': {'x': {'y': {'z': 'z'}}}}}}}}}}}}}}}}}}}}}}}}}}}, 'a', 0, 0, 25, 1, ['a'])
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    """
    real_longest_common_words_path = {}

    real_longest_common_words_path[actual_word] = [str(str(first_index) + '-' + str(last_index))]
    return get_longest_path_recursive(longest_common_words_path, real_longest_common_words_path, actual_word,
                                      first_index, last_index, get_biggest_second_index(longest_common_words_path), 1, [actual_word])


def get_word_sequence(master_dict, slave_dict, longest_common_words_path, word_path):
    """
    This function takes in a master dictionary, a slave dictionary, a list of longest common words, and a list of words.
    It returns a list of words in the correct order.
    """
    correct_word_sequence = []
    last_master_index = 0
    last_slave_index = 0

    # print('master_dict: ' + str(master_dict))
    # print('slave_dict: ' + str(slave_dict))
    # print('longest_common_words_path: ' + str(longest_common_words_path))
    # print('word_path: ' + str(word_path))

    for word in word_path:
        lowest_index, longest_common_words_path = get_lowest_index_and_delete_index(longest_common_words_path, word)
        slave_index, master_index = lowest_index.split('-')

        # print('\nword: ' + word)
        # print('lowest_index: ' + lowest_index)
        # print('master_index: ' + master_index)
        # print('slave_index: ' + slave_index)

        if master_index > slave_index:

            # print('master_index > slave_index')

            for punctuation_mark in get_nlp_punctuation_marks():
                for j in range(int(last_master_index), int(master_index)):
                    if punctuation_mark == master_dict[j]:
                        correct_word_sequence.append(punctuation_mark)

            for i in range(int(last_slave_index), int(slave_index)-1):
                correct_word_sequence.append(slave_dict[i])

            # print(slave_dict)
            # print(int(slave_index))
            correct_word_sequence.append(master_dict[int(master_index)])
            last_master_index = master_index
            last_slave_index = slave_index
        else:
            # print('master_index > slave_index')

            for punctuation_mark in get_nlp_punctuation_marks():
                for j in range(int(last_master_index), int(master_index)):
                    if punctuation_mark == master_dict[j]:
                        correct_word_sequence.append(punctuation_mark)

            for i in range(int(last_slave_index), int(slave_index)-1):
                correct_word_sequence.append(slave_dict[i])

            # print(slave_dict)
            # print(int(slave_index))
            correct_word_sequence.append(master_dict[int(master_index)])
            last_master_index = master_index
            last_slave_index = slave_index

        # print('\tcorrect_word_sequence: ' + str(correct_word_sequence))

    return correct_word_sequence


def get_the_correct_word_sequence(master_dict, slave_dict, pixel_6_file_content_dictionary, youtube_subtitles_file_content_dictionary):
    """
    This function takes in two dictionaries, one for the pixel 6 file and one for the youtube subtitles file.
    It then finds the longest common-words path between the two dictionaries.
    It then finds the first word in the longest common-words path.
    It then deletes all the inferior paths in the longest common-words path.
    It then finds the longest path in the longest common-words path.
    It then finds the correct word sequence.
    It then returns the correct word sequence.

    Parameters:
    master_dict (dict): The dictionary for the pixel 6 file.
    slave_dict (dict): The dictionary for the youtube subtitles file.
    pixel_6_file_content_dictionary (dict): The dictionary for the pixel 6 file content.
    youtube_subtitles_file_content_dictionary (dict): The dictionary for the youtube subtitles file content.

    Returns:
    correct_word_sequence (list): The correct word sequence.

    Example:
    >>> get_the_correct_word_sequence(master_dict, slave_dict, pixel_6_file_content_dictionary, youtube_subtitles_file_content_dictionary)
        ['hello', 'world']
    """
    # get the longest common-words path
    longest_common_words_path = get_common_words(master_dict, slave_dict)

    # print(longest_common_words_path)

    first_word, first_index, last_index = get_first_word(longest_common_words_path)

    # print(first_word)

    longest_common_words_path = delete_inferiors(longest_common_words_path, first_index, last_index)

    # print(longest_common_words_path)

    longest_common_words_path, word_path, _ = get_longest_path(longest_common_words_path, first_word, first_index, last_index)

    # print(longest_common_words_path)

    correct_word_sequence = []

    correct_word_sequence = get_word_sequence(pixel_6_file_content_dictionary, youtube_subtitles_file_content_dictionary, longest_common_words_path, word_path)

    return correct_word_sequence


def delete_duplicates(correct_word_sequence, correct_word_sequence_string):
    """Remove duplicate words while preserving natural language patterns."""
    lines = correct_word_sequence_string.split('\n')
    cleaned_lines = []
    
    for line in lines:
        if not line.strip():
            cleaned_lines.append('')
            continue
            
        words = line.split()
        if not words:
            continue
            
        cleaned_words = []
        prev_word = ''
        
        for i, word in enumerate(words):
            # Preservar timestamps y formatos especiales
            if word.startswith('[') or word.endswith(']'):
                cleaned_words.append(word)
                continue
                
            # Preservar patrones naturales del lenguaje
            natural_patterns = [
                ('that', 'is'), ('this', 'is'), ('it', 'is'),
                ('there', 'is'), ('what', 'is'), ('who', 'is'),
                ('how', 'is'), ('where', 'is'), ('when', 'is'),
                ('why', 'is'), ('to', 'be'), ('will', 'be'),
                ('can', 'be'), ('must', 'be'), ('may', 'be')
            ]
            
            should_keep = False
            if i > 0:
                prev_pair = (words[i-1].lower(), word.lower())
                if prev_pair in natural_patterns:
                    should_keep = True
            
            # Evitar duplicados consecutivos excepto en patrones naturales
            if word.lower() != prev_word.lower() or should_keep:
                cleaned_words.append(word)
                prev_word = word
        
        cleaned_line = ' '.join(cleaned_words).strip()
        if cleaned_line:
            cleaned_lines.append(cleaned_line)
    
    return '\n'.join(cleaned_lines)


def delete_spaces_between_punctuation_marks(correct_word_sequence_string):
    """
    This function deletes spaces between punctuation marks.
    It is used to fix the output of the function 'get_correct_word_sequence_string'.
    The function 'get_correct_word_sequence_string' adds spaces between punctuation marks.
    This function deletes those spaces.
    The function 'get_correct_word_sequence_string' is used to get the correct word sequence of a sentence.

    Parameters:
    correct_word_sequence_string (str): The correct word sequence of a sentence.

    Returns:
    correct_word_sequence_string_fixed (str): The correct word sequence of a sentence without spaces between punctuation marks.

    Example:
    >>> delete_spaces_between_punctuation_marks('This is a sentence .')
        'This is a sentence.'
    """
    correct_word_sequence_string_fixed = correct_word_sequence_string
    punctuation_marks = get_nlp_punctuation_marks()

    for punctuation_mark in punctuation_marks:
        casuistic = ' ' + str(punctuation_mark) + ' '
        if casuistic in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(casuistic, casuistic[1:])

    return correct_word_sequence_string_fixed


def get_biggest_second_index(d):
    """
    This function takes a dictionary as an argument.
    The dictionary has keys that are strings and values that are lists of strings.
    The strings in the lists are in the format of 'first_index-second_index'.
    The function returns the second_index of the string in the list with the highest first_index.
    If there are multiple strings with the same highest first_index, the function returns the second_index of the string with the highest second_index.

    Parameters:
    d (dict): A dictionary with keys that are strings and values that are lists of strings.

    Returns:
    int: The second_index of the string in the list with the highest first_index.

    Example:
    >>> d = {'a': ['1-2', '1-3', '2-4'], 'b': ['1-1', '2-2', '3-3']}
    >>> get_biggest_second_index(d)
        3
    """
    biggest_index = None
    biggest_second_index = None

    for key, value in d.items():
        for i in value:
            first_index, second_index = i.split('-')
            if biggest_index is None or biggest_index < int(first_index):
                biggest_index = int(first_index)
                biggest_second_index = int(second_index)
            elif biggest_index == int(first_index) and biggest_second_index < int(second_index):
                biggest_second_index = int(second_index)
    return biggest_second_index


def get_word_from_dict(master_dict, actual_master_index):
    """
    This function takes in a dictionary and an index.
    It returns the word that is associated with the index.
    If the index is not in the dictionary, it returns an empty string.

    Parameters:
    master_dict (dict): The dictionary to search through.
    actual_master_index (int): The index to search for.

    Returns:
    word (str): The word associated with the index.

    Example:
    >>> get_word_from_dict({'a': [0, 1], 'b': [2, 3]}, 1)
        'a'
    """
    word = ''
    for key in master_dict.keys():
        if actual_master_index in master_dict[key]:
            word = key
    return word


def get_nearest_bigger_index_from_actual_index(int_list, actual_slave_index):
    """
    This function takes a list of integers and an integer as input.
    It returns the index of the first integer in the list that is bigger than the input integer.
    If there is no such integer, it returns -1.

    Parameters:
    int_list (list): a list of integers
    actual_slave_index (int): an integer

    Returns:
    int: the index of the first integer in the list that is bigger than the input integer
    or -1 if there is no such integer

    Example:
    >>> get_nearest_bigger_index_from_actual_index([1, 2, 3, 4, 5], 3)
        4
    >>> get_nearest_bigger_index_from_actual_index([1, 2, 3, 4, 5], 5)
        -1
    """
    nearest_bigger_index = -1
    for integer in int_list:
        if integer > actual_slave_index:
            nearest_bigger_index = integer
            break
    return nearest_bigger_index


def get_index_from_dict(slave_dict, actual_word, actual_slave_index):
    """
    This function returns the nearest bigger index from the actual index.
    If the actual index is bigger than the biggest index in the list, it returns the biggest index.
    If the actual index is smaller than the smallest index in the list, it returns the smallest index.
    If the actual index is in the list, it returns the actual index.
    If the actual index is not in the list, it returns the nearest bigger index.

    Parameters:
    slave_dict (dict): The dictionary of the slave word.
    actual_word (str): The actual word.
    actual_slave_index (int): The actual index of the slave word.

    Returns:
    int: The nearest bigger index from the actual index.

    Examples:
    >>> get_index_from_dict({"a": [1, 2, 3, 4, 5]}, "a", 3)
        3
    >>> get_index_from_dict({"a": [1, 2, 3, 4, 5]}, "a", 6)
        5
    >>> get_index_from_dict({"a": [1, 2, 3, 4, 5]}, "a", 0)
        1
    >>> get_index_from_dict({"a": [1, 2, 3, 4, 5]}, "a", 4)
        4
    """
    index = -1
    for key in slave_dict.keys():
        if actual_word == key:
            index = get_nearest_bigger_index_from_actual_index(slave_dict[key], actual_slave_index)
    return index


def get_lowest_index_and_delete_index(dictionary, word):
    """
    This function takes in a dictionary and a word.
    It then finds the lowest index of the word in the dictionary.
    It then deletes the lowest index from the dictionary.
    It then returns the lowest index and the dictionary.

    Parameters:
    dictionary (dict): The dictionary to search through.
    word (str): The word to search for.

    Returns:
    lowest_index (str): The lowest index of the word in the dictionary.
    dictionary (dict): The dictionary with the lowest index deleted.

    Example:
    >>> get_lowest_index_and_delete_index({'a': ['1-2', '3-4']}, 'a')
        ('1-2', {'a': ['3-4']})
    """
    lowest_first_index = None
    lowest_second_index = None

    for key, value in dictionary.items():
        if key == word:
            for i in value:
                first_index, second_index = i.split('-')
                if lowest_first_index is None or lowest_first_index > int(first_index):
                    lowest_first_index = int(first_index)
                    lowest_second_index = int(second_index)
                elif lowest_first_index == int(first_index) and lowest_second_index > int(second_index):
                    lowest_second_index = int(second_index)

    lowest_index = str(str(lowest_first_index) + '-' + str(lowest_second_index))
    dictionary[word].remove(lowest_index)

    return lowest_index, dictionary


def write_file(file_name, file_content, output_dir=None):
    """
    Write a file with the given name and content.

    Parameters
    ----------
    file_name : str
        The name of the file to be written.
    file_content : str
        The content to be written to the file.
    output_dir : Path, optional
        Directory where to save the file. Defaults to OUTPUT_DIR from config.
    """
    # Usar el directorio especificado o el predeterminado
    output_dir = output_dir or OUTPUT_DIR
    
    # Asegurar que el directorio de salida existe
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Usar Path para manejar las rutas de manera segura
    output_path = output_dir / file_name
    
    with open(output_path, 'w+') as f:
        f.write(file_content)

