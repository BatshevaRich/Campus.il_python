import functools


def print_longest_name(file1):
    return max(open(file1, 'r').read().split('\n'), key=len)


def count_all_lens(file1):
    return sum(map(lambda x: len(x), open(file1, 'r').read().split('\n')))
    # nreturn functools.reduce(lambda x, y: x + y, map(lambda x: len(x), open(file1, 'r').read().split('\n')))


def shortest_names(file1):
    return '\n'.join(list([x for x in open(file1, 'r').read().split('\n') if len(
    x) == len(min(open(file1, 'r').read().split('\n'), key=len))]))

def lens_of_words(file1):
    open(r"C:\Users\owner\Documents\GitHub\Campus.il\next.py\lengths.txt", "w").writelines('\n'.join(list(map(str, [len(x) for x in open(file1, 'r').read().split('\n')]))))




print(count_all_lens(r"C:\Users\owner\Documents\GitHub\Campus.il\next.py\names.txt"))
