def read_file(path):
    res = []
    tree = []
    with open(path) as in_stream:
        for line in in_stream:
            if line.startswith('#'):
                continue
            elif line.isspace():
                res.append(tree)
                tree = []
            else:
                word = line.strip().split('\t')
                if not word[0].isdigit():
                    continue
                tree.append(word)
    return res


def find_head(word, tree):
    head_id = word[6]
    if head_id == '0':
        return None
    for w in tree:
        if w[0] == head_id:
            return w


parsed = read_file('fr_sequoia-ud-test.conllu')

# A.
verb_count = 0
for tree in parsed:
    for word in tree:
        if word[3] == 'VERB':
            verb_count += 1

print(f'{verb_count} verbes')

# B.
count = 0
for tree in parsed:
    for word in tree:
        head = find_head(word, tree)
        if head is not None and head[3] == 'VERB':
            count += 1
print(f'{count} mots gouvernés par des verbes')
