from itertools import permutations # I used a library
perms = [''.join(p) for p in permutations(['a','b','c'])]
print(perms) #to output