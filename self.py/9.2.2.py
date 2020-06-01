def copy_file_content(source, destination):
    pasted_file = open(destination, 'w')
    pasted_file.writelines(open(source, 'r').readlines())



copy_file_content(r"C:\Users\owner\Documents\GitHub\python\book\campus\copy.txt", r"C:\Users\owner\Documents\GitHub\python\book\campus\paste.txt")