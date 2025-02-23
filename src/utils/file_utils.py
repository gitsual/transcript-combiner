import os

"""
print_and_export_to_log(text)
    Prints a string to the console and also appends it to a log file.

read_file_content(file)
    Reads the content of a file and returns it as a list of strings.
        
        >>> read_file_content('test.txt')
        ['This is a test file.', 'It has two lines.']
"""


def print_and_export_to_log(text):
    """
    Prints a string to the console and also appends it to a log file.

    :param text: The text to be printed and logged.
    :return: information_log_file: The file object of the log file.
    """
    print(str(text))
    information_log_file = open('/'.join(os.getcwd().split('/')[:-1]) + '/log/application_log.txt', 'a')
    information_log_file.write(str(text) + '\n')
    information_log_file.close()

    return information_log_file


def empty_log():
    open('/'.join(os.getcwd().split('/')[:-1]) + '/log/application_log.txt', 'w+')


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


def get_files_content_n_to_1(*files):
    files_content = []

    for file in files:
        files_content.append(read_file_content(file))

    files_content = ''.join(files_content)

    return files_content


def get_files_content_n_to_n(*files):
    files_content = []

    for file in files:
        files_content.append(read_file_content(file))

    return files_content