import itertools

def sequence_del(my_str):
    for item in my_str:
        # return ''.join(dict.fromkeys(my_str))
        return ''.join(c[0] for c in itertools.groupby(my_str))

print(sequence_del("ppyyyyythhhhhooonnnnn"))
print(sequence_del("SSSSsssshhhh"))
print(sequence_del("Heeyyy   yyouuuu!!!"))
