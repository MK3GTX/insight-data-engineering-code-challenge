# Imports
from collections import Counter
import os
import re
import sys


def get_files(source):
    # Initialize list of file paths
    paths = []

    # Traverse folder for files
    for root, dirs, files in os.walk(source):
        # Alphabetize list w/assumption that all text files are lowercase
        files.sort()

        # Add files that end with .txt to list
        for file in files:
            if file.endswith('.txt'):
                paths.append(source + file)

    return paths


def read_file(file):
    # initialize words array and open file
    words = []
    f = open(file, 'r')

    # traverse file rather than reading it all into memory
    for line in f:
        # remove punctuation
        line = re.sub(r'[^\w\s]', '', line)

        # split into individual words
        for word in line.lower().split():
            words.append(word)

    # return a counter (dictionary) of words
    return Counter(words)


def write_to_file(wc_output, words):
    # open file for writing
    w = open(wc_output, 'w')

    # get sorted list of items in word then traverse it
    for key, value in sorted(words.items()):
        w.write("{}\t{}\n".format(key, value))


def main():
    # check arg length for missing args
    if len(sys.argv) != 3:
        for arg in sys.argv:
            print(arg)
        sys.exit("Invalid parameters.")

    # set vars
    wc_input = sys.argv[1]
    if wc_input[len(wc_input)-1] != "/":
        wc_input += "/"

    wc_output = sys.argv[2]

    # initialize counter
    words = Counter()
    for file in get_files(wc_input):
        words += read_file(file)

    write_to_file(wc_output, words)


if __name__ == "__main__":
    main()