import os
import sys
import subprocess
import platform
import git
from pathlib import Path

from src.process_files import process_files
from src.utils.text_utils import get_nlp_punctuation_marks
from src.config import BASE_DIR, DATA_DIR, INPUT_DIR, OUTPUT_DIR


# Init-Background function
def get_files_in_both_folders_full_path():
    """
    Obtiene la lista de archivos que están en ambas carpetas.
    """
    # Usar las rutas definidas en config.py
    source_2_dir = INPUT_DIR / "source_2"
    source_1_dir = INPUT_DIR / "source_1"

    # Asegurarse de que los directorios existan
    source_2_dir.mkdir(parents=True, exist_ok=True)
    source_1_dir.mkdir(parents=True, exist_ok=True)

    # Obtener archivos excluyendo .gitkeep y otros archivos ocultos
    def get_valid_files(directory):
        return [f for f in os.listdir(directory) 
                if not f.startswith('.') and f != '.gitkeep']

    # Obtener la lista de archivos en ambas carpetas
    source_2_files = get_valid_files(source_2_dir)
    source_1_files = get_valid_files(source_1_dir)

    # Obtener los archivos que están en ambas carpetas
    files_in_both_folders = list(set(source_2_files) & set(source_1_files))

    # Crear lista de tuplas con nombre y rutas completas
    files_in_both_folders_full_path = [
        (file, 
         source_2_dir / file, 
         source_1_dir / file) 
        for file in files_in_both_folders
    ]

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
    print('Transcript Combiner')
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
        _, youtube_sub, source_1_sub = options_dict[int(selected_file)]
        print('')
        output_file, parsed_content = process_files(source_1_sub, youtube_sub)
        print('\t\tFinished!')
        print('')
        print('\t\t\tOutput: ')
        print('\t\t\t\tFile: ' + str(OUTPUT_DIR / output_file))
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
