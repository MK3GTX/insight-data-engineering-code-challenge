# Imports
import os
import sys
from heapq import heappush, heappushpop


def get_files(source):
    # Initialize list of file paths
    paths = []

    # Traverse folder for files
    for root, dirs, files in os.walk(source):
        # Alphabetize list
        files.sort()

        # Add files that end with .txt to list
        for file in files:
            if file.endswith('.txt'):
                paths.append(source + file)

    return paths


def read_file(file):
    # initialize words array and open file
    word_count = []
    f = open(file, 'r')

    # traverse file rather than reading it all into memory
    for line in f:
        word_count.append(line.count(" ") + 1)

    return word_count


def running_median():
    # Compute running median
    def gen():
        left, right = [], [(yield)]
        while True:
            heappush(left, -heappushpop(right, (yield right[0])))
            heappush(right, -heappushpop(left, -(yield ((right[0] - left[0]) / 2.0))))

    g = gen()
    next(g)
    return g


def write_to_file(wc_output, words):
    # open file, write to file, close file
    w = open(wc_output, 'w')
    w.write("\n".join("{0:.1f}".format(word) for word in words))
    w.close()


def main():
    # check arg length for missing args
    if len(sys.argv) != 3:
        sys.exit("Invalid parameters.")

    # set vars
    # set input folder
    wc_input = sys.argv[1]
    if wc_input[len(wc_input) - 1] != "/":
        wc_input += "/"

    # set output file
    wc_output = sys.argv[2]

    # create objects
    median = running_median()
    medians = []
    # iterate through file list
    for file in get_files(wc_input):
        for count in read_file(file):
            medians.append(median.send(count))

    # output to text file
    write_to_file(wc_output, medians)


if __name__ == "__main__":
    main()