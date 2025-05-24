def decrip(filename):
    inputfile = open(filename, 'r')
    for linie in inputfile:
        com = linie[0]
        if linie != '' and linie != '\n' and com != '#':
            linie = linie.split(':')
            if linie[0] not in automat:
                automat[linie[0]] = {}
            linie2 = linie
            linie = list(linie[1].strip().split('; '))
        # print(linie)
        # print(linie2)
        #     if linie2[0] == 'stari':
                # for el in linie:
                #     el = list(el.strip().split(','))
                #     if len(el) >= 2:
                #         automat[linie2[0]][el[0]] = el[1]
            if linie2[0] == 'stari':
                l = linie[0].split(",")
                automat[linie2[0]] = l
            if linie2[0] == 'alfabet':
                linie = list(linie[0].strip().split(','))
                automat[linie2[0]] = linie
            if linie2[0] == 'delta':
                linie = linie[:len(linie)-1]
                l = []
                for el in linie:
                    el = el.split(',')
                    l.append(el)
                automat[linie2[0]] = l
            if linie2[0] == 'start':
                automat[linie2[0]] = linie[0]
            if linie2[0] == 'F':
                automat[linie2[0]] = linie[0]
    return automat

def criptare(automat):
    for linie in automat:
        g.write(linie.strip()+": ")
        if linie == 'stari':
            for el in range(0, len(automat['stari'])):
                if el == len(automat['stari']) -1:
                    g.write(f"{automat['stari'][el]};")
                else:
                    g.write(f"{automat['stari'][el]},")
            g.write("|sfarsit")
            g.write("\n")
        if linie == 'alfabet':
            g.write(",".join(automat['alfabet']) + "; " + "|sfarsit")
            g.write("\n")
        if linie == 'delta':
            for el in automat['delta']:
                g.write(",".join(el) + "; ")
            g.write("|sfarsit\n")
        if linie == 'start':
            g.write(automat['start'] + "; " + "|sfarsit\n")
        if linie == 'F':
            g.write(automat['F'] + "; " + "|sfarsit\n")


g = open('nfa.out','w')
automat = dict()

# afisez dictionarul format
print(decrip('nfa.in'))

def urmatoarele_stari_epsilon(stari, automat):
    stari_initiale = set(stari)
    stari_procesare = list(stari)
    while stari_procesare:
        stare = stari_procesare.pop()
        for tranzitie in automat['delta']:
            if tranzitie[0] == stare and tranzitie[1] == 'e':
                if tranzitie[2] not in stari_initiale:
                    stari_initiale.add(tranzitie[2])
                    stari_procesare.append(tranzitie[2])
    return stari_initiale

x = input()
lista_simbol = list(x.strip().split(' '))
stare_actuala = automat['start']
index = 0
accept = False
stari_prezente = set()
stari_urmatoare = set()
# stari_prezente.add(stare_actuala)
stari_prezente = urmatoarele_stari_epsilon({stare_actuala}, automat)

ok = False

if stare_actuala == automat['F']:
    print('Acceptat')
else:
    while accept == False and index <= len(lista_simbol):
        ok = False
        for stare in stari_prezente:
            for tranzitie in automat['delta']:
                if tranzitie[0] == stare:
                    if index < len(lista_simbol) and tranzitie[1] == lista_simbol[index]:
                        stari_urmatoare.add(tranzitie[2])
                        ok = True
                    # elif tranzitie[1] == 'e':
                    #     stari_urmatoare.add(tranzitie[2])
        if ok:
            index += 1
        elif not stari_urmatoare:
            break # daca nu mai avem stari urmatoare, iesim
        print(stari_prezente)
        print(stari_urmatoare)
        # stari_prezente = stari_urmatoare
        stari_prezente = urmatoarele_stari_epsilon(stari_urmatoare, automat)
        stari_urmatoare.clear()
        if automat['F'] in stari_prezente and index == len(lista_simbol):
            print('Acceptat')
            accept = True

    if not accept:
        print('Neacceptat')















criptare(decrip('nfa.in'))

















