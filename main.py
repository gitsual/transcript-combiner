import os
import sys
import subprocess
import platform

import git

from process_files import process_files


def get_files_in_both_folders_full_path():
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
    # Create a list of tuples with the file name and the full path of the file
    youtube_subtitles_files_full_path = [(file, os.path.join(youtube_subtitles_dir, file)) for file in
                                         files_in_both_folders]
    pixel_6_translation_files_full_path = [(file, os.path.join(pixel_6_translation_dir, file)) for file in
                                           files_in_both_folders]
    # Create a list of tuples with the file name and the full path of the file for both folders
    files_in_both_folders_full_path = [
        (file, os.path.join(youtube_subtitles_dir, file), os.path.join(pixel_6_translation_dir, file)) for file in
        files_in_both_folders]

    return files_in_both_folders_full_path


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


# Create the UI
def print_title():
    clear_screen()
    print('Pixel 6 Recorder + Youtube Subtitles')
    print('====================================')
    print()


def print_menu():
    print('[1]. Combine Versions')
    print('[2]. Update')
    print('[3]. Exit')
    print()


def get_choice(indent):
    choice = input(('\t' * indent) + 'Enter an option: ')
    return choice


def git_pull():
    output = subprocess.check_output(['git', 'pull'])
    return output


def print_updated():
    print('')
    print('Updated!')
    print('')


if __name__ == '__main__':
    selected_option = 0

    files_in_both_folders_full_path = get_files_in_both_folders_full_path()

    while selected_option != 3:
        print_title()
        print_menu()

        selected_option = int(get_choice(0))

        print('')

        if selected_option == 1:
            i = 1
            options_dict = {}
            for file, file_full_path in zip(files_in_both_folders, files_in_both_folders_full_path):
                print('\t[' + str(i) + '].- ' + str(file.capitalize().replace('_', ' ')))
                options_dict[i] = file_full_path
                i += 1

            print('\t[' + str(i) + ' - Onwards].- Go Back')
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

        elif selected_option == 2:
            git.cmd.Git(os.getcwd()).pull()
            print_updated()
        elif selected_option == 3:
            sys.exit(0)
