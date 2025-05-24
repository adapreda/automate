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
            if linie2[0] == 'stari':
                for el in linie:
                    el = list(el.strip().split(','))
                    if len(el) >= 2:
                        automat[linie2[0]][el[0]] = el[1]
            if linie2[0] == 'alfabet':
                linie = list(linie[0].strip().split(','))
                automat[linie2[0]] = linie
            if linie2[0] == 'blank':
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
            for item in automat['stari'].items():
                g.write(item[0] + "," + item[1] + "; ")
            g.write("|sfarsit")
            g.write("\n")
        if linie == 'alfabet':
            g.write(",".join(automat['alfabet']) + "; " + "|sfarsit")
            g.write("\n")
        if linie == 'blank':
            g.write(",".join(automat['blank']) + "; " + "|sfarsit")
            g.write("\n")
        if linie == 'delta':
            for el in automat['delta']:
                g.write(",".join(el) + "; ")
            g.write("|sfarsit\n")
        if linie == 'start':
            g.write(automat['start'] + "; " + "|sfarsit\n")
        if linie == 'F':
            g.write(automat['F'] + "; " + "|sfarsit\n")

g = open('turing.out','w')
automat = dict()

print(decrip('turing.in'))



banda = ['1','1','+','1','1','_']
# print(type(banda))
stare_curenta = automat['start']

i = 0
while i < len(banda):
    tranzitie_aplicata = False
    for tranzitie in automat['delta']:
        if stare_curenta == tranzitie[0] and banda[i] == tranzitie[1]:
            banda[i] = tranzitie[3]
            stare_curenta = tranzitie[2]
            if tranzitie[4] == 'R':
                i += 1
                if i == len(banda) and len(banda) <= 50:
                    banda.append('_')
            elif tranzitie[4] == 'L' and i > 0:
                i -= 1
            else:
                print('banda este depasita la stanga')
                exit()
            tranzitie_aplicata = True
            break
    if not tranzitie_aplicata:
        if stare_curenta in automat['F']:
            print("Cuvântul este acceptat.")
        else:
            print("Cuvântul NU este acceptat.")
        break


print(banda)









criptare(decrip('turing.in'))




g.close()
