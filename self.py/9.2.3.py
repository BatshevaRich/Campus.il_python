def who_is_missing(file_name):
    numbers = sorted(open(file_name, 'r').read().split(','))
    numbers = list(map(int, numbers))
    start, end = int(numbers[0]), int(numbers[-1])
    return ''.join(str(set(range(start, end + 1)).difference(numbers)))


open(r"C:\Users\owner\Documents\GitHub\python\book\campus\found.txt", 'w').write(who_is_missing(r"C:\Users\owner\Documents\GitHub\python\book\campus\findMe.txt"))