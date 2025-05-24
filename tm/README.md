Acest proiect implementează un emulator pentru o mașină Turing, scris în Python. Programul citește definiția mașinii dintr-un fișier text (turing.in), simulează execuția pas cu pas pe o bandă de intrare și determină dacă șirul este acceptat prin ajungerea într-o stare finală. La final, banda modificată este afișată, iar configurația mașinii este salvată în turing.out.

    Descrierea fisierului de configurare

Fișierul turing.in conține configurația completă a unei mașini Turing, exprimată într-un format text ușor de parcurs. Fiecare secțiune este urmată de marcatorul |sfarsit, indicând finalul acelei părți din descriere.

Structura fișierului:
-> stari: dicționar cu stările mașinii (numele stărilor și roluri asociate, dacă este cazul).

Exemplu: stari: q0,R; q1,R; q2,R; q3,F; |sfarsit

-> alfabet: simbolurile permise pe banda de intrare, separate prin virgulă.

Exemplu: alfabet: _,+,1; |sfarsit

-> delta: lista de tranziții, fiecare de forma: stare_curentă, simbol_citit, stare_următoare, simbol_scris, direcție(R/L), separată prin ; .

Exemplu: delta: q0,1,q0,1,R; q0,+,q1,1,R; q1,1,q1,1,R; q1,_,q2,_,L; q2,1,q3,_,R; |sfarsit

-> start: starea inițială a mașinii.

Exemplu: start: q0; |sfarsit

-> F: stare finală sau lista stărilor finale, separate prin virgulă.

Exemplu: F: q3; |sfarsit

        Modul de functionare al emulatorului
