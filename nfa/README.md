  Acest proiect reprezintă un emulator pentru un automat finit nedeterminist cu tranziții epsilon (ε-NFA), implementat în Python. Programul permite citirea structurii automatului dintr-un fișier text (nfa.in), simulează execuția automatului pas cu pas pentru un șir de intrare oferit de utilizator, și determină dacă șirul este acceptat, ținând cont de tranzițiile epsilon. La final, automatul este salvat într-un fișier de ieșire (nfa.out) în același format.

  Fișierul nfa.in conține descrierea structurii unui automat finit nedeterminist cu tranziții epsilon (ε-NFA). Fiecare secțiune este urmată de simbolul |sfarsit, pentru a marca finalul ei.

  Structura fișierului este următoarea:
-> stari: lista tuturor stărilor automatului, separate prin virgulă.
  Exemplu: stari: q1,q2,q3,q4; |sfarsit
-> alfabet: simbolurile de intrare permise (fără epsilon), separate prin virgulă.
  Exemplu: alfabet: 0,1; |sfarsit
-> delta: lista tranzițiilor, fiecare de forma stare_curentă,simbol,stare_următoare, separate prin ; . Tranzițiile epsilon sunt notate cu "e".
  Exemplu: delta: q1,0,q1; q1,1,q1; q1,1,q2; q2,0,q3; q2,e,q3; q3,1,q4; q4,1,q4; q4,0,q4; |sfarsit
-> start: starea inițială a automatului.
  Exemplu: start: q1; |sfarsit
-> F: starea sau stările finale (doar una este folosită în acest script).
  Exemplu: F: q4; |sfarsit

![image_alt](https://github.com/adapreda/automate/blob/b0048ffb1f64f9527f7271ed7d08e287073cb328/nfa/Screenshot%202025-05-24%20153611.pn)

    Modul de funcționare al emulatorului
  Emulatorul citește un automat finit nedeterminist cu tranziții epsilon (ε-NFA) dintr-un fișier de intrare (nfa.in) și simulează execuția acestuia pe un șir de simboluri introdus de utilizator. Pașii principali sunt:

  Parcurgerea fișierului nfa.in și construirea automatului:
-> Automatului i se extrag stările, alfabetul, funcția de tranziție (delta), starea de start și starea finală.
-> Tranzițiile sunt stocate ca liste de forma [stare_curentă, simbol, stare_următoare].
-> Se acceptă și tranziții epsilon (e), tratate special în simulare.
  Introducerea cuvântului de test:
-> Utilizatorul introduce un șir de simboluri separate prin spații (ex: 1 0 1), care este convertit într-o listă de simboluri pentru procesare.
  Inițializarea execuției:
-> Simularea începe din starea de start, dar ia în calcul și toate stările accesibile prin epsilon-tranziții (calculul închiderii epsilon pentru starea de start).
  Procesarea șirului simbol cu simbol:
-> Pentru fiecare simbol, sunt parcurse toate stările curente.
-> Se caută tranziții valide din acele stări, iar rezultatul este o nouă mulțime de stări următoare.
-> Apoi, se aplică din nou închiderea epsilon pe noile stări.
  Verificarea acceptării:
-> Dacă la finalul parcurgerii șirului de intrare, cel puțin una dintre stările curente este stare finală, șirul este acceptat.
  In caz contrar, șirul este respins.

  Scrierea automatului într-un fișier de ieșire (nfa.out):
  -> Automatului citit din fișier i se salvează structura într-un nou fișier, în același format, pentru validare sau reutilizare.
