#1)

mot = input('Votre mot: ')

d = dict()
for lettre in mot:
    d[lettre] = mot.count(lettre)

print(d)

#2)

def list_to_dict(entiers:list[int]) -> dict:

    d = {}
    for e in entiers:
        if e % 2 == 0:
            d[e] = 'pair'
        else:
            d[e] = 'impair'

    return d

print(list_to_dict([1,2,3,4]))