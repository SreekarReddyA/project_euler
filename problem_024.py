from utils import permutations

def lexicographic_permutations(chars, ind):
    p = permutations(chars)
    return p[ind]

print(lexicographic_permutations('0123456789', 1000000-1))