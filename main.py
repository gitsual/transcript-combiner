import os
import sys
import subprocess
import platform

import git

from process_files import process_files


# Init-Background function
def get_files_in_both_folders_full_path():
    """
    Get the list of files that are in both folders.

    Updates
    --------
    files_in_both_folders: A global that contains the common-to-both-folders file names

    Returns
    --------
    list: A list of tuples with the file name and the full path of the file for both folders.

    Example
    --------
    >>> get_files_in_both_folders_full_path()

        files_in_both_folders = ['file1.txt', 'file2.txt']

        files_in_both_folders_full_path = [('file1.txt', '/home/user/youtube_subtitles/file1.txt', '/home/user/pixel_6_translation/file1.txt'),
         ('file2.txt', '/home/user/youtube_subtitles/file2.txt', '/home/user/pixel_6_translation/file2.txt')]
    """
    global files_in_both_folders

    # Get the directory of the script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Get the directories of the two folders
    youtube_subtitles_dir = os.path.join(script_dir, "youtube_subtitles")
    pixel_6_translation_dir = os.path.join(script_dir, "pixel_6_translation")

    # Get the list of files in the two folders
    youtube_subtitles_files = os.listdir(youtube_subtitles_dir)
    pixel_6_translation_files = os.listdir(pixel_6_translation_dir)

    # Get the list of files that are in both folders
    files_in_both_folders = list(set(youtube_subtitles_files) & set(pixel_6_translation_files))

    # Create a list of tuples with the file name and the full path of the file for both folders
    files_in_both_folders_full_path = [
        (file, os.path.join(youtube_subtitles_dir, file), os.path.join(pixel_6_translation_dir, file)) for file in
        files_in_both_folders]

    return files_in_both_folders_full_path


# UI Functions
def clear_screen():
    """
    Clears the screen.
    Works on Windows and Linux.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def print_title():
    """
    This function prints the title of the program.

    It does not take any arguments.

    It does not return anything.
    """
    clear_screen()
    print('Pixel 6 Recorder + Youtube Subtitles')
    print('====================================')
    print()


def print_menu():
    """
    Prints the menu for the user to see.
    """
    print('[1]. Combine Versions')
    print('[2]. Update')
    print('[3]. Exit')
    print()


def print_updated():
    """
    This function prints the string 'Updated!' to the console.
    """
    print('')
    print('Updated!')
    print('')


# UI Handler Functions
def get_choice(indent):
    """
    This function prompts the user for a choice.
    It takes one argument, indent, which is the number of tabs to print.
    It returns the choice.

    Examples
    --------
    >>> get_choice(0)
    Enter an option:

    >>> get_choice(1)
        Enter an option:
    """
    choice = input(('\t' * indent) + 'Enter an option: ')
    return choice


# Program Functions
def combine_versions(common_files_full_path):
    """
    This function takes a list of files in both folders and prints them out in a numbered list.
    The user is then prompted to select a file from the list.
    The selected file is then processed and the output is printed out.

    Parameters:
    files_in_both_folders_full_path (list): A list of files in both folders.

    Returns:
    None

    Example:
    >>> combine_versions(['file1', 'file2', 'file3'])

        [1].- File1
        [2].- File2
        [3].- File3
        [4 // Onwards].- Go Back

        Enter an option: 1

            Processing...

            Finished!

                Output:
                    File: /home/user/file1
                    Content: "This is the content of file1"
    """
    i = 1
    options_dict = {}
    for file, file_full_path in zip(files_in_both_folders, common_files_full_path):
        print('\t[' + str(i) + '].- ' + str(file.capitalize().replace('_', ' ')))
        options_dict[i] = file_full_path
        i += 1
    print('\t[' + str(i) + ' // Onwards].- Go Back')
    print('')
    selected_file = get_choice(1)
    print('')
    if 0 < int(selected_file) < i:
        print('\t\tProcessing...')
        _, youtube_sub, pixel_6_sub = options_dict[int(selected_file)]
        print('')
        output_file, parsed_content = process_files(pixel_6_sub, youtube_sub)
        print('\t\tFinished!')
        print('')
        print('\t\t\tOutput: ')
        print('\t\t\t\tFile: ' + str(os.getcwd()) + str(output_file))
        print('\t\t\t\tContent: "' + str(parsed_content.replace('\n', ' ') + '"'))
        print('')


def git_pull():
    """
    This function pulls the latest version of the code from the remote repository.

    Examples
    --------
    >>> git_pull()
    Already up to date.
    """
    git.cmd.Git(os.getcwd()).pull()


# Main
if __name__ == '__main__':
    """
    This function is the main function of the program.
    It is the first function to be called when the program is run.
    It is the function that calls all other functions.
    It is the function that controls the flow of the program.

    This function:
        1. Gets the full path of all files in both folders.
        2. Prints the title of the program.
        3. Prints the menu of the program.
        4. Gets the user's choice.
        5. If the user's choice is 1, it calls the combine_versions function.
        6. If the user's choice is 2, it calls the git_pull function.
        7. If the user's choice is 3, it exits the program.
        8. If the user's choice is not 1, 2, or 3, it start again from step number 2
    """
    selected_option = 0

    files_in_both_folders_full_path = get_files_in_both_folders_full_path()

    while selected_option != 3:
        print_title()
        print_menu()

        selected_option = int(get_choice(0))

        print('')

        if selected_option == 1:
            combine_versions(files_in_both_folders_full_path)
        elif selected_option == 2:
            git_pull()
            print_updated()
        elif selected_option == 3:
            sys.exit(0)
