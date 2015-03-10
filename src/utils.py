import os


def get_text_files(source):
    paths = []
    for root, dirs, files in os.walk(source):
        files.sort()
        for file in files:
            if file.endswith('.txt'):
                paths.append(source + file)

    return paths