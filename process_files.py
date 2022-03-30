import re
import sys

sys.setrecursionlimit(15000)

from utils.spaCy_utils import string_tokenizer
from utils.vanilla_utils import get_nlp_punctuation_marks


def delete_duplicates(correct_word_sequence, correct_word_sequence_string):
    correct_word_sequence_string_fixed = correct_word_sequence_string

    for word in correct_word_sequence:
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

    correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace('  ', ' ')

    return correct_word_sequence_string_fixed


def delete_spaces_between_punctuation_marks(correct_word_sequence_string):
    correct_word_sequence_string_fixed = correct_word_sequence_string
    punctuation_marks = get_nlp_punctuation_marks()

    for punctuation_mark in punctuation_marks:
        casuistic = ' ' + str(punctuation_mark) + ' '
        if casuistic in correct_word_sequence_string_fixed:
            correct_word_sequence_string_fixed = correct_word_sequence_string_fixed.replace(casuistic, casuistic[1:])

    return correct_word_sequence_string_fixed


def process_files(pixel_6_file, youtube_subtitles_file):
    file_name = str(pixel_6_file).split('/')[-1]
    file_content = []

    pixel_6_file_content_dictionary, youtube_subtitles_file_content_dictionary = get_numbered_words_of_files(
        pixel_6_file,
        youtube_subtitles_file)

    master_dict, slave_dict = ordered_word_dicts(youtube_subtitles_file_content_dictionary,
                                                 pixel_6_file_content_dictionary)

    correct_word_sequence = get_the_correct_word_sequence(master_dict, slave_dict, pixel_6_file_content_dictionary, youtube_subtitles_file_content_dictionary)

    # print(correct_word_sequence)

    correct_word_sequence_string = ' '.join(correct_word_sequence)

    correct_word_sequence_string_fixed = delete_duplicates(correct_word_sequence, correct_word_sequence_string)
    correct_word_sequence_string_fixed_2 = delete_spaces_between_punctuation_marks(correct_word_sequence_string_fixed)
    correct_word_sequence_string_fixed_3 = '# ' + str(file_name.split('.')[0]) + '\n\n' + correct_word_sequence_string_fixed_2.replace('. ', '.\n')

    write_file(file_name, correct_word_sequence_string_fixed_3)

    return file_name, correct_word_sequence_string_fixed_3


def get_numbered_words_of_files(pixel_6_file, youtube_subtitles_file):
    pixel_6_file_content, youtube_subtitles_file_content = get_files_content(pixel_6_file, youtube_subtitles_file)
    pixel_6_file_content_clean, youtube_subtitles_file_content_clean = clean_files_content(pixel_6_file_content,
                                                                                           youtube_subtitles_file_content)
    pixel_6_file_content_clean_dictionary, youtube_subtitles_file_content_clean_dictionary = create_dictionaries(
        pixel_6_file_content_clean,
        youtube_subtitles_file_content_clean)
    return pixel_6_file_content_clean_dictionary, youtube_subtitles_file_content_clean_dictionary


def get_files_content(pixel_6_file, youtube_subtitles_file):
    pixel_6_file_content = read_file_content(pixel_6_file)
    youtube_subtitles_file = read_file_content(youtube_subtitles_file)

    return pixel_6_file_content, youtube_subtitles_file


def read_file_content(file):
    file_content = []

    with open(file, 'r') as f:
        file_content = f.readlines()

    return file_content


def create_dictionaries(list1, list2):
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


def clean_files_content(pixel_6_file_content, youtube_subtitles_file_content):
    pixel_6_file_content_clean = clean_file_content(pixel_6_file_content)
    youtube_subtitles_file_content_clean = clean_file_content(youtube_subtitles_file_content)

    return pixel_6_file_content_clean, youtube_subtitles_file_content_clean


def clean_file_content(list_of_strings):
    new_list = []
    for string in list_of_strings:
        if not re.match(r'^\d{2}:\d{2}$', string) and string != '\n' and string != '':
            new_list.append(string.replace('\n', ''))
    return new_list


def ordered_word_dicts(dict1, dict2):
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


def get_first_word(longest_common_words_path):
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


def get_lowest_index(d):
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


def delete_inferiors(longest_common_words_path, filter_first_index, filter_last_index):
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


def get_biggest_second_index(d):
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


def get_longest_path_recursive(longest_common_words_path, real_longest_common_words_path, actual_word, first_index,
                               last_index, final_index, increment, words_path):
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
    real_longest_common_words_path = {}

    real_longest_common_words_path[actual_word] = [str(str(first_index) + '-' + str(last_index))]
    return get_longest_path_recursive(longest_common_words_path, real_longest_common_words_path, actual_word,
                                      first_index, last_index, get_biggest_second_index(longest_common_words_path), 1, [actual_word])


def get_word_sequence(master_dict, slave_dict, longest_common_words_path, word_path):
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
    :param master_dict: dict that contains the correct text with incorrect punctuation marks
    :param slave_dict: dict that contains the incorrect text with correct punctuation marks
    :return: a dict that contains the largest common-words path, the keys are the order of the common words in the master_dict
    """

    # get the longest common-words path
    # longest_common_words_path, _ = get_longest_common_words_path(master_dict, slave_dict, common_words_path=[], actual_master_index=0, actual_slave_index=0)
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


def get_word_from_dict(master_dict, actual_master_index):
    word = ''
    for key in master_dict.keys():
        if actual_master_index in master_dict[key]:
            word = key
    return word


def get_nearest_bigger_index_from_actual_index(int_list, actual_slave_index):
    nearest_bigger_index = -1
    for integer in int_list:
        if integer > actual_slave_index:
            nearest_bigger_index = integer
            break
    return nearest_bigger_index


def get_index_from_dict(slave_dict, actual_word, actual_slave_index):
    index = -1
    for key in slave_dict.keys():
        if actual_word == key:
            index = get_nearest_bigger_index_from_actual_index(slave_dict[key], actual_slave_index)
    return index


def get_common_words(dict_1, dict_2):
    result_dict = {}
    for word in dict_2:
        if word.lower() in dict_1:
            result = []
            for digit_1 in dict_1[word.lower()]:
                for digit_2 in dict_2[word]:
                    result.append(str(str(digit_1) + '-' + str(digit_2)))
            result_dict[word] = result
    return result_dict


def get_lowest_index_and_delete_index(dictionary, word):
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
    with open('output/' + file_name, 'w+') as f:
        for line in file_content:
            f.write(line)


if __name__ == '__main__':
    process_files(
        '/home/lorty/Escritorio/proyectos/pixel_6_recorder_update/pixel_6_translation/correlacion_eneagrama_mbti.txt',
        '/home/lorty/Escritorio/proyectos/pixel_6_recorder_update/youtube_subtitles/correlacion_eneagrama_mbti.txt')
