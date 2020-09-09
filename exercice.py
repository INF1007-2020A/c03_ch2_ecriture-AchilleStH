def majuscule(mot):
    resultat = ''
    for lettre in mot:
        code=0
        code=ord(lettre)
        code-=32
        lettre=chr(code)
        resultat += lettre
    return resultat


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
