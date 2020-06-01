def edit_file(file1, action):
    input_file = open(file1)
    lines = input_file.readlines()
    words = []
    for line in lines:
        cur = line.split()
        for l in cur:
            words.append(l)
    if action == 'sort':
        return sorted(words)
    if action == 'rev':
        words = words[::-1]
        return [w[::-1] for w in words]
    if action == 'last':
        num_of_rows = int(input('enter a number'))
        return ''.join(lines[-num_of_rows:])


print(edit_file(r"C:\Users\owner\Documents\GitHub\python\book\campus\test.txt", 'last'))