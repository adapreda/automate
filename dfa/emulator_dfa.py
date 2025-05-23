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
g = open('dfa.out','w')
automat = dict()

# afisez dictionarul format
print(decrip('dfa.in'))


x = input()
lista_stari = list(x.strip().split(' '))
stare_curenta = automat['start']
for stare in lista_stari:
    for stare_potentiala in automat['delta']:
        if stare_potentiala[1] == stare and stare_potentiala[0] == stare_curenta:
            stare_curenta = stare_potentiala[2]
            break

if stare_curenta == automat['F']:
    print("Acceptat")
else:
    print("Neacceptat")




criptare(decrip('dfa.in'))