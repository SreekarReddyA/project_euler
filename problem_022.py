with open("names.txt", "r") as f:
    data = f.read()

names = [str.upper(name[1:-1]) for name in data.split(',')]
alphabets = [a for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']


def name_scores(names, alphabets):
    total_score = 0
    for i in range(len(names)):
        char_sum = sum([alphabets.index(alphabet) + 1 for alphabet in names[i]])
        total_score += (i+1) * char_sum
    return total_score

print(name_scores(sorted(names), alphabets))