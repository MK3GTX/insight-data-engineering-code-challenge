# Imports
from collections import Counter
import utils
import re
import sys


# Gets list of words
def get_word_list(file):
    with open(file) as f:
        lines = [re.sub(r'[^\w\s]', '', line) for line in f.read().splitlines()]

    return [word for line in lines
            for word in line.lower().split()]


def get_counter(word_list):
    return Counter(word_list)


def write_to_file(wc_output, words):
    with open(wc_output, 'w') as w:
        for key, value in sorted(words.items()):
            w.write("{}\t{}\n".format(key, value))


def main():
    # check arg length for missing args
    if len(sys.argv) != 3:
        for arg in sys.argv:
            print(arg)
        sys.exit("Invalid parameters.")

    wc_input = sys.argv[1]
    if wc_input[len(wc_input) - 1] != "/":
        wc_input += "/"
    wc_output = sys.argv[2]

    words = Counter()
    for file in utils.get_text_files(wc_input):
        words += get_counter(get_word_list(file))

    write_to_file(wc_output, words)


if __name__ == "__main__":
    main()