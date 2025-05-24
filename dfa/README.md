  Acest proiect are ca scop simularea unui automat finit determinist (DFA) utilizând limbajul Python. Programul citește definiția automatului dintr-un fișier text, procesează o secvență de simboluri introdusă de utilizator și verifică dacă aceasta este acceptată de către automat. La final, structura automatului este rescrisă într-un fișier de ieșire pentru validare.

  Fișierul dfa.in conține descrierea completă a automatului finit determinist, structurată pe mai multe linii, fiecare corespunzând unui element al automatului:
-> stari: – lista stărilor, separate prin virgulă

-> alfabet: – simbolurile de intrare permise

-> delta: – lista tranzițiilor în formatul stare_curentă,simbol,stare_următoare

-> start: – starea de start a automatului

-> F: – starea finală (în versiunea actuală este o singură stare)

*Fiecare linie se încheie cu |sfarsit pentru marcarea finalului de secțiune.

  Automatul acceptă limbajul format din toate cuvintele peste alfabetul {0,1} care conțin o secvență ce duce automatul în starea q1, urmată imediat de simbolul 1, astfel încât execuția se termină în starea finală q2.

  Functia decrip(filename) deschide fisierul dfa.in si construieste un dictionar *automat* pe baza continutului. Se face parsing linie cu linie si se detecteaza tipul de informatie: stari, alfabet, tranzitii, stare de start sau stare finala.

Operații realizate:
-> Se ignoră liniile goale și comentariile (cele care încep cu #)

-> Se separă numele câmpului de conținutul său (linie.split(':'))

-> Se stochează fiecare parte a automatului în dicționarul automat:

stari → listă de stări

alfabet → listă de simboluri

delta → listă de tranziții, fiecare tranziție fiind o listă [stare_curentă, simbol, stare_următoare]

start → starea inițială

F → starea finală

  După ce automatul a fost construit, se citește o secvență de simboluri de la tastatură:

x = input()

lista_stari = list(x.strip().split(' '))

  Se pornește din starea inițială (automat['start']) și se simulează trecerea prin stări pe baza tranzițiilor din automat['delta'].

  Pentru fiecare simbol:
-> Se caută în delta o tranziție care pornește din stare_curenta și care are simbolul respectiv.

-> Dacă tranziția este găsită, stare_curenta este actualizată la noua stare.

-> După ce s-a parcurs toată secvența de simboluri, daca stare_curenta este egala cu starea finala, atunci secventa este acceptata.

Functia criptare(automat) scrie toate datele din automat într-un fișier de ieșire, în formatul original.

