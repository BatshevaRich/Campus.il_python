def are_files_equal(file1, file2):
    first = open(file1, "r")
    second = open(file2, "r")

    for line1, line2 in zip(first, second):
        if line1 != line2:
            return False
    return True

print(are_files_equal(r"C:\Users\owner\Documents\GitHub\python\book\campus\test.txt", r"C:\Users\owner\Documents\GitHub\python\book\campus\test1.txt"))