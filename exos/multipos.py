## On commence par le code fournit pour lire le LeFFF
## Homographes du lefff ayant des @cat différentes
## on complique exprès en ne prenant pas en compte la colonne n

import collections
import re
import regex # module non standard, mais super efficace !

words = collections.defaultdict(set)
pat = re.compile("cat=([a-z]+)")

input_file = "lefff-3.4.elex"

n_line = 0
with open(input_file, 'r', encoding="ISO-8859-1") as f:
    n_line += 1
    for line in f:
        line = line.strip()
        if not line:
            continue
        row = line.split('\t')
        form = row[0]
        m = pat.search(row[3])
        if m:
            cat = m.group(1)
            words[form].add(cat)
            #ou
            #cats = words.get(form, set())
            #cats.add(cat)
            #words[form] = cats
        else:
            words.setdefault(form, set())

ambigus = [word for word in words.keys() if len(words[word]) > 1]
print(len(words.keys()))
print(len(ambigus))



def exo_1A0():
    """Première solution, en utilisant le module re. Il faut énumérer toutes
    les lettres accentuées du français."""
    
    count = 0
    for word in words:
        if re.search("[A-ZÂÄÀÉÈÊËÙÇ].*[A-ZÂÄÀÉÈÊËÙÇ]", word):
            count += 1
    print(f"Avec re. Nombre de mots qui ont plus qu'une majuscule : {count}")

def exo_1A1():
    """Deuxième solution, en utilisant des fonctions de str. On utilise alors
    la fonction isupper() qui fonctionne pour tous les caractères unicodes."""
    
    count = 0
    for word in words:
        if len([l for l in word if l.isupper()]) > 1:
            count += 1
    print(f"Avec str. Nombre de mots qui ont plus qu'une majuscule : {count}")

def exo_1A2():
    """Troisième solution, en utilisant le module regex, plus puissant que re
    mais pas dans la librairie standard. On utilise alors les propriétés
    des caractères unicodes qu'on peut énumérer avec \p{}. On peut alors
    énumérer toutes les propriétés que doivent avoir les caractères que l'on
    souhaite capturer :
    - L => Letter (lettre) pas d'équivalent simple dans re;
    - u => upper (majuscule) pas d'équivalent simple dans re.
    \p{Lu} reconnait donc les lettres majuscules."""
    
    count = 0
    for word in words:
        if regex.search("\p{Lu}.*\p{Lu}", word):
            count += 1
    print(f"Avec regex. Nombre de mots qui ont plus qu'une majuscule : {count}")

def exo_1B0():
    """Première solution avec re. Même topo."""
    
    count = 0
    for word in words:
        if re.search("([A-ZÂÄÀÉÈÊËÙÇa-zâäàéèêëùç].*\d|\d.*[A-ZÂÄÀÉÈÊËÙÇa-zâäàéèêëùç])", word):
            count += 1
    print(f"Avec re. Nombre de mots qui ont au moins un chiffre et une lettre : {count}")

def exo_1B1():
    """Deuxième solution avec les fonctions de str. Même topo."""
    
    count = 0
    for word in words:
        if [l for l in word if l.isalpha()] and [l for l in word if l.isdigit()]:
            count += 1
    print(f"Avec str. Nombre de mots qui ont au moins un chiffre et une lettre : {count}")

def exo_1B2():
    """Troisième solution : en utilisant le module regex. Même topo :
    - L => Letter (lettre) pas d'équivalent simple dans re;
    - \d => digit, existe aussi dans re."""
    
    import regex
    count = 0
    for word in words:
        if regex.search(r"(\p{L}.*\d|\d.+\p{L})", word):
            count += 1
    print(f"Avec regex. Nombre de mots qui ont au moins un chiffre et une lettre : {count}")

def exo_2A1():
    """La solution avec re. Ici, on utilise \W (les "non caractères de mot").
    Vu que le texte est déjà segmenté, il n'y a pas à gérer les espaces."""
    
    import re
    count = 0
    with open("sem_Ef9POe.conll", "r", encoding="utf-8") as infile:
        for line in infile:
            if not line.strip():
                continue
            word, pos, chunk = line.strip().split()
            if re.match(r"^\W+$", word) and pos != "PONCT":
                count += 1
    print(f"Avec re. Nombre de ponctuations annotées autrement que comme une ponctuation : {count}")

def exo_2A2():
    """La solution avec le module regex :
    - P => punctuation (ponctuation)."""
    
    import regex
    count = 0
    with open("sem_Ef9POe.conll", "r", encoding="utf-8") as infile:
        for line in infile:
            if not line.strip():
                continue
            word, pos, chunk = line.strip().split()
            if regex.match(r"^\p{P}+$", word) and pos != "PONCT":
                count += 1
    print(f"Avec regex. Nombre de ponctuations annotées autrement que comme une ponctuation : {count}")


# et maintenant, il ne nous reste plus qu'à tout lancer !

print()
print("==============================")
print()

exo_1A0()
exo_1A1()
exo_1A2()

print()
print("==============================")
print()

exo_1B0()
exo_1B1()
exo_1B2()

print()
print("==============================")
print()

exo_2A1()
exo_2A2()
