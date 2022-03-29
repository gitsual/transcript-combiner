import os
import tkinter as tk
from tkinter import filedialog
from process_files import process_files
import threading
import time

try:
    import winsound
except ImportError:
    import os

    def playsound(frequency, duration):
        #apt-get install beep
        os.system('beep -f %s -l %s' % (frequency,duration))
else:
    def playsound(frequency, duration):
        winsound.Beep(frequency, duration)


def finished_sound():
    playsound(784, 100)
    playsound(784, 600)
    playsound(622, 600)
    playsound(698, 600)
    playsound(784, 200)
    playsound(698, 200)
    playsound(784, 800)


root = tk.Tk()
root.withdraw()

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

# Create the UI
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
