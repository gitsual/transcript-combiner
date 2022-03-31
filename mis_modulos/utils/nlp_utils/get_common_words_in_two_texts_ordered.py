from utils.file_utils import get_files_content_n_to_n, print_and_export_to_log, empty_log
from utils.nlp_utils.curso_nlp_utils.clean_and_normalize_text import clean_text_and_normalize_spanish_left_ñ
from utils.spaCy_utils import string_tokenizer
from utils.vanilla_utils import get_nlp_punctuation_marks

"""
DEBUGGING UTILS
"""
import inspect
import re

debug_mode = True
code_depth = -1

empty_log()


def varname(p):
    """
    Returns the name of the variable passed as argument.

    Parameters
    ----------
    p : any
        The variable whose name is to be returned.

    Returns
    -------
    str
        The name of the variable passed as argument.

    Examples
    --------
    >>> x = 1
    >>> varname(x)
    'x'
    >>> varname(1)
    'p'
    """
    # inspect.currentframe() returns the frame object for the caller's frame.
    # inspect.getframeinfo(frame, context=1) returns a 5-tuple:
    #   (filename, line number, function name, code lines, index of current line in code lines)
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        # The regex searches for the pattern varname(varname) in the current line.
        m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            # The regex returns the variable name as group(1).
            return m.group(1)


def print_debug(code_depth, variable_name, text):
    """
    Prints the given text if debug_mode is True.
    The text is indented by the given code_depth.
    The code_depth is the number of tabs to indent the text by.

    Examples:
        >>> debug_mode = True
        >>> print_debug(0, "Hello World!")
        Hello World!
        >>> print_debug(1, "Hello World!")
            Hello World!
        >>> print_debug(2, "Hello World!")
                Hello World!
        >>> debug_mode = False
        >>> print_debug(0, "Hello World!")
        >>> print_debug(1, "Hello World!")
        >>> print_debug(2, "Hello World!")
    """
    global debug_mode

    if debug_mode:
        if text == 'FUNCTION':
            print_and_export_to_log('')
        print_and_export_to_log(('\t' * code_depth) + str(variable_name) + ': \'' + str(text).replace('\n', '\\n') + '\'')


"""
CODE FUNCTIONS
"""


def get_common_words_in_two_texts_ordered(*files_absolute_path):
    # Debugging // Header
    global code_depth

    # Debugging // Print Function Name
    print_debug(code_depth, inspect.stack()[0][3], 'FUNCTION')

    code_depth += 1

    output_file_absolute_path = str(files_absolute_path[0]).split('/')[-1]

    files_dicts_list = get_numbered_words_of_files(*files_absolute_path)

    print_debug(code_depth, varname(files_dicts_list), files_dicts_list)

    files_dicts_ordered_list = ordered_word_dicts(*files_dicts_list)

    print_debug(code_depth, varname(files_dicts_ordered_list), files_dicts_ordered_list)

    correct_word_sequence = get_the_correct_word_sequence(files_dicts_ordered_list[0], files_dicts_ordered_list[1], files_dicts_list[0], files_dicts_list[1])

    # TODO (dos listas)
    # correct_word_sequence = get_the_correct_word_sequence(master_dict, file_2_dict, files_dict_list, file_2_content)

    print_debug(code_depth, varname(correct_word_sequence), correct_word_sequence)

    # TODO
    """

    common_words_in_both_texts_ordered = ' '.join(correct_word_sequence)

    return common_words_in_both_texts_ordered
    """

    code_depth -= 1
    pass


def clean_files_content(*files):
    # Debugging // Header
    global code_depth

    # Debugging // Depth flow // 'def' starts
    code_depth += 1

    # Debugging // Print Function Name
    print_debug(code_depth, inspect.stack()[0][3], 'FUNCTION')

    # Create an empty list to store the cleaned files
    files_content_clean = []

    # Create an empty list to store the cleaned file content
    file_content_clean = []

    # Debugging // Print
    print_debug(code_depth, varname(files), files)

    # Debugging // Depth flow // 'for' starts
    code_depth += 1

    # Loop through the files
    for file in files:
        # Create an empty string to store the file content
        string_file_content = ''

        # Debugging // Print
        print_debug(code_depth, varname(files), files)

        # Debugging // Depth flow // 'for' starts
        code_depth += 1

        # Loop through the file content
        for file_content in file:
            # Check if string_file_content is empty
            if string_file_content == '':
                # If the string of the file content is empty, add the file content to the string of the file content
                string_file_content += file_content
            else:
                # If the string of the file content is not empty, add the file content with a space in between to the string of the file content
                string_file_content += ' ' + file_content

            # Debugging // Print
            print_debug(code_depth, varname(string_file_content), string_file_content)

            # Cleans the string of the file content
            file_content_clean = [clean_text_and_normalize_spanish_left_ñ(string_file_content)]

            # Debugging // Print
            print_debug(code_depth, varname(files_content_clean), files_content_clean)

        # Debugging // Depth flow // 'for' ends
        code_depth -= 1

        # Add the cleaned file content string to the list of cleaned files content
        files_content_clean.append(file_content_clean)

        # Debugging // Print
        print_debug(code_depth, varname(files_content_clean), files_content_clean)

    # Debugging // Depth flow // 'for' ends
    code_depth -= 1

    # Debugging // Depth flow // 'def' ends
    code_depth -= 1

    # Returns the list of the cleaned files content
    return files_content_clean


def create_dictionaries(*dictionaries_list):
    # Debugging // Header
    global code_depth

    # Debugging // Depth flow // 'def' starts
    code_depth += 1

    # Debugging // Print Function Name
    print_debug(code_depth, inspect.stack()[0][3], 'FUNCTION')

    # Create a list of dictionaries
    dictionaries = []

    # Debugging // Print
    print_debug(code_depth, varname(dictionaries_list), dictionaries_list)

    # Debugging // Depth flow // 'for' starts
    code_depth += 1

    # Iterate through the list of lists
    for list in dictionaries_list[0]:
        # Debugging // Print
        print_debug(code_depth, varname(list), list)

        # Convert the list into a string
        list_string = ' '.join(list)

        # Debugging // Print
        print_debug(code_depth, varname(list_string), list_string)

        # Create a list of all the words in the list
        list_words = string_tokenizer(list_string, ' '.join(get_nlp_punctuation_marks()), False)

        # Debugging // Print
        print_debug(code_depth, varname(list_words), list_words)

        # Create a dictionary where key is the word number and value is the token
        dictionary = {i: list_words[i] for i in range(len(list_words))}

        # Debugging // Print
        print_debug(code_depth, varname(dictionary), dictionary)

        # Append the dictionary to the list of dictionaries
        dictionaries.append(dictionary)

    # Debugging // Depth flow // 'for' ends
    code_depth -= 1

    # Debugging // Print
    print_debug(code_depth, varname(dictionaries), dictionaries)

    # Debugging // Depth flow // 'def' ends
    code_depth -= 1

    return dictionaries


def get_numbered_words_of_files(*files_absolute_path):
    # Debugging // Header
    global code_depth

    # Debugging // Depth flow // 'def' starts
    code_depth += 1

    # Debugging // Print Function Name
    print_debug(code_depth, inspect.stack()[0][3], 'FUNCTION')

    # Get the content of the files
    files_content = get_files_content_n_to_n(*files_absolute_path)

    # Debugging // Print
    print_debug(code_depth, varname(files_content), files_content)

    # Clean the content of the files
    files_content_clean = clean_files_content(*files_content)

    # Debugging // Print
    print_debug(code_depth, varname(files_content_clean), files_content_clean)

    # Create a dictionary of the content of the files
    files_content_clean_dictionary = create_dictionaries(files_content_clean)

    # Debugging // Print
    print_debug(code_depth, varname(files_content_clean_dictionary), files_content_clean_dictionary)

    # Debugging // Depth flow // 'def' ends
    code_depth -= 1

    return files_content_clean_dictionary


def ordered_word_dicts(*args):
    # Debugging // Header
    global code_depth

    # Debugging // Depth flow // 'def' starts
    code_depth += 1

    # Debugging // Print Function Name
    print_debug(code_depth, inspect.stack()[0][3], 'FUNCTION')

    # Create a list to hold the dictionaries we'll be returning.
    result = []

    # Debugging // Print
    print_debug(code_depth, varname(args), args)

    # Debugging // Depth flow // 'for' starts
    code_depth += 1

    # For each dictionary passed in...
    for i in range(len(args)):
        # Create a new dictionary to hold the results.
        result.append({})

        # Create a list to hold the values of the dictionary, but lowercased.
        dict_values_lower = []

        # Debugging // Depth flow // 'for' starts
        code_depth += 1

        # For each key in the dictionary...
        for value in args[i].values():
            # Add the values of the dictionary lowercased.
            dict_values_lower.append(value.lower())

            # Debugging // Print
            print_debug(code_depth, varname(dict_values_lower), dict_values_lower)

        # Debugging // Depth flow // 'for' ends
        code_depth -= 1

        # Debugging // Print
        print_debug(code_depth, varname(dict_values_lower), dict_values_lower)

        # Debugging // Depth flow // 'for' starts
        code_depth += 1

        # For each key in the dictionary...
        for key in args[i]:
            # Check if the value is in the lowercased list.
            if args[i][key] in dict_values_lower:
                # If it is, check if the value is already in the result dictionary.
                if not result[i].get(args[i][key]):
                    result[i][args[i][key]] = []
                # If it isn't, add it to the result dictionary.
                result[i][args[i][key]].append(key)

            # Debugging // Print
            print_debug(code_depth, varname(result), result)

        # Debugging // Depth flow // 'for' ends
        code_depth -= 1

    # Debugging // Depth flow // 'for' ends
    code_depth -= 1

    # Debugging // Print
    print_debug(code_depth, varname(result), result)

    # Debugging // Depth flow // 'def' ends
    code_depth -= 1

    # Return the result dictionaries.
    return result


def get_common_words(dict_1, dict_2):
    # Debugging // Header
    global code_depth

    # Debugging // Depth flow // 'def' starts
    code_depth += 1

    # Debugging // Print Function Name
    print_debug(code_depth, inspect.stack()[0][3], 'FUNCTION')

    # Create an empty dictionary called result_dict.
    result_dict = {}

    # Debugging // Print
    print_debug(code_depth, varname(dict_2), dict_2)

    # Debugging // Depth flow // 'for' starts
    code_depth += 1

    # Loop through the words in dict_2.
    for word in dict_2:
        # If the word is in dict_1...
        if word in dict_1:

            # Debugging // Print
            print_debug(code_depth, varname(word), word)

            # Create an empty list called result.
            result = []

            # Debugging // Print
            print_debug(code_depth, 'dict_1[word]', dict_1[word])

            # Debugging // Depth flow // 'for' starts
            code_depth += 1

            # Loop through the line numbers in dict_1.
            for digit_1 in dict_1[word]:

                # Debugging // Print
                print_debug(code_depth, varname(digit_1), digit_1)

                # Debugging // Print
                print_debug(code_depth, 'dict_2[word]', dict_2[word])

                # Debugging // Depth flow // 'for' starts
                code_depth += 1

                # Loop through the line numbers in dict_2.
                for digit_2 in dict_2[word]:

                    # Debugging // Print
                    print_debug(code_depth, varname(digit_2), digit_2)

                    # Debugging // Print
                    print_debug(code_depth, 'str(str(digit_1) + \'-\' + str(digit_2))', str(str(digit_1) + '-' + str(digit_2)))

                    # Add the line numbers to the result list.
                    result.append(str(str(digit_1) + '-' + str(digit_2)))

                    # Debugging // Print
                    print_debug(code_depth, varname(result), result)

                # Debugging // Depth flow // 'for' ends
                code_depth -= 1

                # Debugging // Print
                print_debug(code_depth, varname(result), result)

            # Debugging // Depth flow // 'for' ends
            code_depth -= 1

            # Debugging // Print
            print_debug(code_depth, varname(result), result)

            # Add the word and the result list to the result_dict dictionary.
            result_dict[word] = result

            # Debugging // Print
            print_debug(code_depth, varname(result_dict[word]), result_dict[word])

    # Debugging // Depth flow // 'for' ends
    code_depth -= 1

    # Debugging // Print
    print_debug(code_depth, varname(result_dict), result_dict)

    # Debugging // Depth flow // 'def' ends
    code_depth -= 1

    # Return the result_dict dictionary.
    return result_dict


def get_lowest_index(d):
    # Debugging // Header
    global code_depth

    # Debugging // Depth flow // 'def' starts
    code_depth += 1

    # Debugging // Print Function Name
    print_debug(code_depth, inspect.stack()[0][3], 'FUNCTION')

    # Create three variables: lowest_index, lowest_second_index, and lowest_key.
    lowest_index = None
    lowest_second_index = None
    lowest_key = ''

    # Debugging // Print
    print_debug(code_depth, varname(d.items()), d.items())

    # Debugging // Depth flow // 'for' starts
    code_depth += 1

    # Loop through the input dictionary.
    for key, value in d.items():

        # Debugging // Print
        print_debug(code_depth, varname(value), value)

        # Debugging // Depth flow // 'for' starts
        code_depth += 1

        # Loops through the list of strings in the value of the dictionary.
        for i in value:

            # Debugging // Print
            print_debug(code_depth, varname(i), i)

            # Splits the string ('A-B') into two parts: first_index ('A') and second_index ('B').
            first_index, second_index = i.split('-')

            # Debugging // Print
            print_debug(code_depth, varname(first_index), first_index)
            print_debug(code_depth, varname(second_index), second_index)

            # Checks if lowest_index is None or if lowest_index is greater than first_index.
            if lowest_index is None or lowest_index > int(first_index):
                # Sets lowest_index to first_index, lowest_second_index to second_index, and lowest_key to the key of the dictionary.
                lowest_index = int(first_index)
                lowest_second_index = int(second_index)
                lowest_key = key
            # If lowest_index is equal to first_index and lowest_second_index is greater than second_index
            elif lowest_index == int(first_index) and lowest_second_index > int(second_index):
                # Sets lowest_second_index to second_index and lowest_key to the key of the dictionary.
                lowest_second_index = int(second_index)
                lowest_key = key

            # Debugging // Print
            print_debug(code_depth, varname(lowest_key), lowest_key)
            print_debug(code_depth, varname(lowest_index), lowest_index)
            print_debug(code_depth, varname(lowest_second_index), lowest_second_index)

    # Debugging // Depth flow // 'for' ends
    code_depth -= 1

    # Debugging // Print
    print_debug(code_depth, varname(lowest_key), lowest_key)
    print_debug(code_depth, varname(lowest_index), lowest_index)
    print_debug(code_depth, varname(lowest_second_index), lowest_second_index)

    # Debugging // Depth flow // 'def' ends
    code_depth -= 1

    # Returns the lowest_key, lowest_index, and lowest_second_index
    return lowest_key, lowest_index, lowest_second_index


def get_first_word(longest_common_words_path):
    # Debugging // Header
    global code_depth

    # Debugging // Depth flow // 'def' starts
    code_depth += 1

    # Debugging // Print Function Name
    print_debug(code_depth, inspect.stack()[0][3], 'FUNCTION')

    # Debugging // Print
    print_debug(code_depth, varname(longest_common_words_path), longest_common_words_path)

    # Take in a dictionary of words and their corresponding index pairs.
    i = 0
    candidates = {}

    # Debugging // Depth flow // 'while' starts
    code_depth += 1

    # Iterates through the index pairs and checks if the second index is equal to i.
    while i < 5:

        # Debugging // Print
        print_debug(code_depth, varname(i), i)

        # Debugging // Print
        print_debug(code_depth, varname(longest_common_words_path.keys()), longest_common_words_path.keys())

        # Debugging // Depth flow // 'for' starts
        code_depth += 1

        for word in longest_common_words_path.keys():

            # Debugging // Print
            print_debug(code_depth, varname(word), word)
            print_debug(code_depth, varname(longest_common_words_path[word]), longest_common_words_path[word])

            # Debugging // Depth flow // 'for' starts
            code_depth += 1

            for index_pair in longest_common_words_path[word]:

                # Debugging // Print
                print_debug(code_depth, varname(index_pair), index_pair)

                if index_pair.split('-')[1] == str(i):
                    # If it is, it adds the word and the index pair to a new dictionary.
                    if word not in candidates:
                        candidates[word] = [index_pair]
                    else:
                        candidates[word].append(index_pair)

                # Debugging // Print
                # print_debug(code_depth, varname('candidates[word]'), candidates[word])
                print_debug(code_depth, varname(candidates), candidates)

            # Debugging // Depth flow // 'for' ends
            code_depth -= 1

            # Debugging // Print
            print_debug(code_depth, varname(candidates), candidates)

        # Debugging // Depth flow // 'for' ends
        code_depth -= 1

        # Debugging // Print
        print_debug(code_depth, varname(candidates), candidates)

        # Increments i by 1 and repeats the process until 5th order relationship.
        i += 1

    # Debugging // Depth flow // 'while' ends
    code_depth -= 1

    # Debugging // Print
    print_debug(code_depth, varname(candidates), candidates)
    print_debug(code_depth, varname(candidates.keys()), candidates.keys())

    final_candidate_dict = {}

    # Debugging // Depth flow // 'for' starts
    code_depth += 1

    # Iterate through the new dictionary indices.
    for candidate in candidates.keys():

        # Debugging // Print
        print_debug(code_depth, varname(candidate), candidate)
        print_debug(code_depth, varname(candidates[candidate]), candidates[candidate])

        # Debugging // Depth flow // 'for' starts
        code_depth += 1

        for index_pair in candidates[candidate]:

            # Debugging // Print
            print_debug(code_depth, varname(candidate), candidate)
            print_debug(code_depth, varname(candidates[candidate]), candidates[candidate])

            # Checks if the difference between the two indices is less than or equal to 20.
            if abs(int(index_pair.split('-')[0]) - int(index_pair.split('-')[0])) <= 20:
                # If it is, it adds the word and the index pair to a new dictionary.
                if candidate not in final_candidate_dict:
                    final_candidate_dict[candidate] = [index_pair]
                else:
                    final_candidate_dict[candidate].append(index_pair)

            # Debugging // Print
            print_debug(code_depth, varname(final_candidate_dict), final_candidate_dict)
            print_debug(code_depth, varname(final_candidate_dict[candidate]), final_candidate_dict[candidate])

        # Debugging // Depth flow // 'for' ends
        code_depth -= 1

        # Debugging // Print
        print_debug(code_depth, varname(final_candidate_dict), final_candidate_dict)

    # Debugging // Depth flow // 'for' ends
    code_depth -= 1

    # Debugging // Print
    print_debug(code_depth, varname(final_candidate_dict), final_candidate_dict)

    # Debugging // Depth flow // 'def' ends
    code_depth -= 1

    # Return the word with the lowest index pair.
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
    # Debugging // Header
    global code_depth

    # Debugging // Depth flow // 'def' starts
    code_depth += 1

    # Debugging // Print Function Name
    print_debug(code_depth, inspect.stack()[0][3], 'FUNCTION')

    # Take in a dictionary of words and their corresponding index pairs.
    i = 0
    candidates = {}

    # Create a new dictionary to hold the results.
    filtered_longest_common_words_path = {}

    # Debugging // Print
    print_debug(code_depth, varname(longest_common_words_path), longest_common_words_path)

    # Debugging // Depth flow // 'while' starts
    code_depth += 1

    # Iterate through the longest_common_words_path dictionary.
    for key in longest_common_words_path:

        # Debugging // Print
        print_debug(code_depth, varname(key), key)
        print_debug(code_depth, varname(longest_common_words_path[key]), longest_common_words_path[key])

        # Debugging // Depth flow // 'while' starts
        code_depth += 1

        # Iterate through the list of indices in the longest_common_words_path dictionary.
        for i in longest_common_words_path[key]:

            # Debugging // Print
            print_debug(code_depth, varname(i), i)

            # Split the indices ('A-B') into two separate indices ('A', 'B').
            first_index, second_index = i.split('-')

            # Debugging // Print
            print_debug(code_depth, varname(first_index), first_index)
            print_debug(code_depth, varname(second_index), second_index)

            # Check if the first index is greater than the filter_first_index and the second index is greater than the filter_last_index.
            if int(first_index) > int(filter_first_index) and int(second_index) > int(filter_last_index):
                # Check if the key is already in the filtered_longest_common_words_path dictionary.
                if key not in filtered_longest_common_words_path:
                    # If the key is not in the filtered_longest_common_words_path dictionary, we add the key and the indices to the dictionary.
                    filtered_longest_common_words_path[key] = [i]
                else:
                    # If the key is already in the filtered_longest_common_words_path dictionary, we append the indices to the list of indices.
                    filtered_longest_common_words_path[key].append(i)

            # print_debug(code_depth, varname('filtered_longest_common_words_path[key]'), filtered_longest_common_words_path[key])
            print_debug(code_depth, varname(filtered_longest_common_words_path), filtered_longest_common_words_path)

        # Debugging // Print
        print_debug(code_depth, varname(filtered_longest_common_words_path), filtered_longest_common_words_path)

        # Debugging // Depth flow // 'for' ends
        code_depth -= 1

    # Debugging // Print
    print_debug(code_depth, varname(filtered_longest_common_words_path), filtered_longest_common_words_path)

    # Debugging // Depth flow // 'for' ends
    code_depth -= 1

    # Debugging // Print
    print_debug(code_depth, varname(filtered_longest_common_words_path), filtered_longest_common_words_path)

    # Debugging // Depth flow // 'def' ends
    code_depth -= 1

    # Return the filtered_longest_common_words_path dictionary.
    return filtered_longest_common_words_path


def get_longest_path_recursive(longest_common_words_path, real_longest_common_words_path, actual_word, first_index,
                               last_index, final_index, increment, words_path):
    # Debugging // Header
    global code_depth

    # Debugging // Depth flow // 'def' starts
    code_depth += 1

    # Debugging // Print Function Name
    print_debug(code_depth, inspect.stack()[0][3], 'FUNCTION')

    # Creates a candidates dictionary.
    candidates = {}

    # Debugging // Print
    print_debug(code_depth, varname(real_longest_common_words_path), real_longest_common_words_path)
    print_debug(code_depth, varname(actual_word), actual_word)
    print_debug(code_depth, varname(first_index), first_index)
    print_debug(code_depth, varname(last_index), last_index)
    print_debug(code_depth, varname(final_index), final_index)
    print_debug(code_depth, varname(increment), increment)

    # TODO

    # Recursion starts
    while (last_index + increment) < final_index:
        # Iterates through the longest_common_words_path dictionary
        for word in longest_common_words_path:
            # Iterates through the longest_common_words_path dictionary's values.
            for index_pair in longest_common_words_path[word]:

                # Splits the index_pair string into two integers.
                first_index_value, second_index_value = index_pair.split('-')

                # It checks if the first_index integer plus the i integer is equal to the first_index_value integer and
                # if the last_index integer plus the j integer is equal to the second_index_value integer.
                for i in range(0, increment):
                    for j in range(0, increment):
                        if ((int(first_index) + i) == int(first_index_value)) and ((int(last_index) + j) == int(second_index_value)):
                            # If the condition is true, it checks if the word string is not in the candidates dictionary.
                            # It adds the index_pair string as a value to the candidates dictionary.
                            if not word in candidates:
                                candidates[word] = [str(str(first_index_value) + '-' + str(second_index_value))]
                            else:
                                candidates[word].append(str(str(first_index_value) + '-' + str(second_index_value)))
        # It checks if the candidates dictionary is empty.
        if not bool(candidates):
            # If the condition is true, it calls itself with a wider-range increment
            real_longest_common_words_path, words_path, last_index = get_longest_path_recursive(longest_common_words_path,
                                                                                    real_longest_common_words_path,
                                                                                    actual_word,
                                                                                    first_index, last_index,
                                                                                    final_index,
                                                                                    increment + 1, words_path)

            # Break the Recursion
            while (last_index + increment) < final_index:
                last_index += 1
        else:
            # If the condition is false, it calls the get_lowest_index function with the candidates dictionary.
            lowest_key, lowest_index, lowest_second_index = get_lowest_index(candidates)

            # It checks if the lowest_key string is not in the real_longest_common_words_path dictionary.
            if not lowest_key in real_longest_common_words_path:
                # If the condition is true, it adds the lowest_key string as a key to the real_longest_common_words_path dictionary and
                #         adds the index_pair string as a value to the real_longest_common_words_path dictionary.
                real_longest_common_words_path[lowest_key] = [str(str(lowest_index) + '-' + str(lowest_second_index))]
            else:
                # If the condition is false, it adds the index_pair string as a value to the real_longest_common_words_path dictionary.
                real_longest_common_words_path[lowest_key].append(str(str(lowest_index) + '-' + str(lowest_second_index)))
            # words_path.append(str(str(lowest_index) + '-' + str(lowest_second_index)))

            # It adds the index_pair string to the words_path list.
            words_path.append(str(lowest_key))

            # Delete the inferior indexes to the lowest indexes from the longest_common_words_path dictionary
            longest_common_words_path = delete_inferiors(longest_common_words_path, lowest_index, lowest_second_index)

            # Calls itself with the next word
            real_longest_common_words_path, words_path, last_index = get_longest_path_recursive(longest_common_words_path,
                                                                                    real_longest_common_words_path,
                                                                                    lowest_key,
                                                                                    lowest_index, lowest_second_index,
                                                                                    final_index,
                                                                                    1, words_path)

            # Break the recursion
            while (last_index + increment) < final_index:
                last_index += 1

    # END TODO

    # Debugging // Print
    print_debug(code_depth, varname(real_longest_common_words_path), real_longest_common_words_path)
    print_debug(code_depth, varname(words_path), words_path)
    print_debug(code_depth, varname(last_index), last_index)

    return real_longest_common_words_path, words_path, last_index


def get_longest_path(longest_common_words_path, actual_word, first_index, last_index):
    # Debugging // Header
    global code_depth

    # Debugging // Depth flow // 'def' starts
    code_depth += 1

    # Debugging // Print Function Name
    print_debug(code_depth, inspect.stack()[0][3], 'FUNCTION')

    # Create a dictionary called real_longest_common_words_path, which will contain the actual longest path.
    real_longest_common_words_path = {}

    # Add the first word to the dictionary with its index as value.
    real_longest_common_words_path[actual_word] = [str(str(first_index) + '-' + str(last_index))]

    # Debugging // Print
    print_debug(code_depth, varname(real_longest_common_words_path[actual_word]), real_longest_common_words_path[actual_word])
    print_debug(code_depth, varname(real_longest_common_words_path), real_longest_common_words_path)

    # Debugging // Depth flow // 'def' ends
    code_depth -= 1

    # Call the recursive function get_longest_path_recursive, which will do the rest of the work.
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


def get_the_correct_word_sequence(file_1_content_ordered_dictionary, file_2_content_ordered_dictionary, file_1_content_dictionary, file_2_content_dictionary):
    # Debugging // Header
    global code_depth

    # Debugging // Depth flow // 'def' starts
    code_depth += 1

    # Debugging // Print Function Name
    print_debug(code_depth, inspect.stack()[0][3], 'FUNCTION')

    # get the longest common-words path
    longest_common_words_path = get_common_words(file_1_content_ordered_dictionary, file_2_content_ordered_dictionary)

    print_debug(code_depth, varname(longest_common_words_path), longest_common_words_path)

    # get the first word
    first_word, first_index, last_index = get_first_word(longest_common_words_path)

    print_debug(code_depth, varname(first_word), first_word)

    # get the longest common-words path without the inferior indexes to first_index and last_index
    longest_common_words_path = delete_inferiors(longest_common_words_path, first_index, last_index)

    print_debug(code_depth, varname(longest_common_words_path), longest_common_words_path)

    # Get the longest common words path
    longest_common_words_path, word_path, _ = get_longest_path(longest_common_words_path, first_word, first_index, last_index)

    print_debug(code_depth, varname(longest_common_words_path), longest_common_words_path)
    print_debug(code_depth, varname(word_path), word_path)

    """
    correct_word_sequence = []

    correct_word_sequence = get_word_sequence(file_1_content_dictionary, file_2_content_dictionary, longest_common_words_path, word_path)

    """

    return longest_common_words_path


def delete_duplicates(correct_word_sequence, correct_word_sequence_string):
    """
    This function takes two arguments:
    1. correct_word_sequence: a list of words that are correct
    2. correct_word_sequence_string: a string of words that are correct

    The function then checks for duplicates in the string and removes them.
    It returns the string with the duplicates removed.
    """
    correct_word_sequence_string_fixed = correct_word_sequence_string

    """
    for word in correct_word_sequence:
        print('word: ' + str(word))
        word_lower = word.lower()
        case_1 = word_lower.capitalize() + ' ' + word_lower.capitalize()
        case_2 = word_lower.capitalize() + ' ' + word_lower
        case_3 = word_lower + ' ' + word_lower.capitalize()
        case_4 = word_lower + ' ' + word_lower

        case_5 = word_lower.capitalize() + ' . ' + word_lower.capitalize()
        case_6 = word_lower.capitalize() + ' . ' + word_lower
        case_7 = word_lower + ' . ' + word_lower.capitalize()
        case_8 = word_lower + ' . ' + word_lower

        case_9 = word_lower.capitalize() + ' , ' + word_lower.capitalize()
        case_10 = word_lower.capitalize() + ' , ' + word_lower
        case_11 = word_lower + ' , ' + word_lower.capitalize()
        case_12 = word_lower + ' , ' + word_lower

        if case_1 in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(case_1, word_lower.capitalize() + ' ')

        if case_2 in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(case_2, word_lower.capitalize() + ' ')

        if case_3 in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(case_3, word_lower.capitalize() + ' ')

        if case_4 in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(case_4, word_lower + ' ')

        if case_5 in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(case_5, ' . ' + word_lower.capitalize())

        if case_6 in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(case_6, word_lower + ' . ')

        if case_7 in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(case_7, word_lower + ' . ')

        if case_8 in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(case_8, ' . ' + word_lower.capitalize())

        if case_9 in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(case_5, ' , ' + word_lower.capitalize())

        if case_10 in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(case_6, word_lower + ' , ')

        if case_11 in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(case_7, word_lower + ' , ')

        if case_12 in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(case_8, ' , ' + word_lower.capitalize())
    """

    correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace('  ', ' ')

    return correct_word_sequence_string_fixed


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


def write_file(file_name, file_content):
    """
        Write a file with the given name and content.

        Parameters
        ----------
        file_name : str
            The name of the file to be written.
        file_content : list
            A list of strings to be written to the file.
    """
    with open('output/' + file_name, 'w+') as f:
        for line in file_content:
            f.write(line)


if __name__ == '__main__':
    get_common_words_in_two_texts_ordered('/home/lorty/Escritorio/proyectos/mis_modulos/utils/nlp_utils/correlacion_eneagrama_mbti_1.txt', '/home/lorty/Escritorio/proyectos/mis_modulos/utils/nlp_utils/correlacion_eneagrama_mbti_2.txt', '/home/lorty/Escritorio/proyectos/mis_modulos/utils/nlp_utils/correlacion_eneagrama_mbti_1.txt')
