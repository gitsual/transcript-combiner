import os
import sys
import time
import subprocess
import platform
import shutil
import urllib.request
import zipfile
import json
import re
import datetime
import getpass
import socket
import urllib.request
import urllib.parse
import urllib.error




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
youtube_subtitles_files_full_path = [(file, os.path.join(youtube_subtitles_dir, file)) for file in files_in_both_folders]
pixel_6_translation_files_full_path = [(file, os.path.join(pixel_6_translation_dir, file)) for file in files_in_both_folders]

# Create a list of tuples with the file name and the full path of the file for both folders
files_in_both_folders_full_path = [(file, os.path.join(youtube_subtitles_dir, file), os.path.join(pixel_6_translation_dir, file)) for file in files_in_both_folders]

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


# Create the UI
def print_title():
    clear_screen()
    print('Pixel 6 Recorder Update')
    print('=======================')
    print()


def print_menu():
    print('1. Combine Versions')
    print('2. Update')
    print('3. Exit')
    print()


def get_choice():
    choice = input('Enter an option: ')
    return choice


def check_updates():
    print_title()
    print('Checking for updates...')
    print()
    time.sleep(2)

    try:
        with urllib.request.urlopen('https://api.github.com/repos/pixel6/pixel6-recorder/releases/latest') as url:
            data = json.loads(url.read().decode())
            tag_name = data['tag_name']
            print('Latest version:', tag_name)
            print()
            time.sleep(2)
            print('Checking installed version...')
            print()
            time.sleep(2)
            with open('version.txt', 'r') as f:
                installed_version = f.read()
                print('Installed version:', installed_version)
                print()
                time.sleep(2)
                if tag_name != installed_version:
                    print('Update available!')
                    print()
                    time.sleep(2)
                    print('Current version:', installed_version)
                    print('New version:', tag_name)
                    print()
                    time.sleep(2)
                    print('Do you want to install the update? (y/n)')
                    print()
                    choice = input()
                    if choice == 'y':
                        install_updates()
                    else:
                        print('Update installation aborted.')
                        print()
                        time.sleep(2)
                        main()
                else:
                    print('No updates available.')
                    print()
                    time.sleep(2)
                    main()
    except urllib.error.URLError as e:
        print('Error:', e.reason)
        print()
        time.sleep(2)
        main()

window = tk.Tk()
window.title("Select a file")
window.geometry("500x500")

# Create a label
label = tk.Label(window, text="Select a file")
label.grid(column=0, row=0)

# Create a dropdown menu
clicked = tk.StringVar()
clicked.set(files_in_both_folders_full_path[0][0])
dropdown_menu = tk.OptionMenu(window, clicked, *files_in_both_folders)
dropdown_menu.grid(column=0, row=1)

# Create a button
button = tk.Button(window, text="Select", command=lambda: [label.configure(text=clicked.get()), label.configure(font=("Helvetica", 20, "bold")), label.place(relx=0.5, rely=0.5, anchor=tk.CENTER), label.place(relx=0.5, rely=0, anchor=tk.N), dropdown_menu.grid_forget(), button.grid_forget(), threading.Thread(target=process_files, args=(files_in_both_folders_full_path[files_in_both_folders.index(clicked.get())][2], files_in_both_folders_full_path[files_in_both_folders.index(clicked.get())][1])).start(), label.configure(text="Done"), finished_sound(), time.sleep(5), window.destroy()])

button.grid(column=0, row=2)

window.mainloop()
