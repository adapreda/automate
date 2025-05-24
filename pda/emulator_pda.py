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
            if linie2[0] == 'stiva':
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
        if linie == 'stiva':
            g.write(",".join(automat['stiva']) + "; " + "|sfarsit")
            g.write("\n")
        if linie == 'delta':
            for el in automat['delta']:
                g.write(",".join(el) + "; ")
            g.write("|sfarsit\n")
        if linie == 'start':
            g.write(automat['start'] + "; " + "|sfarsit\n")
        if linie == 'F':
            g.write(automat['F'] + "; " + "|sfarsit\n")
g = open('pda.out','w')
automat = dict()

# afisez dictionarul format
print(decrip('pda.in'))


def emulator_pda(automat, x):
    lista_simbol = x.strip().split(' ')
    configuratii = []  # fiecare configurație este (stare, index curent în input, stiva)
    vizitate = set()
    configuratii.append((automat['start'], 0, ['$']))  # stiva începe cu simbolul de bază $

    while configuratii:
        configurare = configuratii.pop()
        stare = configurare[0]
        index = configurare[1]
        stiva = configurare[2]

        # cheie = (stare, index, tuple(stiva))
        # if cheie in vizitate:
        #     continue
        # vizitate.add(cheie)

        # dacă am ajuns în stare finală și am consumat tot inputul
        if stare in automat['F'].split(',') and index == len(lista_simbol):
            return True

        for tranzitie in automat['delta']:
            stare_sursa, simbol_input, simbol_stiva, simbol_push, stare_dest = tranzitie

            if stare == stare_sursa:
                # tranzitia este corecta daca nu consum input sau simbolul curent coincide cu cel din tranzitie
                input_valid = False
                if simbol_input == 'e':
                    input_valid = True
                elif index < len(lista_simbol):
                    if simbol_input == lista_simbol[index]:
                        input_valid = True

                # tranzitia este corecta daca nu fac pop pe stiva sau varful stivei e egal cu simbolul din tranzitie
                stiva_valid = False
                if simbol_stiva == 'e':
                    stiva_valid = True
                elif len(stiva) > 0:
                    if stiva[-1] == simbol_stiva:
                        stiva_valid = True

                if input_valid and stiva_valid:
                    # noul index în input
                    if simbol_input != 'e':
                        index_nou = index + 1
                    else:
                        index_nou = index
                    # copiez stiva și fac modificările
                    noua_stiva = stiva[:]
                    if simbol_stiva != 'e' and noua_stiva:
                        noua_stiva.pop()
                    if simbol_push != 'e':
                        noua_stiva.append(simbol_push)

                    # adaug noua configurație în stivă
                    configuratii.append((stare_dest, index_nou, noua_stiva))

    return False

x = input()
if emulator_pda(automat, x):
    print("Acceptat")
else:
    print("Neacceptat")

criptare(decrip('pda.in'))