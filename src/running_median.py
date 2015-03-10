# Imports
import sys
import utils
from heapq import heappush, heappushpop


# Reads file and returns wordcount
def get_word_count(file):
    word_count = []
    with open(file) as f:
        for line in f:
            word_count.append(line.count(" ") + 1)

    return word_count


# Computes the running median
def running_median():
    def gen():
        left, right = [], [(yield)]
        while True:
            heappush(left, -heappushpop(right, (yield right[0])))
            heappush(right, -heappushpop(left, -(yield ((right[0] - left[0]) / 2.0))))

    g = gen()
    next(g)
    return g


# Write output to text file
def write_to_file(wc_output, words):
    with open(wc_output, 'w') as w:
        w.write("\n".join("{0:.1f}".format(word) for word in words))


def main():
    # check arg length for missing args
    if len(sys.argv) != 3:
        sys.exit("Invalid parameters.")

    wc_input = sys.argv[1]
    if wc_input[len(wc_input) - 1] != "/":
        wc_input += "/"
    wc_output = sys.argv[2]

    medians = []
    median = running_median()
    for file in utils.get_text_files(wc_input):
        for count in get_word_count(file):
            medians.append(median.send(count))

    # output to text file
    write_to_file(wc_output, medians)


if __name__ == "__main__":
    main()