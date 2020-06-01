from itertools import groupby

def sort_anagrams(list_of_strings):
    return [list(group) for key,group in groupby(sorted(list_of_strings,key=sorted),sorted)]

list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
print(sort_anagrams(list_of_words))