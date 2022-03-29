import re
import sys
sys.setrecursionlimit(15000)

from utils.spaCy_utils import string_tokenizer
from utils.vanilla_utils import get_nlp_punctuation_marks


def process_files(pixel_6_file, youtube_subtitles_file):
    file_name = str(pixel_6_file).split('/')[-1]
    file_content = []

    pixel_6_file_content_dictionary, youtube_subtitles_file_content_dictionary = get_numbered_words_of_files(pixel_6_file,
                                                                                                  youtube_subtitles_file)

    master_dict, slave_dict = ordered_word_dicts(youtube_subtitles_file_content_dictionary, pixel_6_file_content_dictionary)

    largest_word_sequence, useless_words = get_the_largest_word_sequence(master_dict, slave_dict)

    print(largest_word_sequence)
    print(useless_words)

    write_file(file_name, file_content)


def get_numbered_words_of_files(pixel_6_file, youtube_subtitles_file):
    pixel_6_file_content, youtube_subtitles_file_content = get_files_content(pixel_6_file, youtube_subtitles_file)
    pixel_6_file_content_clean, youtube_subtitles_file_content_clean = clean_files_content(pixel_6_file_content, youtube_subtitles_file_content)
    pixel_6_file_content_clean_dictionary, youtube_subtitles_file_content_clean_dictionary = create_dictionaries(pixel_6_file_content_clean,
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


def get_the_largest_word_sequence(master_dict, slave_dict):
    """
    :param master_dict: dict that contains the correct text with incorrect punctuation marks
    :param slave_dict: dict that contains the incorrect text with correct punctuation marks
    :return: a dict that contains the largest common-words path, the keys are the order of the common words in the master_dict
    """

    # get the longest common-words path
    longest_common_words_path = get_longest_common_words_path(master_dict, slave_dict, common_words_path=[], actual_master_index=0, actual_slave_index=0)

    print(longest_common_words_path)

    longest_common_words_path_with_indexes = {}

    for word in longest_common_words_path:
        slave_dict, word_index = get_lowest_index_and_delete_index(slave_dict, word)
        longest_common_words_path_with_indexes[word_index] = word

    return longest_common_words_path_with_indexes, slave_dict


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


def get_longest_common_words_path(master_dict, slave_dict, common_words_path, actual_master_index, actual_slave_index):
    actual_word = get_word_from_dict(master_dict, actual_master_index)
    slave_index = get_index_from_dict(slave_dict, actual_word, actual_slave_index)

    print(('\t' * actual_master_index) + 'master_dict: ' + str(master_dict))
    print(('\t' * actual_master_index) + 'slave_dict: ' + str(slave_dict))
    print(('\t' * actual_master_index) + 'common_words_path: ' + str(common_words_path))
    print(('\t' * actual_master_index) + 'actual_master_index: ' + str(actual_master_index))
    print(('\t' * actual_master_index) + 'actual_slave_index: ' + str(actual_slave_index))
    print(('\t' * (actual_master_index + 1)) + 'actual_word: ' + str(actual_word))
    print(('\t' * (actual_master_index + 1)) + 'slave_index: ' + str(slave_index))

    new_common_words_path = []

    for word in common_words_path:
        new_common_words_path.append(word)

    while slave_index != actual_slave_index and actual_master_index < len(master_dict):
        if actual_word != '':
            if slave_index == -1:
                new_common_words_path_1 = get_longest_common_words_path(master_dict, slave_dict, common_words_path, actual_master_index+1, actual_slave_index)

                new_common_words_path_2 = get_longest_common_words_path(master_dict, slave_dict, [],
                                                                        actual_master_index + 1, actual_slave_index)

                if len(new_common_words_path_1) > len(new_common_words_path_2):
                    new_common_words_path = new_common_words_path_1
                else:
                    new_common_words_path = new_common_words_path_2

                if len(new_common_words_path) > len(common_words_path):
                    common_words_path = []

                    for word in new_common_words_path:
                        common_words_path.append(word)
            else:
                new_common_words_path.append(actual_word)
                metaverse_1 = get_longest_common_words_path(master_dict, slave_dict, new_common_words_path, actual_master_index+1, slave_index+1)
                metaverse_2 = get_longest_common_words_path(master_dict, slave_dict, common_words_path, actual_master_index+1, slave_index+1)
                metaverse_3 = get_longest_common_words_path(master_dict, slave_dict, [], actual_master_index+1, slave_index+1)


                if len(metaverse_1) > len(metaverse_2):
                    if len(metaverse_3) > len(metaverse_1):
                        if len(metaverse_3) > len(common_words_path):
                            common_words_path = []

                            for word in metaverse_3:
                                common_words_path.append(word)
                    else:
                        if len(metaverse_1) > len(common_words_path):
                            common_words_path = []

                            for word in metaverse_1:
                                common_words_path.append(word)
                else:
                    if len(metaverse_3) > len(metaverse_2):
                        if len(metaverse_2) > len(common_words_path):
                            common_words_path = []

                            for word in metaverse_3:
                                common_words_path.append(word)
                    else:
                        if len(metaverse_2) > len(common_words_path):
                            common_words_path = []

                            for word in metaverse_2:
                                common_words_path.append(word)
        else:
            new_common_words_path_1 = get_longest_common_words_path(master_dict, slave_dict, common_words_path,
                                                                  actual_master_index + 1, actual_slave_index)
            new_common_words_path_2 = get_longest_common_words_path(master_dict, slave_dict, [],
                                                                  actual_master_index + 1, actual_slave_index)

            if len(new_common_words_path_1) > len(new_common_words_path_2):
                new_common_words_path = new_common_words_path_1
            else:
                new_common_words_path = new_common_words_path_2

            if len(new_common_words_path) > len(common_words_path):
                common_words_path = []

                for word in new_common_words_path:
                    common_words_path.append(word)

    print(('\t' * (actual_master_index + 1)) + '[After Method] common_words_path: ' + str(common_words_path))

    return common_words_path


def get_lowest_index_and_delete_index(slave_dict, word):
    int_list = slave_dict[word]
    lowest_index = int_list[min(int_list)]
    slave_dict[word] = int_list.remove(lowest_index)

    return lowest_index, slave_dict


def write_file(file_name, file_content):
    with open('output/' + file_name, 'w+') as f:
        for line in file_content:
            f.write(line)


if __name__ == '__main__':
    process_files('/home/lorty/Escritorio/proyectos/pixel_6_recorder_update/pixel_6_translation/correlacion_eneagrama_mbti.txt', '/home/lorty/Escritorio/proyectos/pixel_6_recorder_update/youtube_subtitles/correlacion_eneagrama_mbti.txt')