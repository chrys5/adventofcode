import re
import os

def read_file(filename: str, strip: bool = False, delimiters: list|None = None, line_range: tuple = (None, None)):
    """
    Parse txt file into a 2D jagged array of words for each line.\n
    OPTIONAL: Specify start and end line numbers (inclusive), using 1-indexed line numbering. (default: all lines)\n
    OPTIONAL: Pass raw lines with no splitting if needed. (default: split enabled)\n
    OPTIONAL: Use a given list of delimiters for splitting. (default: space)\n
    """
    contents = []

    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path, filename), 'r') as f:
        if strip:
            lines = [line.strip() for line in f.readlines()]
        else:
            lines = [line.rstrip('\n') for line in f.readlines()]

    start, stop = line_range
    if line_range != (None, None):
        if start is None:
            start = 1
        if stop is None:
            stop = len(lines)
        lines = lines[start-1:stop]

    if delimiters is not None:
        for line in lines:
            contents.append([word for word in re.split('|'.join(map(re.escape, delimiters)), line) if word])
    else:
        contents = lines

    return contents