

import csv
import os

verses = {}
words = {}

with open('verses_database.csv', mode = 'r') as csvfile_v:
    csv_reader_verse = csv.reader(csvfile_v)
    for row in csv_reader_verse:
        verses[row[0]] = row[1:]
with open('word_definition_database.csv', 'r') as csvfile_w:
    csv_reader_word = csv.reader(csvfile_w)
    for row in csv_reader_word:
        words[row[0]] = row[1:]


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

verse_counter = 1

# Gets the first command
clear_terminal()
print(verses[str(verse_counter)])
command = input()

# This goes through verse by verse and prints the verse definitions
# Makes the command repeat until "quit" is input
while command != "quit":
    if command == "next":
        if verse_counter == 8:
            verse_counter = 1
        clear_terminal()
        verse_counter = verse_counter + 1
        print(verses[str(verse_counter)])

    elif "law" in command:
        print(words["law"])
    elif "sin" in command or "death" in command:
        print(words["sin"])
    elif "Spirit" in command:
        print(words["spirit"])
    else:
        clear_terminal()
        command = str(verse_counter)
        print(verses[str(command)])
    command = input()