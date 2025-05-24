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

![image_alt](https://github.com/adapreda/automate/blob/19fbb8f4a10f4bec812f3a77fd608d067a02f885/pda/Screenshot%202025-05-24%20160511.png)

        Modul de functionare al emulatorului

Emulatorul simulează comportamentul unui automat cu stivă (PDA) pe baza unei descrieri externe (pda.in) și a unui șir de intrare oferit de utilizator. Automatizarea este realizată pas cu pas, respectând regulile de tranziție ale PDA-ului și folosind o stivă internă.

Pașii principali ai simulării:

1. Citirea și construirea automatului (pda.in):

-> Se extrag: stările, alfabetul de intrare, alfabetul stivei, tranzițiile (delta), starea inițială și stările finale.

-> Tranzițiile sunt încărcate sub forma:    stare_curentă, simbol_input, simbol_stivă, simbol_push, stare_următoare

2. Inițializarea simulării:

-> Emulatorul pornește din starea inițială, cu simbolul $ în stivă.

-> Inputul este împărțit în simboluri (ex: 0 1 0) și indexul începe de la 0.

3. Explorarea configurațiilor:

-> Fiecare configurație este definită printr-un triplet: (stare_curentă, poziție_input, conținut_stivă)

-> Sunt explorate toate tranzițiile posibile, inclusiv cele epsilon (e), fără a consuma simboluri sau fără a verifica vârful stivei.

4. Aplicația tranzițiilor:

-> Pentru fiecare tranziție validă:

-Se consumă simbolul de intrare, dacă este necesar.

-Se efectuează operații de tip POP (dacă simbolul de pe stivă coincide) și PUSH (dacă trebuie adăugat un nou simbol).

-Se generează o nouă configurație care este adăugată pentru explorare.

5. Verificarea acceptării:

-> Dacă una dintre configurații ajunge într-o stare finală și a fost consumat tot cuvântul, cuvântul este acceptat.

-> Dacă niciuna dintre configurațiile posibile nu duce la o stare finală cu input complet consumat, cuvântul este respins.
