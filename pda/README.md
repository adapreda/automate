Acest proiect reprezintă un emulator pentru un automat cu stivă (PDA), implementat în Python. Programul citește descrierea automatului dintr-un fișier text (pda.in), simulează procesarea unui cuvânt simbol cu simbol, utilizând o stivă internă, și determină dacă acesta este acceptat prin stare finală. La final, automatul este salvat într-un fișier de ieșire (pda.out) în același format.

    Fisierul de configurare pda.in

Fișierul pda.in conține descrierea unui automat cu stivă (PDA), utilizat de emulator pentru simularea acceptării unui cuvânt, fiecare secțiune fiind urmată de marcatorul |sfarsit.

Structura fișierului:
-> stari: lista tuturor stărilor automatului, separate prin virgulă.
Exemplu: stari: q1,q2,q3,q4; |sfarsit

-> alfabet: simbolurile posibile din șirul de intrare, separate prin virgulă.
Exemplu: alfabet: 0,1; |sfarsit

-> stiva: simbolurile permise în stivă, separate prin virgulă.
Exemplu: stiva: 1,0,$; |sfarsit

-> delta: lista tranzițiilor, fiecare de forma *stare_curentă,simbol_input,simbol_de_pe_stivă,simbol_de_pus_în_stivă,stare_următoare*,separate prin ;. 
  Tranzițiile ε (epsilon) sunt notate cu e.
Exemplu: delta: q1,e,e,$,q2; q2,0,e,0,q2; q2,1,e,1,q2; q2,e,e,e,q3; q3,0,0,e,q3; q3,1,1,e,q3; q3,e,$,e,q4; |sfarsit

-> start: starea inițială a automatului.
Exemplu: start: q1; |sfarsit

-> F: stare sau stări finale, separate prin virgulă dacă sunt mai multe.
Exemplu: F: q4; |sfarsit

![image_alt]()
